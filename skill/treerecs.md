---
name: treerecs
category: analysis
description: TreeRecs - Tool for phylogenetic tree reconciliation.
tags: [treerecs, phylogenetic-tree, reconciliation, gene-tree, species-tree]
author: oxo-call-community
source_url: "https://github.com/compbio/treerecs"
---

## Concepts

- **Tool Overview**: TreeRecs - A tool for reconciling gene trees with species trees.
- **Core Function**: Infers gene duplication, loss, and transfer events by reconciling gene and species trees.
- **Input**: Gene trees, species tree, optional sequence data.
- **Output**: Reconciled trees, duplication/loss/transfer events, reconciliation scores.
- **Installation**: `pip install treerecs` or `conda install -c bioconda treerecs`
- **Use Case**: Phylogenomics, gene family evolution, comparative genomics.

## Pitfalls

- **Tree Quality**: Requires accurate gene and species trees.
- **Complexity**: May have difficulties with large gene families.

## Examples

### Reconcile trees
**Args:** `treerecs -g gene_trees.nwk -s species_tree.nwk -o reconciliation/`
**Explanation:** Reconcile gene trees with species tree.

### With sequences
**Args:** `treerecs -g genes.nwk -s species.nwk -a sequences.fasta -o results/`
**Explanation:** Reconcile trees with sequence data for improved accuracy.
