---
name: bandage_ng
category: assembly
description: BandageNG - Next generation Bioinformatics Application for Navigating De novo Assembly Graphs
tags: [bandage_ng, assembly-graph, visualization, de-bruijn-graph, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/asl/BandageNG/blob/v2026.4.1/README.md"
---

## Concepts

- **Tool Overview**: BandageNG (v2026.4.1) is the next generation of Bandage, a bioinformatics application for visualizing and navigating de novo assembly graphs.
- **Core Function**: Visualizes de novo assembly graphs to help understand assembly structure and quality.
- **Graph Visualization**: Renders assembly graphs (GFA, FASTA, SAM/BAM formats) showing contigs as nodes and overlaps as edges.
- **Quality Assessment**: Helps identify assembly issues like bubbles, tips, and chimeric connections.
- **Path Finding**: Supports finding paths through the graph corresponding to specific sequences or genes.
- **Interactive Exploration**: Allows interactive panning, zooming, and selection of graph elements.
- **Input/Output**: Accepts GFA, FASTA, SAM/BAM files; outputs visualizations and analysis reports.
- **Installation**: `conda install -c bioconda bandage_ng`.

## Pitfalls

- **Large Graphs**: Very large assembly graphs (>100,000 nodes) may be slow to render. Consider simplifying or filtering.
- **Memory Usage**: Large graphs require substantial memory. Monitor system resources.
- **Format Compatibility**: Ensure input files are in supported formats (GFA, FASTA, SAM/BAM).
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Load and visualize assembly graph
**Args:** `bandage_ng load assembly.gfa`
**Explanation:** Opens assembly graph in BandageNG GUI for interactive visualization.

### Find sequence in graph
**Args:** `bandage_ng load assembly.gfa --query gene.fasta`
**Explanation:** Loads assembly graph and highlights paths matching query sequence.

### Save graph image
**Args:** `bandage_ng image assembly.gfa graph.png --width 2000 --height 2000`
**Explanation:** Renders assembly graph to PNG image without opening GUI.

### Simplify graph
**Args:** `bandage_ng load assembly.gfa --minlength 1000`
**Explanation:** Filters graph to show only contigs ≥1000bp for cleaner visualization.

### Export graph statistics
**Args:** `bandage_ng stats assembly.gfa -o stats.txt`
**Explanation:** Generates statistics about the assembly graph structure.

### Batch mode processing
**Args:** `bandage_ng batch -i graphs.txt -o results/`
**Explanation:** Processes multiple assembly graphs in batch mode.

### Display help
**Args:** `bandage_ng --help`
**Explanation:** Shows all available command-line options and usage information.