---
name: biobb_chemistry
category: utility
description: BioBB module for chemical conversions
tags: [bioexcel, chemistry, format-conversion, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_chemistry"
---

## Concepts
- **Tool Overview**: biobb_chemistry provides BioExcel Building Blocks for chemical format conversions and manipulations, wrapping tools like Babel for molecular file format interconversion.
- **Format Conversion**: Converts between chemical file formats (SDF, MOL2, PDB, SMILES, etc.).
- **Applications**: Drug design, ligand preparation, virtual screening preprocessing.

## Pitfalls
- **Format Limitations**: Some format conversions may lose information (e.g., 3D coordinates when converting SMILES to 2D).

## Examples
### Convert SDF to PDB
**Args:** `biobb_chemistry.acpype --input ligand.sdf --output ligand.pdb`
**Explanation:** Converts a ligand from SDF to PDB format.
