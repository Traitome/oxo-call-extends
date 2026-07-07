---
name: rnachipintegrator
category: epigenomics
description: integrate ChIP-seq peaks with gene annotations via peak-centric and gene-centric proximity analysis
tags: ["rnachipintegrator", "chip-seq", "epigenomics", "peak-annotation", "regulatory"]
author: oxo-call-community
source_url: "https://rnachipintegrator.readthedocs.io"
---

## Concepts

- **Tool Overview**: RnaChipIntegrator (v3.0.0) is a Python bioinformatics utility that performs integrated analyses of "gene" data (gene lists, expression tables, canonical gene sets) with "peak" data (ChIP-seq / ATAC-seq / CUT&RUN peaks) to identify the nearest genes/features to each peak and vice versa.
- **Core Function**: Two reciprocal analyses in one run: **peak-centric** (for each peak, list the nearest genes) and **gene-centric** (for each gene, list the nearest peaks). Both run by default and write to `<basename>_peak_centric.txt` and `<basename>_gene_centric.txt`.
- **Algorithm**: Computes the genomic distance between each peak and each gene under a user-chosen distance metric (`--edge`), filters pairs by `--cutoff` (default 1,000,000 bp; set to 0 for no limit), and reports the surviving pairs sorted by distance.
- **Input Format**: Two tab-delimited text files: a "genes" file (with at minimum chromosome, start, end, ID, strand) and a "peaks" file (chromosome, start, end; optional peak ID via `--peak_id`). Multiple genes/peak files can be supplied via repeated `--genes` / `--peaks` flags for batch mode.
- **Output Format**: Default is two TSVs (`*_peak_centric.txt`, `*_gene_centric.txt`) with one peak/gene pair per line, columns include peak coordinates, gene ID, strand, TSS, TES, distances (`dist_closest`, `dist_TSS`, `dist_TES`), direction (`U`/`D`/`.`), and overlap flags. Optional Excel (`--xlsx`), compact one-line-per-peak (`--compact`), summary (`--summary`), and per-output files in batch mode (`--split-outputs`).
- **Use Case**: Linking ChIP-seq/ATAC-seq peaks (e.g., H3K27ac, CTCF) to their putative target genes, building enhancer–promoter maps, prioritizing peaks near differentially expressed genes (`--only-DE`), and producing summary tables for a manuscript's supplementary data.

## Pitfalls

- **CRITICAL — Basename defaults to the input genes filename**: Without `--name`, the output prefix is derived from the genes file. If the path is something like `/data/genes/2025/my_genes.tsv`, the output goes to `my_genes_peak_centric.txt` in the current directory; always pass `--name` for clarity and to control output location.
- **CRITICAL — Default distance cutoff is 1 Mb, not "infinite"**: Gene/peak pairs more than 1,000,000 bp apart are dropped unless `--cutoff 0` is set. Many enhancer–promoter interactions span >1 Mb (e.g., in the MHC locus), so silent truncation is a common mistake — always check whether your biology requires `--cutoff 0`.
- **`--edge` choice changes the distance semantics**: `tss` (default) measures from the gene's TSS to the nearest peak edge (strand-aware), `tes` measures from the TES, `both` is strand-agnostic. Using `both` recovers intergenic peaks on the "wrong" strand but can over-report distal peaks that are actually close to a different gene.
- **Differential-expression flag in the genes file**: `--only-DE` looks for a DE column in the genes file (the column name is configurable, see docs). If the column is missing or named differently, `--only-DE` silently filters nothing — verify by checking the output row count.
- **`--promoter_region` only affects the `overlap_promoter` column**: Setting it does **not** restrict the analysis to promoters; it only changes whether a peak is flagged as overlapping the promoter region in the output. Use `--cutoff` for distance-based filtering.
- **Batch mode (`--peaks` repeated) requires consistent gene file**: When passing multiple peaks files via repeated `--peaks`, all peaks are matched against the same genes file. To switch genes per peak file, run RnaChipIntegrator in a loop with different `--genes` flags.

## Examples

### Basic integration
**Args:** `RnaChipIntegrator genes.tsv peaks.bed`
**Explanation:** Positional arguments: `genes.tsv` is the tab-delimited gene file and `peaks.bed` is the BED-like peak file; produces `genes_peak_centric.txt` and `genes_gene_centric.txt` with default 1 Mb cutoff and TSS-anchored distances.

### Restrict to peaks within 50 kb of a gene
**Args:** `RnaChipIntegrator --cutoff 50000 genes.tsv peaks.bed`
**Explanation:** `--cutoff 50000` limits reported pairs to those within 50,000 bp; useful for promoter-proximal analyses where distal enhancers are not of interest.

### Use strand-agnostic distance
**Args:** `RnaChipIntegrator --edge both genes.tsv peaks.bed`
**Explanation:** `--edge both` measures the shortest distance from any peak edge to the nearest of the gene's TSS/TES; effectively strand-agnostic and recovers peaks sitting between two convergently transcribed genes.

### Restrict to differentially expressed genes
**Args:** `RnaChipIntegrator --only-DE genes_with_de.tsv peaks.bed`
**Explanation:** `--only-DE` requires a DE-status column in the genes file (default column name is configurable); only DE genes are considered in the gene-centric output, and only peaks near DE genes appear in the peak-centric output.

### Cap the number of reported genes per peak
**Args:** `RnaChipIntegrator --number 3 genes.tsv peaks.bed`
**Explanation:** `--number 3` keeps only the 3 nearest genes per peak (peak-centric) and the 3 nearest peaks per gene (gene-centric); dramatically shrinks the output for genome-wide analyses.

### Custom output basename
**Args:** `RnaChipIntegrator --name h3k27ac_vs_de_genes genes.tsv peaks.bed`
**Explanation:** `--name h3k27ac_vs_de_genes` writes `h3k27ac_vs_de_genes_peak_centric.txt` and `h3k27ac_vs_de_genes_gene_centric.txt` in the current directory; essential when the input file path is long or shared across multiple runs.

### Multi-core batch mode
**Args:** `RnaChipIntegrator --nprocessors 8 --peaks peaks1.bed --peaks peaks2.bed --peaks peaks3.bed genes.tsv`
**Explanation:** `--peaks` can be repeated; `--nprocessors 8` runs the three peak files in parallel across 8 worker processes; output goes to a single combined file per analysis type unless `--split-outputs` is added.

### Write an Excel summary plus TSV
**Args:** `RnaChipIntegrator --xlsx --summary --name h3k4me3_run1 genes.tsv peaks.bed`
**Explanation:** `--xlsx` emits an Excel workbook with one sheet per analysis (handy for collaborators); `--summary` adds a high-level summary file with counts of total peaks/genes and within-cutoff pairs.

### Disable the distance cutoff entirely
**Args:** `RnaChipIntegrator --cutoff 0 genes.tsv peaks.bed`
**Explanation:** `--cutoff 0` removes the 1 Mb default; every peak/gene pair is reported, which on a whole-genome dataset can be hundreds of millions of rows — pipe the output to `awk` or `csvkit` to filter downstream.
