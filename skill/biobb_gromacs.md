---
name: biobb_gromacs
category: utility
description: BioBB module for molecular dynamics simulations using GROMACS
tags: [bioexcel, gromacs, molecular-dynamics, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_gromacs"
---

## Concepts
- **Tool Overview**: biobb_gromacs wraps the GROMACS molecular dynamics suite for BioBB workflows. It provides Python interfaces for all major GROMACS operations.
- **MD Workflow**: Structure preparation, topology generation, energy minimization, equilibration, production MD, and analysis.
- **Applications**: Protein simulations, membrane systems, free energy calculations, biomolecular modeling.

## Pitfalls
- **GROMACS Dependency**: Requires GROMACS installation separately.
- **Force Field Selection**: Appropriate force field selection is critical for accurate results.

## Examples
### Generate topology
**Args:** `biobb_gromacs.pdb2gmx --input protein.pdb --output processed.gro --forcefield amber99sb-ildn`
**Explanation:** Generates GROMACS topology from PDB structure.

### Run energy minimization
**Args:** `biobb_gromacs.grompp --input em.mdp --output em.tpr && biobb_gromacs.mdrun --input em.tpr --output em.trr`
**Explanation:** Prepares and runs energy minimization.

### Run production MD
**Args:** `biobb_gromacs.mdrun --input md.tpr --output trajectory.xtc`
**Explanation:** Runs production molecular dynamics simulation.
