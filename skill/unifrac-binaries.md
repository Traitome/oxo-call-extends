---
name: unifrac-binaries
category: bioinformatics
description: UniFrac - Phylogenetic beta diversity tool.
tags: [unifrac-binaries, unifrac, phylogenetic-diversity, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/biocore/unifrac"
---

## Concepts

- **Tool Overview**: UniFrac - A tool for calculating phylogenetic beta diversity.
- **Core Function**: Computes UniFrac distances between microbial communities.
- **Input**: OTU table, phylogenetic tree.
- **Output**: Distance matrix.
- **Installation**: Install via conda or source
- **Use Case**: Microbiome analysis, community ecology, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Tree Requirements**: Requires rooted phylogenetic tree.

## Examples

### Compute UniFrac distance
**Args:** `unifrac -i otu_table.txt -t tree.nwk -o distances.txt`
**Explanation:** Compute UniFrac distances.

### Weighted UniFrac
**Args:** `unifrac -i otu_table.txt -t tree.nwk -o distances.txt -w`
**Explanation:** Compute weighted UniFrac.
