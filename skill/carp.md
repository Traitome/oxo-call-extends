---
name: carp
category: utility
description: Quantify rearrangement complexity of pangenomes and their graphs
tags: [carp, pangenome, rearrangement, complexity, graph]
author: oxo-call-community
source_url: "https://github.com/gi-bielefeld/scj-carp"
---

## Concepts

- **Tool Overview**: Carp quantifies rearrangement complexity of pangenomes using SCJ distance.
- **Core Function**: Computes rearrangement distances in pangenome graphs.
- **Algorithm**: Based on Single-Cut or Join (SCJ) rearrangement model.
- **Input**: Pangenome graph in GFA format.
- **Output**: Rearrangement complexity scores.
- **Application**: Pangenome analysis and comparison.
- **Installation**: Install via bioconda: `conda install -c bioconda carp`

## Pitfalls

- **SCJ Model**: Currently supports only SCJ rearrangement model.
- **Graph Format**: Requires GFA format input.
- **Scale**: Very large pangenomes may be slow.

## Examples

### Compute rearrangement complexity
**Args:** `carp -i pangenome.gfa -o complexity.tsv`
**Explanation:** Computes rearrangement complexity of pangenome graph.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
