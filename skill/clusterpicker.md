---
name: clusterpicker
category: formatting
description: Identifies clusters in Newick-formatted phylogenetic trees with cluster matching capabilities
tags: [clusterpicker, phylogenetics, tree-analysis, clustering, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/emmahodcroft/cluster-picker-and-cluster-matcher"
---

## Concepts

- **Tool Overview**: ClusterPicker is a tool for identifying clusters in Newick-formatted phylogenetic trees, with additional cluster matching capabilities between different trees.
- **Core Function**: Identifies clusters in phylogenetic trees and provides tools for matching clusters across different tree analyses.
- **Algorithm**: Traverses trees to find clusters based on genetic distance and bootstrap support thresholds.
- **Input**: Newick-formatted phylogenetic trees.
- **Output**: Cluster assignments and cluster matching results.
- **Application**: Phylogenetic analysis, outbreak investigation, and tracking cluster relationships.
- **Installation**: Install via bioconda: `conda install -c bioconda clusterpicker`

## Pitfalls

- **Tree Format**: Requires properly formatted Newick trees.
- **Parameter Tuning**: May require adjustment of distance and bootstrap cut-offs.
- **Memory Usage**: May require significant memory for large trees.
- **Matching Accuracy**: Cluster matching depends on tree topology similarity.
- **Bootstrap Values**: Needs bootstrap support values for certain analyses.

## Examples

### Identify clusters
**Args:** `clusterpicker -i tree.nwk -o clusters.txt`
**Explanation:** Identifies clusters in phylogenetic tree.

### Match clusters between trees
**Args:** `clusterpicker match -i tree1.nwk tree2.nwk -o matches.txt`
**Explanation:** Matches clusters between two different phylogenetic trees.

### With custom thresholds
**Args:** `clusterpicker -i tree.nwk -d 0.03 -b 80 -o clusters.txt`
**Explanation:** Uses custom distance (0.03) and bootstrap (80%) thresholds.

### Display help
**Args:** `clusterpicker --help`
**Explanation:** Shows all available options and usage information.