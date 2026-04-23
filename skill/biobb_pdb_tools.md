---
name: biobb_pdb_tools
category: utility
description: BioBB swiss army knife for manipulating and editing PDB files
tags: [bioexcel, pdb, structure-editing, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_pdb_tools"
---

## Concepts
- **Tool Overview**: biobb_pdb_tools is a BioBB module wrapping pdb-tools, a swiss army knife for manipulating and editing PDB files.
- **PDB Manipulation**: Renumber residues, select chains, remove heteroatoms, fix formatting, and many other PDB operations.
- **Applications**: Structure preparation for MD simulations, PDB file cleaning, format standardization.

## Pitfalls
- **Format Compliance**: PDB format has strict column requirements; always validate after editing.

## Examples
### Select specific chain
**Args:** `biobb_pdb_tools.selchain --input structure.pdb --chain A --output chainA.pdb`
**Explanation:** Extracts chain A from a PDB structure.

### Remove water molecules
**Args:** `biobb_pdb_tools.rmhetero --input structure.pdb --output no_water.pdb`
**Explanation:** Removes water and other heteroatoms from PDB file.

### Renumber residues
**Args:** `biobb_pdb_tools.resser --input structure.pdb --output renumbered.pdb`
**Explanation:** Renumbers residues sequentially in PDB file.
