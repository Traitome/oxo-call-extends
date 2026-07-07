---
name: rnaquast
category: expression
description: Evaluate RNA-Seq assembly quality against a reference genome and a gene database; produces per-transcript and per-gene metrics comparable to QUAST for genome assemblies.
tags: ["rnaquast", "assembly", "evaluation", "rna-seq", "transcriptome", "quast"]
author: oxo-call-community
source_url: "https://github.com/ablab/rnaquast"
---

## Concepts

- **Tool Overview**: rnaQUAST (v2.3.2, ablab / Center for Algorithmic Biotechnology) is a tool for evaluating RNA-Seq assembly quality. It mirrors the QUAST genome-assembly tool but is specialized for transcriptome assemblies: it compares assembled transcripts to a reference genome and a gene database (e.g., BUSCO, OMArk, or a curated set of full-length isoforms) and reports per-transcript and per-gene statistics.
- **Core Function**: Takes a set of assembled transcripts (FASTA, possibly multiple files for multiple assemblers), a reference genome, and an optional gene database; produces a quality report (HTML) and a set of TSV tables with metrics including: number of assembled transcripts, fraction of full-length isoforms, fraction of genes with at least one assembled isoform, N50, E90N50, and per-base coverage of the gene database.
- **Algorithm**: Aligns each assembled transcript to the reference genome with `gmap` (or `minimap2` in newer versions), calls the best genomic locus, and compares the gene-database coordinates to the assembled coordinates. The metric `E90N50` is the N50 of the longest transcripts that cover ≥ 90% of the gene-database entries — a transcriptome-specific quality measure.
- **Input Format**: (1) One or more FASTA files of assembled transcripts (multiple assemblers can be passed as separate `--transcripts` arguments for side-by-side comparison); (2) a reference genome FASTA; (3) an optional gene database (GFF/GTF with full-length isoforms); (4) optional short-read alignments (BAM) for read-coverage-based metrics.
- **Output Format**: A `rnaQUAST_results/` directory containing: a `report.html` (the main deliverable), a `short_report.html`, per-assembler sub-directories with detailed metrics, and a `stats` directory with per-transcript TSVs. JSON output is also available via `--output-format json`.
- **Use Case**: Comparing multiple transcriptome assemblers (Trinity, rnaSPAdes, TransABySS, Oases, StringTie) on the same data set, validating a de novo assembly against a well-annotated model organism, and computing the "match ratio" for a custom transcript set against a gene database.

## Pitfalls

- **CRITICAL — Reference genome must be a DNA FASTA, not a transcriptome**: rnaQUAST aligns transcripts to a genomic DNA reference. Passing a transcriptome FASTA (with introns removed) will misalign long transcripts and inflate "fused" / "fragmented" counts. Use a true genome assembly (FASTA, one record per chromosome/scaffold).
- **CRITICAL — Gene database GFF/GTF must be coordinate-sorted and indexed**: A GFF without `gff_sort` or with duplicate transcript IDs will cause the gene-database coverage calculation to fail silently. Pre-process with `gffread` + `grep -v "#"` + `sort -k1,1 -k4,4n`.
- **Multiple `--transcripts` arguments are compared side-by-side**: This is the default behavior, not a bug. To compare only one assembler, pass a single `--transcripts` argument; the output still uses the multi-assembler directory layout but with one column.
- **gmap must be on PATH and built for the reference genome**: rnaQUAST calls `gmap` internally. For large genomes (human, mouse), build a gmap index first with `gmap_build -d <db_name> -k 15 genome.fa` and pass it via `--gmap-index <db_name>`. The Bioconda recipe installs gmap but does not pre-build any index.
- **`--read-sam` requires coordinate-sorted BAMs**: If the BAM is sorted by read name, the read-coverage metric (`E90N50`) is wrong. Sort with `samtools sort -o sorted.bam -@ 8 input.bam` first.
- **The HTML report uses an older CSS framework and may render poorly in some browsers**: Save the page or convert with `wkhtmltopdf report.html report.pdf` for a more reproducible snapshot.

## Examples

### Evaluate a single assembly
**Args:** `rnaquast.py --transcripts assembled.fa --reference genome.fa -o results/`
**Explanation:** `--transcripts` is the assembled transcripts (FASTA), `--reference` is the reference genome (FASTA), `-o` is the output directory. Produces `results/report.html` with all metrics for a single assembler.

### Compare multiple assemblers
**Args:** `rnaquast.py --transcripts trinity.fa --transcripts rnaspades.fa --transcripts stringtie.fa --reference genome.fa -o compare/`
**Explanation:** Three `--transcripts` arguments are passed; the output `compare/report.html` shows per-assembler columns with N50, E90N50, full-length-isoform counts, and matched-gene counts side-by-side. This is the canonical "which assembler is best" run.

### Use a gene database for full-length isoform counts
**Args:** `rnaquast.py --transcripts assembled.fa --reference genome.fa --gene-database genes.gff -o with_db/`
**Explanation:** `--gene-database` adds a GFF/GTF of full-length isoforms; rnaQUAST reports how many database isoforms are fully covered by the assembly. The `-db` and `-dbf` flags also accept FASTA of protein sequences for translated searches.

### Build a gmap index for a large genome
**Args:** `gmap_build -d hg38 -k 15 hg38.fa && rnaquast.py --transcripts transcripts.fa --reference hg38.fa --gmap-index hg38 -o results/`
**Explanation:** `gmap_build` indexes the reference; `--gmap-index hg38` reuses the index. For human/mouse, this saves ~30 minutes per rnaquast run when iterating on different assemblies.

### Use short-read BAMs for read-coverage metrics
**Args:** `rnaquast.py --transcripts assembled.fa --reference genome.fa --read-sam aligned.bam -o with_reads/`
**Explanation:** `--read-sam` (also accepts a sorted BAM) enables per-transcript read-coverage metrics; combined with `-d` for a gene database, the E90N50 metric is computed. This is the canonical setup for a thorough assembly evaluation.

### JSON output for downstream parsing
**Args:** `rnaquast.py --transcripts assembled.fa --reference genome.fa --output-format json -o json_run/`
**Explanation:** `--output-format json` writes `json_run/report.json` with all metrics in a machine-readable format, suitable for ingestion by a comparison script (e.g., a Snakemake benchmark rule). HTML is still produced alongside.

### Skip read-coverage and gmap steps
**Args:** `rnaquast.py --transcripts assembled.fa --reference genome.fa --no-read-coverage --no-gmap -o quick/`
**Explanation:** `--no-read-coverage` and `--no-gmap` skip the slow gmap alignment and read-coverage computation, producing only alignment-free metrics (N50, transcript counts, length statistics). Use this for a quick sanity check before running the full pipeline.
