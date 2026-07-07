---
name: metagenomescope
category: assembly
description: Visualization tool for (meta)genome assembly graphs
tags: [metagenomescope, assembly, visualization, genome-graph]
author: oxo-call-community
source_url: "https://github.com/marbl/MetagenomeScope"
---

## Concepts

- **Tool Overview**: MetagenomeScope v1.2.0 is a visualization tool specifically designed for exploring and analyzing (meta)genome assembly graphs.
- **Core Function**: Provides interactive visualization of assembly graphs to help researchers understand genome structure and assembly complexity.
- **Graph Visualization**: Renders assembly graphs with nodes representing sequences and edges representing overlaps.
- **Interactive Exploration**: Supports zooming, panning, and highlighting of specific regions in the assembly graph.
- **Input/Output**: Accepts assembly graph files in GFA (Graphical Fragment Assembly) format; outputs visualizations and analysis reports.
- **Assembly Validation**: Helps identify assembly errors, complex regions, and potential misassemblies.

## Pitfalls

- **Graph Complexity**: Very large assembly graphs may be difficult to visualize effectively.
- **Memory Requirements**: Rendering large graphs may require significant memory resources.
- **File Format**: Requires specific input format (GFA) which may require conversion from other formats.
- **Visualization Clutter**: Dense graphs can become visually cluttered and difficult to interpret.
- **Computational Resources**: Layout algorithms may be computationally intensive for large graphs.
- **Interpretation**: Requires expertise to interpret assembly graph visualizations correctly.

## Examples

### Visualize assembly graph
**Args:** `metagenomescope -i assembly.gfa -o visualization.html`
**Explanation:** Generates an interactive HTML visualization of the assembly graph.

### With custom layout
**Args:** `metagenomescope -i assembly.gfa -o visualization.html -l force-directed`
**Explanation:** Uses force-directed layout algorithm for graph visualization.

### Highlight specific contigs
**Args:** `metagenomescope -i assembly.gfa -o visualization.html -h contig1,contig2`
**Explanation:** Highlights specified contigs in the visualization.

### Generate statistics
**Args:** `metagenomescope -i assembly.gfa -s stats.txt`
**Explanation:** Generates statistical analysis of the assembly graph.

### Export as image
**Args:** `metagenomescope -i assembly.gfa -o graph.png -f png`
**Explanation:** Exports the assembly graph as a PNG image.