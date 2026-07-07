---
name: figtree
category: visualization
description: "A graphical viewer for phylogenetic trees and a program for producing publication-ready figures, designed for BEAST-generated trees."
tags: [figtree, visualization, phylogeny, phylogenetic-tree, BEAST, Newick, Nexus, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rambaut/figtree"
---

## Concepts

- **Tool Overview**: FigTree is a graphical viewer for phylogenetic trees and a program for producing publication-ready figures. It is specifically designed for viewing summarized and annotated trees produced by BEAST.
- **Core Function**: Provides interactive visualization of phylogenetic trees with support for node labels, branch colors, tree layouts (rectangular, circular, radial), and export to multiple graphic formats.
- **Input/Output**: Input: Newick, Nexus, or other tree formats. Output: Interactive GUI display or exported graphics (PDF, SVG, PNG, PS, EMF, SWF).
- **Algorithm**: Java-based tree rendering using the JEBL (Java Evolutionary Biology Library) for tree manipulation and display.
- **Key Features**: Interactive GUI, multiple tree layouts, node annotation support, publication-ready exports, BEAST compatibility, cross-platform (Java).
- **Installation**: `conda install -c bioconda figtree` or download from http://tree.bio.ed.ac.uk/software/figtree/
- **Note**: FigTree has been superseded by [PearTree](http://github.com/artic-network/peartree) for many use cases.

## Pitfalls

- **Superseded Tool**: FigTree is no longer actively maintained. PearTree is recommended for new projects as it offers a more modern interface and webapp option.
- **Java Dependency**: Requires Java runtime environment (JRE). Ensure Java is installed before running.
- **Memory for Large Trees**: Large phylogenetic trees can consume significant memory. Use `-Xmx` flag to allocate more heap space (e.g., `java -Xmx4g -jar figtree.jar`).
- **Limited Automation**: Primarily a GUI tool with limited command-line options. For batch processing, consider using R packages (ggtree) or Python (ete3) instead.
- **File Format Compatibility**: While primarily designed for BEAST trees, it supports standard Newick and Nexus formats from other phylogenetic software.

## Examples

### Display a tree file
**Args:** `figtree tree_file.nex`
**Explanation:** Opens the phylogenetic tree file in the FigTree GUI for interactive viewing.

### Export as PDF
**Args:** `figtree -graphic PDF tree_file.tre output.pdf`
**Explanation:** Exports the tree directly to PDF format without opening the GUI, suitable for batch processing and publication figures.

### Export as PNG with dimensions
**Args:** `figtree -graphic PNG -width 800 -height 600 tree_file.tre output.png`
**Explanation:** Exports the tree as a PNG image with specified pixel dimensions (800x600).

### Get help
**Args:** `figtree -help`
**Explanation:** Displays the help message showing all available command-line options.

### Interactive viewing
**Args:** `figtree tree_file.newick`
**Explanation:** Opens the tree in GUI mode for interactive exploration, node selection, and layout adjustments.
