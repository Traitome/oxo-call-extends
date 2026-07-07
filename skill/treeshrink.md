---
name: treeshrink
category: analysis
description: TreeShrink - Tool for detecting and removing outlier taxa from phylogenetic trees.
tags: [treeshrink, phylogenetic-tree, outlier-detection, tree-cleaning, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/uym2/treeshrink"
---

## Concepts

- **Tool Overview**: TreeShrink - A tool for detecting and removing outlier taxa from phylogenetic trees.
- **Core Function**: Identifies and removes outlier sequences that may distort phylogenetic analyses.
- **Input**: Phylogenetic tree (Newick format), optional alignment.
- **Output**: Cleaned tree, outlier list, statistics.
- **Installation**: `pip install treeshrink`
- **Use Case**: Phylogenetic analysis, tree cleaning, outlier detection.

## Pitfalls

- **Over-filtering**: May remove legitimate taxa if parameters are too strict.
- **Subjectivity**: Outlier detection may be subjective.

## Examples

### Detect outliers
**Args:** `treeshrink -i tree.nwk -o cleaned_tree.nwk`
**Explanation:** Detect and remove outlier taxa from tree.

### With alignment
**Args:** `treeshrink -i tree.nwk -a alignment.fasta -o result/`
**Explanation:** Use alignment for better outlier detection.
