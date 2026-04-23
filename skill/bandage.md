---
name: bandage
category: assembly
description: Bandage - Bioinformatics application for navigating de novo assembly graphs
tags: [assembly-graph, visualization, de-bruijn-graph, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/rrwick/Bandage"
---

## Concepts

- **Tool Overview**: Bandage is a GUI application for visualizing de novo assembly graphs, helping users understand assembly structure and quality.

- **Graph Visualization**: Renders assembly graphs (GFA format) showing contigs as nodes and overlaps as edges.

- **Quality Assessment**: Helps identify assembly issues like bubbles, tips, and chimeric connections.

- **Path Finding**: Supports finding paths through the graph corresponding to specific sequences or genes.

- **Interactive Exploration**: Allows interactive panning, zooming, and selection of graph elements.

## Pitfalls

- **Large Graphs**: Very large assembly graphs (>100,000 nodes) may be slow to render. Consider simplifying or filtering.

- **Memory Usage**: Large graphs require substantial memory. Monitor system resources.

- **GFA Format**: Requires GFA format input. Convert other formats if necessary.

## Examples

### Load and visualize assembly graph
**Args:** `Bandage load assembly.gfa`
**Explanation:** Opens assembly graph in Bandage GUI for interactive visualization.

### Find sequence in graph
**Args:** `Bandage load assembly.gfa --query gene.fasta`
**Explanation:** Loads assembly graph and highlights paths matching query sequence.

### Save graph image
**Args:** `Bandage image assembly.gfa graph.png --width 2000 --height 2000`
**Explanation:** Renders assembly graph to PNG image without opening GUI.

### Simplify graph
**Args:** `Bandage load assembly.gfa --minlength 1000`
**Explanation:** Filters graph to show only contigs ≥1000bp for cleaner visualization.
