---
name: strangepg
category: visualization
description: Strange pangenome-scale interactive graph visualizer.
tags: [strangepg, pangenome, visualization, graph]
author: oxo-call-community
source_url: "https://github.com/qwx9/strangepg"
---

## Concepts

- **Tool Overview**: strangepg (v0.9.4) is an interactive visualization tool for exploring pangenome graphs.
- **Core Function**: Visualizes large-scale pangenome graphs for comparative genomic analysis.
- **Algorithm**: Uses graph rendering and interactive navigation for pangenome exploration.
- **Input/Output**: Input: Pangenome graph (GFA format); Output: Interactive visualization.
- **Applications**: Pangenome analysis, comparative genomics, evolutionary studies.
- **Installation**: `conda install -c bioconda strangepg` or download from GitHub.

## Pitfalls

- **Graph Complexity**: Very large pangenome graphs are hard to visualize.
- **Memory Requirements**: Large graphs require significant memory.
- **Rendering Time**: Complex graphs may take time to render.
- **Input Format**: Requires specific graph format (GFA).
- **Interactive Performance**: May be slow with very large datasets.
- **Export Limitations**: Export options may be limited for complex visualizations.

## Examples

### Display help
**Args:** `strangepg --help`
**Explanation:** Shows available options and usage information.

### Basic visualization
**Args:** `strangepg -i pangenome.gfa`
**Explanation:** Open interactive visualization of pangenome graph.

### Export image
**Args:** `strangepg -i pangenome.gfa -o visualization.png`
**Explanation:** Export visualization as image file.

### Verbose mode
**Args:** `strangepg -i pangenome.gfa -v`
**Explanation:** Run with detailed logging for debugging.

### Custom layout
**Args:** `strangepg -i pangenome.gfa -l circular`
**Explanation:** Use circular layout for visualization.

### Filter by length
**Args:** `strangepg -i pangenome.gfa -m 1000`
**Explanation:** Filter nodes shorter than 1000 bp.

### Highlight regions
**Args:** `strangepg -i pangenome.gfa -h region.bed`
**Explanation:** Highlight specific genomic regions.

### Batch visualization
**Args:** `strangepg -i graphs/ -o images/`
**Explanation:** Export multiple graphs as images.

### Generate report
**Args:** `strangepg -i pangenome.gfa --report`
**Explanation:** Generate comprehensive HTML report with visualization.
