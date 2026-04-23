---
name: dlcpar
category: population-genomics
description: Accurate inference of orthogroups, orthologues, gene trees and rooted species tree.
tags: [dlcpar, population-genomics, orthologs, gene-tree, species-tree]
author: oxo-call-community
source_url: "https://github.com/davidemms/OrthoFinder"
---

## Concepts

- **Tool Overview**: DLCpar v1.0 - Tool for inferring orthogroups, orthologues, and gene/species trees.
- **Core Function**: Reconciles gene trees with species trees to infer orthology relationships.
- **Input/Output**: Expects gene trees and species tree; outputs reconciled orthology relationships.
- **Installation**: `conda install -c bioconda dlcpar`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires gene trees and species tree in Newick format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dlcpar --genetree gene.nwk --speciestree species.nwk --output orthologs.tsv`
**Explanation:** Infers orthology relationships from gene and species trees.
