---
name: scripps-msms
category: structural-biology
description: Scripps MSMS - Fast algorithm for computing molecular surfaces
tags: ["scripps-msms", "structural-biology", "molecular-surface", "protein-structure"]
author: oxo-call-community
source_url: "https://ccsb.scripps.edu/msms/documentation/"
---

## Concepts

- **Tool Overview**: Scripps MSMS (v2.6.1) is a fast algorithm for computing molecular surfaces.
- **Core Function**: Computes solvent-accessible and molecular surfaces from PDB files.
- **Algorithm**: Uses triangulation for efficient surface calculation.
- **Input/Output**: Accepts PDB files and produces surface representations.
- **Surface Calculation**: Computes various surface properties including area and volume.
- **Applications**: Structural biology, protein analysis, and drug design.

## Pitfalls

- **Memory Usage**: High memory requirements for large molecules.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Format**: Requires properly formatted PDB files.
- **Surface Quality**: Results depend on input structure quality.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Basic surface calculation
**Args:** `msms -if protein.pdb -of surface`
**Explanation:** `-if` input PDB; `-of` output prefix.

### With probe radius
**Args:** `msms -if protein.pdb -of surface -probe_radius 1.4`
**Explanation:** `-probe_radius` sets probe radius for surface calculation.

### Output format
**Args:** `msms -if protein.pdb -of surface -af surface.area`
**Explanation:** `-af` specifies area file output.

### Verbose logging
**Args:** `msms -if protein.pdb -of surface -v`
**Explanation:** `-v` enables verbose output.

### Multiple chains
**Args:** `msms -if protein.pdb -of surface -all`
**Explanation:** `-all` processes all chains in PDB.

### Surface area calculation
**Args:** `msms -if protein.pdb -of surface -show_area`
**Explanation:** `-show_area` prints surface area statistics.

### Volume calculation
**Args:** `msms -if protein.pdb -of surface -volume`
**Explanation:** `-volume` computes and outputs molecular volume.