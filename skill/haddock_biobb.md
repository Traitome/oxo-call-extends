---
name: haddock_biobb
category: bioinformatics
description: HADDOCK3 is an integrative modelling software for biomolecular structure prediction and refinement.
tags: [haddock_biobb, protein-structure, molecular-modelling, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/haddocking/haddock3"
---

## Concepts

- **Integrative Modelling**: HADDOCK3 integrates experimental data into structure prediction.

- **Protein-Protein Docking**: Predicts protein-protein complex structures.

- **Structure Refinement**: Refines existing molecular structures.

- **Experimental Data Integration**: Incorporates NMR, X-ray, and EM data.

- **Scoring Functions**: Uses energy-based scoring for model evaluation.

- **Ensemble Generation**: Generates multiple structural models.

## Pitfalls

- **Computational Resources**: Requires significant computational resources.

- **Input Quality**: Results depend on input data quality.

- **Parameter Tuning**: May require extensive parameter optimization.

- **Model Interpretation**: Carefully interpret generated models.

- **Time Consuming**: Complex simulations may take hours to days.

## Examples

### Run HADDOCK3
**Args:** `haddock3 config.cfg`
**Explanation:** Runs HADDOCK3 with configuration file.

### Create configuration
**Args:** `haddock3-config -o config.cfg`
**Explanation:** Generates default configuration file.

### Protein-protein docking
**Args:** `haddock3 --mode protein-protein -r receptor.pdb -l ligand.pdb -o results`
**Explanation:** Performs protein-protein docking.

### Refine structure
**Args:** `haddock3 --mode refine -i model.pdb -o refined`
**Explanation:** Refines existing molecular model.

### Cluster analysis
**Args:** `haddock3 --mode cluster -i models/ -o clusters`
**Explanation:** Performs clustering of generated models.

### Generate restraints
**Args:** `haddock3-restraints -i data.csv -o restraints.tbl`
**Explanation:** Generates restraint file from experimental data.

### Help command
**Args:** `haddock3 --help`
**Explanation:** Shows available options and usage information.