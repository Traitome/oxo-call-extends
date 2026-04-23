---
name: biobb_cmip
category: utility
description: BioBB module for computing classical molecular interaction potentials
tags: [bioexcel, molecular-interaction, potential, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_cmip"
---

## Concepts
- **Tool Overview**: biobb_cmip wraps the CMIP tool for computing classical molecular interaction potentials on protein structures.
- **Molecular Interaction Potentials**: Computes electrostatic and van der Waals potentials around biomolecules.
- **Applications**: Binding site prediction, protein-ligand interaction analysis.

## Pitfalls
- **Input Requirements**: Requires properly formatted PDB structures.
- **Computational Cost**: High-resolution potential calculations can be time-consuming.

## Examples
### Compute electrostatic potential
**Args:** `biobb_cmip.cmip --input structure.pdb --output potential.dx`
**Explanation:** Computes molecular interaction potential around a protein structure.
