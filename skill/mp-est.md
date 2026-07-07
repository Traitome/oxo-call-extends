---
name: mp-est
category: utility
description: Maximum Pseudo-likelihood Estimation of Species Trees.
tags: [mp-est, utility, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/lliu1871/mp-est"
---

## Concepts

- **Tool Overview**: MP-EST v3.1.0 estimates species trees using pseudo-likelihood.
- **Core Function**: Reconstructs species trees from gene trees.
- **Pseudo-likelihood**: Uses maximum pseudo-likelihood estimation.
- **Multi-locus Analysis**: Integrates information from multiple loci.
- **Species Tree Inference**: Specialized for species tree reconstruction.
- **Input/Output**: Accepts gene trees; outputs species tree.

## Pitfalls

- **Phylogenetics Specific**: Designed for species tree inference.
- **Memory Requirements**: Memory usage depends on gene tree count.
- **Parameter Tuning**: May require parameter adjustment for estimation.
- **Data Quality**: Results depend on gene tree quality.
- **Computational Resources**: Large datasets may require significant resources.
- **Gene Tree Dependence**: Requires input gene trees.

## Examples

### Estimate species tree
**Args:** `mp-est -i gene_trees.newick -o species_tree.newick`
**Explanation:** Estimates species tree from gene trees.

### With bootstrap
**Args:** `mp-est -i gene_trees.newick -b 100 -o species_tree.newick`
**Explanation:** Performs 100 bootstrap replicates.

### With multiple threads
**Args:** `mp-est -i gene_trees.newick -t 4 -o species_tree.newick`
**Explanation:** Uses 4 threads for parallel computation.

### Verbose output
**Args:** `mp-est -i gene_trees.newick -v -o species_tree.newick`
**Explanation:** Shows detailed estimation progress.

### Batch processing
**Args:** `mp-est -i trees/ -o results/`
**Explanation:** Processes multiple gene tree files.