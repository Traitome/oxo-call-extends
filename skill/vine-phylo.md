---
name: vine-phylo
category: bioinformatics
description: vine-phylo - Phylogenetic analysis tool.
tags: [vine-phylo, phylogenetics, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/vine-phylo/"
---

## Concepts

- **Tool Overview**: vine-phylo - Phylogenetic tree construction.
- **Core Function**: Builds phylogenetic trees from sequence data.
- **Input**: Sequence alignment.
- **Output**: Phylogenetic tree.
- **Installation**: Install via pip or conda
- **Use Case**: Phylogenetics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Time**: May be slow for large datasets.

## Examples

### Build tree
**Args:** `vine-phylo -i alignment.fasta -o tree.nwk`
**Explanation:** Build phylogenetic tree.

### With options
**Args:** `vine-phylo -i alignment.fasta -o tree.nwk -m maximum-likelihood`
**Explanation:** Use maximum likelihood method.
