---
name: biobb_structure_utils
category: utility
description: BioBB module to modify or extract information from PDB structure files
tags: [bioexcel, pdb, structure-utils, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_structure_utils"
---

## Concepts
- **Tool Overview**: biobb_structure_utils provides BioExcel Building Blocks for modifying or extracting information from PDB structure files.
- **Operations**: Extract models/chains, remove water/ligands, renumber atoms/residues, sort structures, merge structures.
- **Applications**: Structure preparation, PDB file manipulation, MD simulation setup.

## Pitfalls
- **Format Preservation**: Ensure PDB format compliance after modifications.

## Examples
### Extract chain from PDB
**Args:** `biobb_structure_utils.extract_chain --input structure.pdb --chain A --output chainA.pdb`
**Explanation:** Extracts chain A from a multi-chain PDB structure.

### Remove water molecules
**Args:** `biobb_structure_utils.remove_water --input structure.pdb --output no_water.pdb`
**Explanation:** Removes water molecules from PDB structure.

### Renumber residues
**Args:** `biobb_structure_utils.renumber --input structure.pdb --output renumbered.pdb`
**Explanation:** Renumbers residues sequentially in the PDB file.
