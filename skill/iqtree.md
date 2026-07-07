---
name: iqtree
category: utility
description: Efficient phylogenomic software by maximum likelihood.
tags: [iqtree, utility, phylogeny, tree-inference, maximum-likelihood, phylogenomics]
author: oxo-call-community
source_url: "http://www.iqtree.org/doc"
---

## Concepts

- **Tool Overview**: IQ-TREE (v3.1.1+) is an efficient and versatile phylogenomic software for maximum likelihood tree inference. It supports multiple sequence alignment data and offers advanced features like model selection, bootstrap support, and partitioned analysis.
- **Core Function**: Performs phylogenetic tree reconstruction using maximum likelihood (ML) method with fast tree search algorithms and comprehensive model support.
- **Input/Output**: Input: FASTA/PHYLIP/NEXUS aligned sequences. Output: Newick tree files, log files with statistics, consensus trees, and bootstrap replicates.
- **Algorithm**: Uses a combination of hill-climbing, nearest neighbor interchange (NNI), and subtree pruning and regrafting (SPR) for tree search optimization.
- **Key Features**: Automatic model selection (ModelFinder), ultrafast bootstrap approximation (UFBoot), partitioned models, and support for morphological data.
- **Installation**: `conda install -c bioconda iqtree`

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory. Use `-mem` flag to limit memory usage if needed.
- **Model Selection**: Default model may not be optimal. Use `-m TEST` for ModelFinder automatic model selection.
- **Bootstrap Convergence**: Ensure sufficient bootstrap replicates for reliable support values. UFBoot typically requires fewer replicates than traditional bootstrapping.
- **Partitioned Analysis**: When using partitioned models, ensure the partition file format is correct and matches the alignment.
- **Ambiguous Characters**: IQ-TREE may treat ambiguous characters (N, ?, -) differently. Check the `-ambiguous` option for handling.

## Examples

### Display help and check installation
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic tree inference
**Args:** `-s alignment.fasta -m GTR+G -pre tree`
**Explanation:** Infers a ML tree from alignment.fasta using GTR+G model, outputs tree.treefile and tree.log.

### Automatic model selection with UFBoot
**Args:** `-s alignment.fasta -m TEST -bb 1000 -pre tree_auto`
**Explanation:** Uses ModelFinder to select best-fit model and runs 1000 UFBoot bootstrap replicates for branch support.

### Partitioned analysis
**Args:** `-s alignment.fasta -p partitions.txt -bb 1000 -pre tree_part`
**Explanation:** Runs partitioned analysis with models specified in partitions.txt file and 1000 UFBoot replicates.

### Bayesian-like approximation (BIONJ starting tree)
**Args:** `-s alignment.fasta -m GTR+I+G -init 0 -pre tree_bionj`
**Explanation:** Uses BIONJ as starting tree for better initial topology before ML optimization.

### Consensus tree from bootstrap replicates
**Args:** `-s alignment.fasta -m GTR+G -bb 1000 -consense majority -pre tree_consensus`
**Explanation:** Generates a majority-rule consensus tree from 1000 bootstrap replicates.

### Morphological data analysis
**Args:** `-s morphology.nex -m MK+G -pre morph_tree`
**Explanation:** Analyzes morphological data in NEXUS format using the MK model with gamma rate heterogeneity.