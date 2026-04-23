---
name: astral-tree
category: population-genomics
description: ASTRAL - Coalescent-based species tree estimation from gene trees under incomplete lineage sorting
tags: [species-tree, phylogenomics, coalescent, gene-trees, ils]
author: oxo-call-community
source_url: "https://github.com/smirarab/ASTRAL"
---

## Concepts

- **Tool Overview**: ASTRAL (Accurate Species TRee ALgorithm) estimates unrooted species trees from sets of unrooted gene trees. Statistically consistent under multi-species coalescent model. Version 5.7.8.
- **Incomplete Lineage Sorting**: Handles ILS by summarizing gene tree discordance. Does not assume gene trees match species tree.
- **Quartet-Based**: Finds species tree that maximizes number of shared induced quartet trees with gene trees. Quartet aggregation approach.
- **Statistical Consistency**: Proven consistent under multi-species coalescent. Accurate even with high ILS levels.
- **Scalability**: Handles thousands of genes and hundreds of species. Efficient for phylogenomic datasets.
- **Support Values**: Provides local posterior probabilities for branches. Indicates confidence in each clade.
- **Gene Tree Error**: Robust to moderate gene tree estimation error. More accurate than concatenation when gene trees have error.

## Pitfalls

- **Unrooted Trees**: Requires unrooted gene trees as input. Rooted trees will cause errors. Remove roots before running.
- **Gene Tree Quality**: Poor gene trees (low bootstrap, wrong models) reduce accuracy. Ensure gene trees are well-estimated.
- **Missing Data**: Genes missing from some taxa are handled, but excessive missing data reduces accuracy.
- **Branch Lengths**: ASTRAL ignores branch lengths in gene trees. Only topology matters.
- **Outgroup**: Does not root the tree. Root separately using outgroup or other methods.
- **Computational Limits**: Very large datasets (>1000 taxa, >10000 genes) may require substantial memory and time.

## Examples

### Basic ASTRAL run
**Args:** `java -jar astral.jar -i gene_trees.tre -o species_tree.tre`
**Explanation:** Standard ASTRAL analysis from file of gene trees in Newick format. Outputs species tree with branch support values.

### Run with bootstrapping
**Args:** `java -jar astral.jar -i gene_trees.tre -o species_tree_bs.tre -b 100`
**Explanation:** Performs 100 bootstrap replicates. Gene trees resampled with replacement. Outputs bootstrap support values on branches.

### Multi-threaded execution
**Args:** `java -jar astral.jar -i gene_trees.tre -o species_tree.tre -t 8`
**Explanation:** Uses 8 threads for parallel processing. Speeds up analysis for large datasets with many gene trees.

### Output branch lengths in coalescent units
**Args:** `java -jar astral.jar -i gene_trees.tre -o species_tree.tre -t 2`
**Explanation:** Outputs branch lengths in coalescent units (2*Ne generations). Useful for population genetics interpretation.

### Score existing tree
**Args:** `java -jar astral.jar -i gene_trees.tre -t species_tree.tre -o scored_tree.tre`
**Explanation:** Scores existing species tree against gene trees. Computes quartet score and support values. Useful for hypothesis testing.

### Handle polytomies in gene trees
**Args:** `java -jar astral.jar -i gene_trees.tre -o species_tree.tre -p 0.5`
**Explanation:** Handles gene trees with polytomies. Branches with support <50% collapsed to polytomies. Useful for low-support gene trees.

### Generate quartet scores
**Args:** `java -jar astral.jar -i gene_trees.tre -o species_tree.tre -q quartet_scores.txt`
**Explanation:** Outputs quartet scores for each gene. Useful for identifying outlier genes with discordant histories.

### Set memory limit
**Args:** `java -Xmx16G -jar astral.jar -i gene_trees.tre -o species_tree.tre`
**Explanation:** Allocates 16GB memory for ASTRAL. Required for large datasets. Adjust based on available RAM.