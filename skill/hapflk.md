---
name: hapflk
category: bioinformatics
description: hapFLK detects selection signatures using FLK and hapFLK tests based on multi-population genotyping data.
tags: [hapflk, population-genomics, selection-signatures, bioinformatics]
author: oxo-call-community
source_url: "https://forge-dga.jouy.inra.fr/projects/hapflk"
---

## Concepts

- **Selection Detection**: hapFLK detects signatures of natural selection.

- **FLK Test**: Fisher's exact test for population differentiation.

- **hapFLK Test**: Haplotype-based FLK test for selection.

- **Multi-Population Analysis**: Analyzes genetic variation across multiple populations.

- **Population Genetics**: Studies population genetic structure.

- **Genome-Wide Scans**: Performs genome-wide selection scans.

## Pitfalls

- **Population Structure**: Account for population structure in analysis.

- **Sample Size**: Results depend on sample size per population.

- **Marker Density**: Requires sufficient marker density.

- **Linkage Disequilibrium**: LD may affect test statistics.

- **Multiple Testing**: Correct for multiple hypothesis testing.

## Examples

### Run hapFLK
**Args:** `hapflk --bfile input --pop populations.txt --out results`
**Explanation:** Runs hapFLK analysis on genotype data.

### FLK test only
**Args:** `hapflk --bfile input --pop populations.txt --flk --out flk_results`
**Explanation:** Performs FLK test only.

### With kinship matrix
**Args:** `hapflk --bfile input --pop populations.txt --kinship kinship.txt --out results`
**Explanation:** Uses kinship matrix for analysis.

### Permutation testing
**Args:** `hapflk --bfile input --pop populations.txt --perm 1000 --out results`
**Explanation:** Performs permutation testing for significance.

### Batch processing
**Args:** `for chr in {1..22}; do hapflk --bfile chr${chr} --pop populations.txt --out chr${chr}_results; done`
**Explanation:** Processes multiple chromosomes.

### Generate Manhattan plot
**Args:** `hapflk_plot.py -i results.flk -o manhattan.pdf`
**Explanation:** Generates Manhattan plot of results.

### Help command
**Args:** `hapflk --help`
**Explanation:** Shows available options and usage information.