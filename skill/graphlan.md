---
name: graphlan
category: bioinformatics
description: GraPhlAn produces high-quality circular representations of taxonomic and phylogenetic trees for visualizing microbial community structures.
tags: [graphlan, phylogenetics, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/biobakery/graphlan"
---

## Concepts

- **Circular Phylogenetic Trees**: GraPhlAn specializes in generating circular tree visualizations, ideal for displaying taxonomic relationships.

- **Taxonomic Visualization**: Visualizes hierarchical relationships in microbial communities and phylogenetic data.

- **Annotation Integration**: Integrates taxonomic annotations and metadata into tree visualizations.

- **Color Coding**: Supports color coding of branches and nodes based on taxonomic classification or abundance.

- **Layout Customization**: Offers extensive customization options for tree layout, colors, and annotations.

- **Publication-Quality Output**: Generates high-resolution images suitable for scientific publications.

## Pitfalls

- **Tree Complexity**: Very large trees may produce cluttered visualizations. Consider simplifying or focusing on specific clades.

- **Memory Usage**: Processing large phylogenetic trees may require significant memory.

- **Input Format**: Ensure input trees are in Newick format. Other formats may need conversion.

- **Annotation Format**: Metadata files must be correctly formatted. Mismatched identifiers will cause errors.

- **Visualization Interpretation**: Circular layouts can be difficult to interpret for complex trees.

## Examples

### Generate basic circular tree
**Args:** `graphlan_annotate.py -t tree.nwk -o annotated.tree`
**Explanation:** Annotates a phylogenetic tree for visualization.

### Create visualization
**Args:** `graphlan.py annotated.tree output.png`
**Explanation:** Generates a circular tree visualization from an annotated tree.

### Add color annotations
**Args:** `graphlan_annotate.py -t tree.nwk -a annotations.txt -o annotated.tree`
**Explanation:** Adds color annotations from a metadata file.

### Customize tree appearance
**Args:** `graphlan.py annotated.tree output.png --size 10 --dpi 300`
**Explanation:** Generates a 10-inch tree at 300 DPI resolution.

### Specify branch colors
**Args:** `graphlan_annotate.py -t tree.nwk -b branch_colors.txt -o annotated.tree`
**Explanation:** Specifies custom branch colors for visualization.

### Generate PDF output
**Args:** `graphlan.py annotated.tree output.pdf --format pdf`
**Explanation:** Generates a PDF version of the tree visualization.

### Batch processing
**Args:** `for tree in *.nwk; do graphlan_annotate.py -t $tree -o ${tree%.nwk}_annotated.tree; done`
**Explanation:** Processes multiple tree files in a directory.