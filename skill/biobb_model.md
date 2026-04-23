---
name: biobb_model
category: utility
description: BioBB module to check and model 3D structures, create mutations, reconstruct missing atoms
tags: [bioexcel, structure-modeling, mutation, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_model"
---

## Concepts
- **Tool Overview**: biobb_model provides BioExcel Building Blocks for checking and modeling 3D structures, creating mutations, and reconstructing missing atoms.
- **Structure Checking**: Validates PDB structure quality, identifies missing atoms, and checks for structural issues.
- **Modeling**: Reconstructs missing atoms, adds hydrogens, and fixes structural problems.
- **Mutations**: Introduces point mutations in protein structures.

## Pitfalls
- **Structure Quality**: Input structure quality affects modeling results.
- **Side Chain Conformations**: Mutated side chains may require optimization.

## Examples
### Check structure quality
**Args:** `biobb_model.check --input structure.pdb --output report.json`
**Explanation:** Checks PDB structure for issues and missing atoms.

### Create mutation
**Args:** `biobb_model.mutate --input structure.pdb --mutation A:ALA:VAL:50 --output mutated.pdb`
**Explanation:** Introduces a point mutation at position 50 in chain A.
