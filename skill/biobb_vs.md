---
name: biobb_vs
category: utility
description: BioBB module for virtual screening studies
tags: [bioexcel, virtual-screening, drug-discovery, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_vs"
---

## Concepts
- **Tool Overview**: biobb_vs provides BioExcel Building Blocks for virtual screening studies, including ligand preparation, docking, and scoring.
- **Virtual Screening Workflow**: Ligand library preparation, target preparation, molecular docking, and result ranking.
- **Applications**: Drug discovery, lead identification, binding site prediction.

## Pitfalls
- **Docking Engine**: Requires docking software (AutoDock Vina, etc.) installation.
- **Scoring Limitations**: Docking scores are approximations; experimental validation required.

## Examples
### Run virtual screening
**Args:** `biobb_vs.docking --target protein.pdb --ligands library.sdf --output results/`
**Explanation:** Performs virtual screening of ligand library against target protein.

### Prepare ligand
**Args:** `biobb_vs.ligand_prep --input ligand.sdf --output prepared.mol2`
**Explanation:** Prepares ligand for docking by adding hydrogens and optimizing geometry.
