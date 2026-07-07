---
name: musicc
category: metagenomics
description: A marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome.
tags: [musicc, metagenomics, normalization, marker-genes, microbiome, abundance-profiling]
author: oxo-call-community
source_url: "http://elbo.gs.washington.edu/software_musicc.html"
---

## Concepts

- **Tool Overview**: MUSiCC v1.0.4 (Marker Genes-based Framework for Metagenomic Normalization and Profiling) is a method for normalizing metagenomic gene abundance data using sets of universal single-copy marker genes. It improves cross-sample comparability by accounting for biases in sequencing depth and gene copy number variations.
- **Core Function**: Takes gene abundance tables from metagenomic samples and returns normalized abundance profiles. The normalization uses the ratio of observed to expected marker gene abundances to correct systematic biases.
- **Algorithm**: Identifies universal single-copy marker genes present in nearly all organisms, then uses their collective abundance to estimate normalization factors. Genes are normalized by dividing by these factors.
- **Input Format**: Expects a tab-delimited gene abundance table with samples as columns and genes as rows. First column should be gene IDs, subsequent columns are sample abundances.
- **Output**: Produces a normalized abundance table in the same format as input. Also provides quality metrics including marker gene detection rates and normalization factors.
- **Use Case**: Particularly useful for comparing gene abundances across samples where technical variation (sequencing depth, copy number) would otherwise confound biological differences.

## Pitfalls

- **Gene Table Format**: Input must be properly formatted with consistent gene identifiers. Ensure no missing values or non-numeric entries.
- **Marker Gene Coverage**: MUSiCC requires sufficient marker gene representation. Samples with very low marker gene counts may produce unreliable normalizations.
- **Single-Copy Markers Assumption**: The method assumes most single-copy genes are truly single-copy. Horizontal gene transfer or gene duplications can violate this assumption.
- **Sample Comparability**: While normalization improves comparability, it cannot fully correct for extreme differences in community composition or sequencing technology.
- **Output Interpretation**: Normalized values represent relative abundances adjusted for biases. Absolute quantification requires additional calibration.
- **Biomarker Discovery**: MUSiCC-normalized data is suitable for differential abundance analysis, but statistical methods should account for the normalization step.

## Examples

### Basic normalization
**Args:** `-i gene_abundances.tsv -o normalized.tsv`
**Explanation:** Takes an input gene abundance table and outputs a normalized version. The normalization factors are derived from universal marker genes in the data.

### Verbose output with statistics
**Args:** `-i abundances.tsv -o normalized.tsv -v -s stats.txt`
**Explanation:** Runs with verbose output (-v) and saves statistics (-s) including marker gene counts, normalization factors, and quality metrics for each sample.

### Specify marker gene set
**Args:** `-i abundances.tsv -o normalized.tsv -m universal_markers.txt`
**Explanation:** Uses a custom marker gene set file instead of the default. Useful when working with specific taxonomic groups or custom marker databases.

### Filter low-abundance samples
**Args:** `-i abundances.tsv -o normalized.tsv --min-markers 10`
**Explanation:** Filters out samples with fewer than 10 marker genes detected. Samples failing this threshold are excluded from output.

### Parallel processing
**Args:** `-i abundances.tsv -o normalized.tsv -p 4`
**Explanation:** Uses 4 parallel threads for computation. Speeds up processing for large gene tables with many samples.
