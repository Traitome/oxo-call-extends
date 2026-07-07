---
name: bte
category: programming
description: BioTreeEnv - Cython wrapper for the MAT library for phylogenetic tree operations
tags: [bte, biotreeenv, phylogenetics, python, tree]
author: oxo-call-community
source_url: "https://jmcbroome.github.io/BTE/build/html/index.html"
---

## Concepts

- **Tool Overview**: BTE (BioTreeEnv) is a Cython wrapper enabling use of the MAT (Maximum Agreement Subtree) library in Python for phylogenetic tree operations.
- **Core Function**: Provides efficient tree comparison and manipulation operations for phylogenetics.
- **Features**: Maximum agreement subtree computation, tree distance metrics, and tree manipulation.
- **Input**: Newick format phylogenetic trees.
- **Application**: Phylogenetic tree analysis and comparison in bioinformatics workflows.
- **Installation**: Install via bioconda: `conda install -c bioconda bte`

## Pitfalls

- **Python Library**: This is a Python library, not a command-line tool.
- **Tree Format**: Input trees must be in Newick format.
- **Version Compatibility**: Ensure compatibility with Python and Cython versions.

## Examples

### Import and use
**Args:** `from bte import Tree; t = Tree('((A,B),C)')`
**Explanation:** Creates a Tree object from Newick string.

### Compute agreement subtree
**Args:** `from bte import agreement_subtree; result = agreement_subtree(tree1, tree2)`
**Explanation:** Computes maximum agreement subtree between two trees.