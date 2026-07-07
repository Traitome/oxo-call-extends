---
name: cfm
category: metabolomics
description: Competitive Fragmentation Modeling tools for spectrum prediction and metabolite identification
tags: [cfm, metabolomics, mass-spectrometry, fragmentation, metabolite-identification]
author: oxo-call-community
source_url: "https://sourceforge.net/p/cfm-id/wiki/Home/"
---

## Concepts

- **Tool Overview**: CFM provides tools for applying Competitive Fragmentation Modeling to spectrum prediction and metabolite identification tasks.
- **Core Function**: Predicts mass spectra from molecular structures and identifies metabolites from MS/MS data.
- **Algorithm**: Uses machine learning models trained on experimental fragmentation data.
- **Input**: Molecular structures (SMILES, InChI) or mass spectrometry data.
- **Output**: Predicted spectra, fragmentation patterns, and metabolite identifications.
- **Application**: Metabolomics research and mass spectrometry data analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cfm`

## Pitfalls

- **Training Data**: Model performance depends on training data quality and coverage.
- **Molecular Format**: Requires correct molecular structure format (SMILES/InChI).
- **Computational Time**: Spectrum prediction can be computationally intensive.
- **Database Dependencies**: May require reference spectral databases.

## Examples

### Predict spectrum from SMILES
**Args:** `cfm-predict -s "CCO" -o spectrum.txt`
**Explanation:** Predicts mass spectrum for ethanol (SMILES: CCO).

### Identify metabolite from MS/MS
**Args:** `cfm-identify -i msms_data.mzML -o identifications.tsv`
**Explanation:** Identifies metabolites from MS/MS data.

### Generate fragments
**Args:** `cfm-fragment -s "C(=O)O" -o fragments.txt`
**Explanation:** Generates fragmentation patterns for acetic acid.

### Display help
**Args:** `cfm-predict --help`
**Explanation:** Shows all available options and usage information.