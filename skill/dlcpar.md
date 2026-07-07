---
name: dlcpar
category: population-genomics
description: DLCpar - Orthogroup and orthology inference tool.
tags: [dlcpar, population-genomics, orthologs, gene-tree, species-tree, reconciliation]
author: oxo-call-community
source_url: "https://github.com/dlcpar/dlcpar"
---

## Concepts

- **Tool Overview**: DLCpar is a tool for inferring orthogroups, orthologues, and gene/species trees.
- **Core Function**: Reconciles gene trees with species trees to infer orthology relationships using duplication-loss-coalescence model.
- **Input/Output**: Input: Gene trees and species tree (Newick). Output: Reconciled orthology relationships, orthogroups.
- **Algorithm**: Uses maximum parsimony or likelihood to reconcile gene trees with species tree.
- **Key Features**: Orthology inference, gene tree reconciliation, duplication-loss modeling, orthogroup assignment, visualization.
- **Installation**: `conda install -c bioconda dlcpar`

## Pitfalls

- **Input Requirements**: Requires gene trees and species tree in Newick format.
- **Tree Quality**: Poorly resolved trees affect orthology inference.
- **Model Selection**: Choosing appropriate reconciliation model is critical.
- **Computational Time**: May be slow for large datasets.
- **Gene Tree Error**: Gene tree estimation errors propagate to orthology calls.

## Examples

### Infer orthology relationships
**Args:** `dlcpar --genetree gene.nwk --speciestree species.nwk --output orthologs.tsv`
**Explanation:** Infers orthology relationships from gene and species trees.

### With multiple gene trees
**Args:** `dlcpar --genetrees trees/*.nwk --speciestree species.nwk --output orthologs.tsv`
**Explanation:** Process multiple gene trees simultaneously.

### Orthogroup assignment
**Args:** `dlcpar --genetrees trees/*.nwk --speciestree species.nwk --output orthogroups.tsv --orthogroups`
**Explanation:** Assign genes to orthogroups.

### Reconciliation only
**Args:** `dlcpar --genetree gene.nwk --speciestree species.nwk --output reconciliation.nwk --reconcile-only`
**Explanation:** Only perform tree reconciliation.

### Generate visualization
**Args:** `dlcpar --genetree gene.nwk --speciestree species.nwk --output plot.png --visualize`
**Explanation:** Generate visualization of reconciliation.