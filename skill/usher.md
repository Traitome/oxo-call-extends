---
name: usher
category: bioinformatics
description: UShER - Ultrafast Sample placement on Existing tRees.
tags: [usher, phylogenetic-tree, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/yatisht/usher"
---

## Concepts

- **Tool Overview**: UShER - A tool for rapid placement of samples on phylogenetic trees.
- **Core Function**: Places new sequences onto existing phylogenetic trees.
- **Input**: Reference tree, sequence variants.
- **Output**: Updated phylogenetic tree.
- **Installation**: Install via conda or source
- **Use Case**: Phylogenetics, viral evolution, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large trees.
- **Tree Format**: Requires specific tree format.

## Examples

### Place samples
**Args:** `usher -t tree.nwk -v variants.vcf -o updated_tree.nwk`
**Explanation:** Place variants onto tree.

### With options
**Args:** `usher -t tree.nwk -v variants.vcf -o updated_tree.nwk -m 10`
**Explanation:** Set maximum placements.
