---
name: constava
category: formatting
description: Calculate conformational states probability from protein ensembles
tags: [constava, protein-structure, conformational-analysis, ensemble, pdb]
author: oxo-call-community
source_url: "https://pypi.org/project/constava/"
---

## Concepts

- **Tool Overview**: Constava calculates conformational states probability and variability from protein structure ensembles, analyzing the likelihood of residues adopting different conformational states.
- **Core Function**: Analyzes conformational ensembles to calculate conformational state propensities and variability for each residue in the protein structure.
- **Algorithm**: Uses statistical analysis of dihedral angles and structural parameters across ensemble members.
- **Input**: Protein structure ensemble files in PDB format.
- **Output**: Conformational state probabilities and variability scores per residue.
- **Application**: Protein dynamics analysis, NMR ensemble characterization, and conformational flexibility studies.
- **Installation**: Install via pip: `pip install constava`

## Pitfalls

- **Ensemble Size**: Requires sufficient ensemble members for statistical reliability.
- **Structure Quality**: Results depend on accurate structure determination.
- **Missing Residues**: Missing coordinates may affect calculations.
- **Conformational Sampling**: Limited sampling may miss rare conformations.
- **Threshold Selection**: State definition thresholds affect results.

## Examples

### Calculate conformational probabilities
**Args:** `constava -i ensemble.pdb -o probabilities.txt`
**Explanation:** Calculates conformational state probabilities from structure ensemble.

### With variability analysis
**Args:** `constava -i ensemble.pdb --variability -o variability_scores.txt`
**Explanation:** Calculates conformational variability per residue.

### With custom thresholds
**Args:** `constava -i ensemble.pdb -t 0.7 -o results.txt`
**Explanation:** Sets 70% threshold for conformational state assignment.

### Display help
**Args:** `constava --help`
**Explanation:** Shows all available options and usage information.