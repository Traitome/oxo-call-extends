---
name: rtk
category: statistics
description: rtk - rarefaction toolkit for OTU tables.
tags: ["rtk", "rarefaction", "OTU", "microbiome", "diversity"]
author: oxo-call-community
source_url: "https://github.com/hildebra/Rarefaction"
---

## Concepts

- **Tool Overview**: rtk (v0.93.2) is a command-line rarefaction toolkit specifically designed for OTU (Operational Taxonomic Unit) table analysis in microbiome research. It provides tools for subsampling, diversity estimation, and rarefaction curve generation.
- **Core Function**: Performs rarefaction (random subsampling without replacement) to normalize sequencing depth across samples, enabling fair comparison of alpha diversity metrics.
- **Algorithm**: Implements repeated random subsampling to generate rarefaction curves, supporting multiple diversity indices including Shannon, Simpson, Chao1, and ACE.
- **Input Format**: BIOM format OTU tables, tab-separated count matrices, or QIIME legacy formats.
- **Output Format**: Rarefaction curves in PDF/PNG format, diversity metrics in TSV format, resampled OTU tables.
- **Use Case**: Microbiome diversity analysis, normalization of sequencing depth, quality control of sequencing data, generating publication-quality rarefaction curves.

## Pitfalls

- **Sample size reduction**: Rarefaction reduces sample size, potentially losing statistical power for small samples.
- **Random variability**: Results vary between runs due to random subsampling; use fixed seed for reproducibility.
- **Input format sensitivity**: Strict format requirements; ensure OTU tables are properly formatted.
- **Computational intensity**: Many iterations can be slow for large OTU tables with many samples.
- **Depth selection**: Choosing inappropriate rarefaction depth can mask true diversity patterns.
- **Singleton loss**: Rarefaction may remove rare taxa, affecting diversity estimates.

## Examples

### Generate rarefaction curve
**Args:** `rtk rarefy -i otu_table.biom -o rarefaction.pdf`
**Explanation:** `-i` input OTU table in BIOM format; `-o` output PDF with rarefaction curve.

### Specify subsampling depth
**Args:** `rtk rarefy -i otu_table.biom -d 5000 -o rarefaction.pdf`
**Explanation:** `-d` subsample depth. Rarefies all samples to 5,000 reads per sample.

### Compute alpha diversity
**Args:** `rtk diversity -i otu_table.biom -o diversity.tsv -m shannon,simpson,chao1`
**Explanation:** `-m` diversity metrics to compute. Outputs TSV with diversity indices for each sample.

### Resample OTU table
**Args:** `rtk resample -i otu_table.biom -d 10000 -o resampled.biom`
**Explanation:** Generates a new OTU table with all samples rarefied to specified depth.

### Multiple iterations
**Args:** `rtk rarefy -i otu_table.biom -n 50 -o rarefaction.pdf`
**Explanation:** `-n` number of iterations. Computes mean and standard deviation across 50 subsampling runs.

### Set random seed
**Args:** `rtk rarefy -i otu_table.biom -s 12345 -o rarefaction.pdf`
**Explanation:** `-s` random seed for reproducible results.

### Compare diversity between groups
**Args:** `rtk compare -i otu_table.biom -g groups.txt -o comparison.tsv`
**Explanation:** `-g` group assignment file. Compares diversity metrics between sample groups.
