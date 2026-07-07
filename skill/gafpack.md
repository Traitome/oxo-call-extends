---
name: gafpack
category: alignment
description: Convert alignments to pangenome variation graphs to coverage maps.
tags: [gafpack, pangenome, variation graph, coverage map]
author: oxo-call-community
source_url: "https://github.com/pangenome/gafpack"
---

## Concepts
- **Pangenome Graphs**: Builds pangenome variation graphs.
- **GAF Format**: Processes Graph Alignment Format files.
- **Coverage Mapping**: Generates coverage maps from alignments.
- **Graph Construction**: Constructs variation graphs from alignments.
- **Visualization Support**: Supports graph visualization.

## Pitfalls
- **Graph Complexity**: Large graphs can be memory-intensive.
- **GAF Format**: Requires proper GAF format input.
- **Computational Time**: Building graphs is time-consuming.
- **Memory Usage**: High memory usage for large pangenomes.
- **Tool Compatibility**: Limited compatibility with other graph tools.

## Examples
### Build variation graph
**Args:** `gafpack build -i alignments.gaf -o graph.gfa`
**Explanation:** Builds variation graph from GAF alignments.

### Generate coverage map
**Args:** `gafpack coverage -i alignments.gaf -o coverage.txt`
**Explanation:** Generates coverage map from alignments.

### Extract subgraph
**Args:** `gafpack subgraph -i graph.gfa -r chr1:1000-2000 -o subgraph.gfa`
**Explanation:** Extracts subgraph for a genomic region.

### Export coverage
**Args:** `gafpack coverage -i alignments.gaf --bed -o coverage.bed`
**Explanation:** Exports coverage in BED format.

### Statistics
**Args:** `gafpack stats -i graph.gfa -o stats.txt`
**Explanation:** Generates statistics about the graph.