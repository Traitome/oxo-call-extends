---
name: bacprune
category: population-genomics
description: BacPrune - Fast LD pruning of haploid genotype matrices for bacterial genomics
tags: [ld-pruning, linkage-disequilibrium, bacterial-genomics, variant-filtering]
author: oxo-call-community
source_url: "https://github.com/bacpop/BacPrune-Rust"
---

## Concepts

- **Tool Overview**: BacPrune performs fast linkage disequilibrium (LD) pruning on haploid genotype matrices, designed specifically for bacterial population genomics.

- **Three Pruning Modes**: Supports greedy pruning by r² (Pearson r-squared), |D'| threshold, and exact-duplicate removal via hashing.

- **Haploid Design**: Optimized for haploid bacterial genomes, unlike tools designed for diploid eukaryotes.

- **Hash-Based Dedup**: First removes exact duplicate variant columns via hashing before threshold-based pruning.

- **Output**: Produces pruned genotype matrix, pruning summary, and per-variant correlation-direction file.

## Pitfalls

- **Haploid Only**: Not suitable for diploid organisms. Use PLINK or similar for diploid LD pruning.

- **Threshold Selection**: LD threshold affects results significantly. Test multiple thresholds for optimal pruning.

- **Input Format**: Requires specific genotype matrix format. Ensure correct input formatting.

- **Missing Data**: Missing genotypes may affect LD calculations. Consider imputation or filtering first.

## Examples

### Prune by r² threshold
**Args:** `bacprune --r --threshold 0.8 --input genotypes.tsv --output pruned.tsv`
**Explanation:** Prunes variants with r² > 0.8 using greedy algorithm, keeping representative variants.

### Prune by D' threshold
**Args:** `bacprune --dprime --threshold 0.9 --input genotypes.tsv --output pruned.tsv`
**Explanation:** Prunes variants with |D'| > 0.9, an alternative LD measure.

### Exact duplicate removal only
**Args:** `bacprune --dedup --input genotypes.tsv --output deduped.tsv`
**Explanation:** Removes only exact duplicate variant columns, no LD-based pruning.

### With summary output
**Args:** `bacprune --r --threshold 0.8 --input genotypes.tsv --output pruned.tsv --summary summary.txt`
**Explanation:** Produces pruning summary with statistics about removed variants.

### Specify correlation direction file
**Args:** `bacprune --r --threshold 0.8 --input genotypes.tsv --output pruned.tsv --directions directions.tsv`
**Explanation:** Outputs per-variant correlation direction file for downstream analysis.
