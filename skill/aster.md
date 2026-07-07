---
name: aster
category: population-genomics
description: ASTER - Accurate Species Tree Estimator for phylogenetic inference
tags: [aster, population-genomics, species-tree, phylogenetics, c++]
author: oxo-call-community
source_url: "https://github.com/chaoszhang/ASTER/blob/v1.23/README.md"
---

## Concepts

- **Tool Overview**: ASTER (Accurate Species Tree Estimator) is a family of optimization algorithms for species tree inference implemented in C++. Version 1.23.
- **Core Function**: Estimates species trees from multi-locus sequence data using various optimization algorithms.
- **Phylogenetic Inference**: Uses coalescent-based methods to infer species relationships from genomic data.
- **Multi-locus Analysis**: Handles multiple gene loci simultaneously for more accurate species tree estimation.
- **Optimization Algorithms**: Implements several optimization strategies including maximum likelihood and Bayesian methods.
- **Input/Output**: Accepts FASTA sequence files or gene trees, outputs inferred species trees in Newick format.
- **Installation**: `conda install -c bioconda aster` or compile from source.

## Pitfalls

- **Computational Complexity**: Species tree inference can be computationally intensive for large datasets.
- **Input Requirements**: Requires properly formatted sequence alignments or gene trees.
- **Model Selection**: Choosing appropriate evolutionary model affects inference accuracy.
- **Missing Data**: Incomplete data may affect tree inference quality.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Memory Usage**: Large datasets may require significant memory resources.

## Examples

### Display help
**Args:** `aster --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic species tree inference
**Args:** `aster -i alignments.fasta -o species_tree.newick`
**Explanation:** Infers species tree from multi-locus sequence alignments.

### Specify model
**Args:** `aster -i alignments.fasta -o species_tree.newick -m GTR+G`
**Explanation:** Uses GTR+G evolutionary model for inference.

### Set number of threads
**Args:** `aster -i alignments.fasta -o species_tree.newick -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Input gene trees
**Args:** `aster -i gene_trees.newick -o species_tree.newick --input-type trees`
**Explanation:** Infers species tree from pre-computed gene trees.

### Bootstrap analysis
**Args:** `aster -i alignments.fasta -o species_tree.newick -b 100`
**Explanation:** Performs 100 bootstrap replicates for assessing support.

### Output detailed statistics
**Args:** `aster -i alignments.fasta -o species_tree.newick -s stats.txt`
**Explanation:** Outputs inference statistics to separate file.

### Specify outgroup
**Args:** `aster -i alignments.fasta -o species_tree.newick -o outgroup_taxon`
**Explanation:** Roots tree using specified outgroup taxon.

### Use Bayesian inference
**Args:** `aster -i alignments.fasta -o species_tree.newick --method bayesian`
**Explanation:** Uses Bayesian method instead of maximum likelihood.

### Set convergence criteria
**Args:** `aster -i alignments.fasta -o species_tree.newick --convergence 0.01`
**Explanation:** Sets convergence threshold for Bayesian inference.