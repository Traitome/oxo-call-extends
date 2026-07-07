---
name: metatree
category: utility
description: Visualisation of polyphyletic groups between phylogenetic trees to a reference tree.
tags: [metatree, utility, phylogenetic-trees]
author: oxo-call-community
source_url: "https://github.com/aaronmussig/metatree"
---

## Concepts

- **Tool Overview**: MetaTree v0.0.1 is a tool for visualizing polyphyletic groups between phylogenetic trees and a reference tree.
- **Core Function**: Compares multiple phylogenetic trees against a reference tree to identify polyphyletic groups.
- **Tree Comparison**: Compares topological relationships across multiple phylogenetic trees.
- **Polyphyly Detection**: Identifies polyphyletic groups that are scattered across different parts of the tree.
- **Input/Output**: Accepts Newick-formatted trees; outputs visualizations and comparison reports.
- **Visualization**: Generates visual representations of tree comparisons.

## Pitfalls

- **Tree Format**: Requires proper Newick format for input trees.
- **Tree Quality**: Analysis quality depends on input tree quality.
- **Computational Resources**: Processing large trees may require significant computational resources.
- **Visualization Complexity**: Complex trees may produce cluttered visualizations.
- **Interpretation**: Requires expertise in phylogenetic analysis for proper interpretation.
- **Parameter Tuning**: May require parameter adjustment for optimal visualization.

## Examples

### Compare trees
**Args:** `metatree -r reference.tree -t trees/ -o comparison.pdf`
**Explanation:** Compares multiple trees against a reference tree.

### Highlight polyphyletic groups
**Args:** `metatree -r reference.tree -t trees/ -o comparison.pdf --highlight`
**Explanation:** Highlights polyphyletic groups in visualization.

### Generate report
**Args:** `metatree -r reference.tree -t trees/ -o report.txt --report`
**Explanation:** Generates a text report of tree comparisons.

### Custom color scheme
**Args:** `metatree -r reference.tree -t trees/ -o comparison.pdf --colors colors.txt`
**Explanation:** Uses custom color scheme for visualization.

### Batch processing
**Args:** `metatree -r reference.tree -t trees/ -o results/`
**Explanation:** Processes multiple tree files in batch mode.