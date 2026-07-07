---
name: tcolor
category: visualization
description: Tree visualization tool for coloring and annotating phylogenetic trees.
tags: [tcolor, visualization, phylogenetics, tree-coloring, annotation]
author: oxo-call-community
source_url: "https://github.com/dskrypel/tcolor"
---

## Concepts

- **Tool Overview**: tcolor - A phylogenetic tree visualization tool for adding colors, annotations, and visual enhancements to Newick-format phylogenetic trees.
- **Core Function**: Reads Newick tree files and adds color-coded branches, labels, or annotations based on taxonomic groups, metadata, or custom criteria.
- **Input**: Newick format tree files (.nwk, .tree) with optional metadata files for annotation.
- **Output**: SVG, PNG, or PDF formatted tree images with color annotations.
- **Installation**: `pip install tcolor` or `conda install -c bioconda tcolor`
- **Use Case**: Creating publication-quality phylogenetic tree visualizations with taxonomic or metadata-based coloring.

## Pitfalls

- **Newick Format Only**: tcolor works specifically with Newick format trees - convert other formats first.
- **Metadata Matching**: Color assignments require exact matching of taxon names between tree and metadata files.
- **Output Size**: High-resolution output can produce large files, especially for trees with many taxa.
- **Limited Documentation**: Less widely used tool with limited online documentation and examples.
- **Dependencies**: May require specific graphics libraries for certain output formats.

## Examples

### Basic tree coloring
**Args:** `tcolor tree.nwk -o colored_tree.png`
**Explanation:** Basic tree visualization with default coloring scheme applied to branches.

### Color by taxonomic group
**Args:** `tcolor tree.nwk -c taxonomy.txt -o colored_tree.png`
**Explanation:** Color branches based on taxonomic group assignments provided in taxonomy file.

### SVG output
**Args:** `tcolor tree.nwk -o tree.svg -f svg`
**Explanation:** Export tree as SVG vector format for scalable publication figures.

### With leaf labels
**Args:** `tcolor tree.nwk -l -o labeled_tree.png`
**Explanation:** Include leaf labels on the tree visualization in addition to colored branches.
