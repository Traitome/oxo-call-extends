---
name: biobb_dna
category: utility
description: BioBB module for nucleic acid trajectory analysis
tags: [bioexcel, dna, rna, nucleic-acid, trajectory-analysis]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_dna"
---

## Concepts
- **Tool Overview**: biobb_dna provides BioExcel Building Blocks for analyzing nucleic acid (DNA/RNA) trajectories from molecular dynamics simulations.
- **Analysis Types**: Helical parameters, backbone torsions, groove dimensions, base pair step parameters.
- **Applications**: DNA/RNA flexibility analysis, drug-DNA interaction studies, nucleic acid structure characterization.

## Pitfalls
- **Trajectory Requirements**: Requires nucleic acid-containing MD trajectories.
- **Parameter Definitions**: Helical parameter definitions follow Curves+ conventions.

## Examples
### Compute helical parameters
**Args:** `biobb_dna.helical_parameters --input trajectory.xtc --topology topol.tpr --output helical_params.csv`
**Explanation:** Computes DNA helical parameters from MD trajectory.
