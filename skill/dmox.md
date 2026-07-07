---
name: dmox
category: annotation
description: DMOX - Drug Metabolism and Oxidation prediction tool.
tags: [dmox, annotation, drug-metabolism, oxidation, prediction, chemoinformatics]
author: oxo-call-community
source_url: "https://github.com/dmox/dmox"
---

## Concepts

- **Tool Overview**: DMOX is a tool for predicting drug metabolism and oxidation sites.
- **Core Function**: Predicts metabolic oxidation sites and drug metabolism pathways.
- **Input/Output**: Input: Molecular structures (SMILES/SDF). Output: Predicted metabolism sites, reaction pathways.
- **Algorithm**: Uses machine learning and rule-based approaches to predict metabolic sites.
- **Key Features**: Oxidation site prediction, metabolism pathway prediction, multiple model support, visualization, batch processing.
- **Installation**: `conda install -c bioconda dmox`

## Pitfalls

- **Input Requirements**: Requires molecular structure data in SMILES or SDF format.
- **Structure Quality**: Poorly defined structures affect prediction accuracy.
- **Model Selection**: Choosing appropriate prediction model is critical.
- **False Positives**: May predict false metabolism sites.
- **Metabolite Prediction**: Does not predict actual metabolites, only sites.

## Examples

### Predict metabolism sites
**Args:** `dmox --input molecule.smi --output metabolism.tsv`
**Explanation:** Predicts drug metabolism and oxidation sites.

### With multiple molecules
**Args:** `dmox --input molecules.sdf --output metabolism.tsv`
**Explanation:** Process multiple molecules from SDF file.

### Specific enzyme prediction
**Args:** `dmox --input molecule.smi --output metabolism.tsv --enzyme cyp450`
**Explanation:** Predict sites for specific enzyme family.

### Generate visualization
**Args:** `dmox --input molecule.smi --output metabolism.tsv --visualize structure.png`
**Explanation:** Generate visualization of predicted sites on molecule.

### Batch processing
**Args:** `dmox --input-dir molecules/ --output-dir results/`
**Explanation:** Process multiple molecular structure files.