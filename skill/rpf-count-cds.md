---
name: rpf-count-cds
category: utility
description: Python script for counting Ribosome-Protected Fragment (RPF) reads that map to the Coding Sequence (CDS) of a gene, producing per-gene RPF counts for Ribo-Seq analysis.
tags: ["rpf-count-cds", "rpf", "ribo-seq", "cds-counting", "ribosome-profiling"]
author: oxo-call-community
source_url: "https://github.com/xzt41/RPF-count-CDS"
---

## Concepts

- **Tool Overview**: rpf-count-cds (v0.0.1, xzt41) is a small Python script for counting Ribosome-Protected Fragment (RPF) reads that map to the Coding Sequence (CDS) region of each gene in a Ribo-Seq experiment. The output is a per-gene RPF count table suitable for differential translation analysis.
- **Core Function**: Takes a BAM file of RPF reads and a GTF annotation, and reports the number of RPF reads that fall within the CDS of each gene. By default, only reads in the correct reading frame (frame 0, 1, or 2) and of a typical RPF length (26–34 nt) are counted. The output is a TSV with one row per gene.
- **Algorithm**: A featureCounts-style counting algorithm: (1) parse the GTF to get the CDS coordinates per gene; (2) iterate over the BAM and assign each read to a gene if the read's 5' end falls within the CDS; (3) optionally filter by read length and frame; (4) write the per-gene count matrix.
- **Input Format**: (1) A BAM file of RPF reads (coordinate-sorted, indexed); (2) a GTF annotation. Optional: a read-length filter (e.g., `--min-length 26 --max-length 34`) and a frame filter (e.g., `--frame 0` for in-frame only).
- **Output Format**: A TSV with one row per gene: `gene_id, num_rpf_reads, num_in_frame_reads, mean_read_length`. The first column is the gene ID; the second is the total RPF count; the third is the in-frame subset. A summary of the read-length distribution is also written to a separate file.
- **Use Case**: The standard CDS-counting step in a Ribo-Seq analysis (canonical use case), preparing per-gene RPF counts for differential translation with `anota2seq` or `riborex`, QC-ing a Ribo-Seq library by computing the frame distribution, and producing the RPF counts for the denominator of a translation-efficiency calculation.

## Pitfalls

- **CRITICAL — The BAM must be coordinate-sorted and indexed**: featureCounts-style counting requires a coordinate-sorted BAM with a `.bai` index. Pre-process with `samtools sort -o sorted.bam input.bam && samtools index sorted.bam`.
- **CRITICAL — Read length and frame filters are applied AFTER counting, not before**: The default behavior is to count all reads in the CDS, then filter to the in-frame, length-correct set. The output's `num_in_frame_reads` column is the filtered count. If downstream tools expect the unfiltered count, use `--no-filter`.
- **Multi-mapping reads are counted ONCE (or many times, depending on `--allow-multimapping`)**: By default, multi-mapping reads are counted once at their primary alignment. Use `--allow-multimapping` to count them at each alignment (e.g., for reads from repetitive rRNA loci).
- **The script does not handle overlapping genes**: If two genes have overlapping CDS regions (common in compact genomes), a read in the overlap is assigned to the first gene. Pre-filter with `bedtools intersect` to assign reads to a single gene.
- **No normalization (RPKM, TPM) is applied**: The output is raw counts. Normalize upstream with `DESeq2` (size factors) or `edgeR` (TMM) for differential analysis.
- **The default frame filter is `frame == 0` (in-frame)**: A Ribo-Seq library with a high in-frame fraction (e.g., 60–70%) is expected; a low fraction (e.g., 20%) suggests a library-prep issue. Verify with a metagene plot.

## Examples

### Basic RPF counting
**Args:** `rpf-count-cds --bam ribo.bam --gtf annotation.gtf --out rpf_counts.tsv`
**Explanation:** `--bam` is the RPF BAM file, `--gtf` is the gene annotation, `--out` is the output TSV. The output has one row per gene with the total and in-frame RPF counts.

### Specify read length range
**Args:** `rpf-count-cds --bam ribo.bam --gtf annotation.gtf --min-length 26 --max-length 34 --out rpf_counts_filtered.tsv`
**Explanation:** `--min-length 26 --max-length 34` restricts the analysis to reads of 26–34 nt (the typical RPF length range). Excludes very short or very long reads that are likely contaminants.

### Count all reads, no frame filter
**Args:** `rpf-count-cds --bam ribo.bam --gtf annotation.gtf --no-filter --out rpf_counts_all.tsv`
**Explanation:** `--no-filter` counts all reads in the CDS, regardless of frame or length. Useful for QC or for downstream tools that re-filter.

### Use as input to differential translation
**Args:** `rpf-count-cds --bam ribo.bam --gtf annotation.gtf --out rpf_counts.tsv && featureCounts -a annotation.gtf -o rna_counts.txt rna.bam && anota2seq --countmat rpf_counts.tsv,rna_counts.txt --conditions treat,ctrl --out anota2seq_out/`
**Explanation:** Composite: count RPF reads, count RNA-Seq reads, then run `anota2seq` for differential translation. The output reports genes with significant changes in translation efficiency.

### Restrict to a specific chromosome
**Args:** `samtools view -b ribo.bam chr1 > ribo_chr1.bam && samtools index ribo_chr1.bam && rpf-count-cds --bam ribo_chr1.bam --gtf annotation.gtf --out rpf_chr1.tsv`
**Explanation:** Composite: pre-filter the BAM to a specific chromosome, then count. Useful for per-chromosome analyses or for running the script in parallel per chromosome.

### Output a per-read-length distribution
**Args:** `rpf-count-cds --bam ribo.bam --gtf annotation.gtf --out-length-dist length_dist.tsv --out rpf_counts.tsv`
**Explanation:** `--out-length-dist` writes the per-read-length distribution of RPF reads (a histogram of read lengths). Useful for QC and for choosing the read-length filter.

### Use a custom gene ID regex
**Args:** `rpf-count-cds --bam ribo.bam --gtf annotation.gtf --gene-id-regex "gene_id \"([^\"]+)\"" --out rpf_counts.tsv`
**Explanation:** `--gene-id-regex` specifies a custom regex for parsing the gene_id from the GTF attributes. Required for non-standard GTFs (e.g., from a custom annotator).
