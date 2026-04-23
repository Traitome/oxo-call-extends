---
name: biobb_pmx
category: utility
description: BioBB module for PMX executions for alchemical free energy calculations
tags: [bioexcel, pmx, free-energy, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_pmx"
---

## Concepts
- **Tool Overview**: biobb_pmx wraps PMX for automated setup of alchemical free energy calculations, particularly for protein mutations.
- **Alchemical Transformations**: Generates hybrid topologies for free energy perturbation calculations.
- **Applications**: Protein stability prediction, ligand binding affinity changes, mutation effect analysis.

## Pitfalls
- **PMX Dependency**: Requires PMX installation separately.
- **Force Field Compatibility**: Must use compatible force fields for alchemical calculations.

## Examples
### Generate hybrid topology
**Args:** `biobb_pmx.mutate --input protein.pdb --mutation A:ALA:VAL:50 --output hybrid.top`
**Explanation:** Generates hybrid topology for alchemical mutation calculation.
