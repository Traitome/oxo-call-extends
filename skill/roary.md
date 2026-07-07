---
name: roary
category: utility
description: Rapid large-scale prokaryote pan-genome analysis; takes annotated prokaryote assemblies (GFF3) and produces a pan-genome (core + accessory genes), a presence/absence matrix, and per-gene alignments for downstream phylogenetics.
tags: ["roary", "pangenome", "prokaryote", "core-genome", "accessory-genome", "presence-absence"]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/Roary"
---

## Concepts

- **Tool Overview**: Roary (v3.13.0, Sanger / Andrew Page) is the workhorse tool for prokaryote pan-genome analysis. It takes a set of annotated assemblies (GFF3 from PROKKA or similar) and produces the core gene alignment, the accessory gene presence/absence matrix, and per-gene FASTA alignments for downstream phylogenetics.
- **Core Function**: (1) Pre-cluster the contigs into coding sequences (CDS) per genome; (2) build a homologous gene group catalog via `cd-hit` and `BLASTP`-based clustering; (3) build a presence/absence matrix; (4) align the core genes with `MUSCLE`/`MAFFT`; (5) concatenate the core alignment for core-SNP / core-gene phylogenetics; (6) emit a multi-FASTA of each core gene for downstream tools (e.g., RAxML, IQ-TREE).
- **Algorithm**: A heuristic iterative clustering: (1) Pre-filter with `cd-hit-est` to collapse identical sequences; (2) BLASTP all-vs-all to build a similarity graph; (3) `MCL` to identify homologous gene groups; (4) `MAFFT`/`MUSCLE` for per-group alignment; (5) `FastTree` for the per-gene tree. The pan-genome matrix is the union of the per-genome group memberships.
- **Input Format**: A directory of GFF3 files (one per genome), one per isolate. The GFF3 must have the `CDS` features and the `FASTA` sequences at the end (PROKKA produces this format by default). A `--gff` directory or a single `gff` glob is accepted.
- **Output Format**: A directory with: `gene_presence_absence.csv` (the matrix), `gene_presence_absence.Rtab` (binary form), `core_gene_alignment.aln` (concatenated core alignment), `pan_genome_reference.fa` (a single representative sequence per group), per-group FASTA alignments, and an `accessory_binary_genes.fa` (a presence/absence tree). The standard outputs are usable by downstream tools (Roary2fripan, SCOARY, pigz, etc.).
- **Use Case**: The canonical pan-genome analysis of a set of bacterial isolates (e.g., 100 Klebsiella genomes), core-gene phylogenetics for outbreak tracking, accessory-gene association with phenotype (via SCOARY), and rapid screening of the pan-genome for lineage-specific markers.

## Pitfalls

- **CRITICAL — Input GFF3 must have the FASTA appended**: Roary requires the GFF3 to include the genome's nucleotide FASTA after the `##FASTA` directive. PROKKA produces this; bakta and other annotators do not by default. Verify with `grep "##FASTA" input.gff`.
- **CRITICAL — Contigs must be present in the GFF3 sequence headers**: If the GFF3 lists `NODE_1` but the FASTA has `>contig_1`, the `BEDTools` `getfasta` step fails. Normalize the IDs with `sed` before running Roary.
- **`-i` is the minimum BLASTP identity (NOT the input file)**: `-i 95` requires 95% identity to merge two genes into a group. The default is 50% (very lenient); for closely related isolates, use 70–95% to avoid merging paralogs.
- **`-c` is the minimum number of genomes a gene must appear in to be "core"**: Default is `99% of the input genomes`. For 100 genomes, a core gene must be in 99. For 10 genomes, 9. Adjust with `-cd 100` for "strict core".
- **Roary is RAM-hungry for large inputs**: 5000 genomes needs ~500 GB RAM (the BLASTP all-vs-all step scales quadratically). Split the input or use `panaroo` (a faster alternative) for very large pan-genomes.
- **The `pan_genome_reference.fa` is NOT a true reference**: It is a concatenation of one representative per group; not suitable for variant calling (which needs a single-genome reference). Use the original PROKKA assembly for variant calling.

## Examples

### Basic Roary run on a directory of GFF3 files
**Args:** `roary -f output_dir/ -e -n -v *.gff`
**Explanation:** `-f` is the output directory, `-e` enables MAFFT for the per-gene alignment (faster than MUSCLE for large sets), `-n` enables fast clustering (cd-hit pre-filtering), `-v` is verbose. `*.gff` is a glob of the input GFF3 files.

### Tighten the BLASTP identity threshold
**Args:** `roary -f output_dir/ -e -n -i 90 *.gff`
**Explanation:** `-i 90` requires 90% BLASTP identity to merge two genes into a group (default 50%). Use 70–95% for closely related species to avoid merging paralogs.

### Adjust the core-gene threshold
**Args:** `roary -f output_dir/ -e -n -cd 100 *.gff`
**Explanation:** `-cd 100` requires a gene to be in 100% of input genomes to be "core" (default 99%). Use `-cd 100` for a strict core alignment in core-gene phylogenetics.

### Limit to a single thread for memory-constrained runs
**Args:** `roary -f output_dir/ -e -n -t 4 *.gff`
**Explanation:** `-t 4` uses 4 CPU threads. Roary's default is to use all cores, which doubles memory usage. For large inputs on a memory-constrained machine, reduce the thread count.

### Skip paralog splitting for a faster run
**Args:** `roary -f output_dir/ -e -n -s *.gff`
**Explanation:** `-s` (or `--skip_paralogs`) skips the paralog-handling step, treating each gene group as a single allele. Faster but less accurate for genomes with many paralogs.

### Use a custom group-size limit
**Args:** `roary -f output_dir/ -e -n --group_limit 100000 *.gff`
**Explanation:** `--group_limit 100000` increases the maximum number of gene groups from the default 60000 to 100000. For very large pangenomes (thousands of genomes), the default may be exceeded.

### Run a core-gene phylogeny from Roary output
**Args:** `FastTree -nt core_gene_alignment.aln > core_tree.nwk`
**Explanation:** Composite: after Roary runs, `core_gene_alignment.aln` is a concatenated alignment of all core genes. `FastTree -nt` builds a quick NJ tree. For ML, use `iqtree -s core_gene_alignment.aln -m GTR+G` for a more thorough analysis.
