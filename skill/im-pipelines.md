---
name: im-pipelines
category: cheminformatics
description: Components for cheminformatics and computational chemistry workflows
tags: [im-pipelines, cheminformatics, computational-chemistry, drug-discovery]
author: oxo-call-community
source_url: "https://github.com/InformaticsMatters/pipelines"
---

## Concepts

- **Tool Overview**: im-pipelines (v1.1.6) provides reusable components and workflows for cheminformatics and computational chemistry applications.
- **Core Function**: Enables construction of modular pipelines for molecular property calculation, compound screening, and drug discovery workflows.
- **Input/Output**: Accepts various molecular formats (SMILES, SDF, PDB). Outputs computed properties, descriptors, and screening results.
- **Modular Architecture**: Components can be combined in flexible workflows for diverse computational chemistry tasks.
- **High-Performance Computing**: Supports parallel processing and integration with HPC environments.

## Pitfalls

- **Format Compatibility**: Ensure input molecules are in supported formats with proper validation.
- **Computational Resources**: Some calculations (e.g., quantum chemistry) require significant computational resources.
- **Parameter Tuning**: Proper parameter selection is critical for accurate property predictions.
- **Result Interpretation**: Computational chemistry results require domain expertise for proper interpretation.
- **Licensing**: Some third-party tools integrated in pipelines may have specific licensing requirements.

## Examples

### Run molecular property calculation
**Args:** `im-pipelines calculate -i compounds.sdf -p molecular_weight logp tpsa -o properties.tsv`
**Explanation:** Calculates molecular weight, logP, and TPSA for compounds in SDF file.

### Virtual screening workflow
**Args:** `im-pipelines screen -i library.sdf -t target.pdb -o hits.sdf --top-n 100`
**Explanation:** Performs virtual screening and returns top 100 hits against target protein.

### Convert molecular formats
**Args:** `im-pipelines convert -i input.smiles -f sdf -o output.sdf`
**Explanation:** Converts molecules from SMILES format to SDF format.

### QSAR model building
**Args:** `im-pipelines qsar -i training_data.csv -m random_forest -o model.pkl`
**Explanation:** Builds QSAR model using random forest algorithm.

### ADMET property prediction
**Args:** `im-pipelines admet -i compounds.sdf -o admet_predictions.tsv`
**Explanation:** Predicts ADMET properties (absorption, distribution, metabolism, excretion, toxicity).

### Molecular docking
**Args:** `im-pipelines dock -i ligands.sdf -r receptor.pdb -o docking_results.sdf`
**Explanation:** Performs molecular docking of ligands against receptor structure.