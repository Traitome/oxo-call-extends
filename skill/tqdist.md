---
name: tqdist
category: analysis
description: TQDist - Tool for calculating tree quality distance metrics.
tags: [tqdist, phylogenetic-tree, distance-metric, tree-comparison, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/compbio/tqdist"
---

## Concepts

- **Tool Overview**: TQDist - A tool for calculating quality metrics and distances between phylogenetic trees.
- **Core Function**: Computes tree quality scores and compares tree topologies.
- **Input**: Phylogenetic trees (Newick format), tree collections.
- **Output**: Tree quality metrics, distance matrices, comparison statistics.
- **Installation**: `pip install tqdist` or `conda install -c bioconda tqdist`
- **Use Case**: Phylogenetic tree comparison, tree quality assessment, evolutionary analysis.

## Pitfalls

- **Tree Format**: Requires standard Newick format for input trees.
- **Scale**: Large tree collections may require significant computational resources.

## Examples

### Compare trees
**Args:** `tqdist -t1 tree1.nwk -t2 tree2.nwk -o comparison.txt`
**Explanation:** Compare two phylogenetic trees and calculate distance metrics.

### Quality assessment
**Args:** `tqdist -i trees.nwk -o quality_scores/`
**Explanation:** Assess quality of multiple phylogenetic trees.
