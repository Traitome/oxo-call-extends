---
name: fpocketr
category: utility
description: CLI tool to find, characterize, and visualize RNA-ligand binding pockets.
tags: [fpocketr, RNA, binding pockets, drug discovery]
author: oxo-call-community
source_url: "https://github.com/Weeks-UNC/fpocketR"
---

## Concepts
- **RNA Binding Pockets**: Identifies potential ligand binding sites in RNA structures.
- **fpocket Integration**: Wrapper around fpocket 4.0 for RNA-specific analysis.
- **Pocket Characterization**: Analyzes pocket properties (volume, hydrophobicity, druggability).
- **Visualization**: Generates visualizations of binding pockets.
- **Ligand Docking Support**: Prepares pockets for virtual screening.

## Pitfalls
- **Architecture Limitation**: Only available for x86_64 Linux and macOS.
- **Structure Quality**: Requires high-resolution RNA structures.
- **False Positives**: May identify non-functional pockets.
- **Computational Time**: Pocket detection can be time-consuming.
- **Output Interpretation**: Requires domain knowledge to interpret results.

## Examples
### Find binding pockets
**Args:** `fpocketr find -i rna.pdb -o pockets/`
**Explanation:** Identifies potential binding pockets in the RNA structure.

### Characterize pockets
**Args:** `fpocketr characterize -i pockets/ -o properties.txt`
**Explanation:** Analyzes and outputs pocket properties.

### Visualize pockets
**Args:** `fpocketr visualize -i rna.pdb -p pockets/ -o pocket_view.png`
**Explanation:** Generates visualization of identified binding pockets.

### Prepare for docking
**Args:** `fpocketr prepare -i pockets/ -o docking_input/`
**Explanation:** Prepares pockets for virtual ligand screening.

### Compare pockets
**Args:** `fpocketr compare -i pocket1/ pocket2/ -o comparison.txt`
**Explanation:** Compares properties of different binding pockets.