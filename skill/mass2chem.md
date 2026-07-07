---
name: mass2chem
category: utility
description: Utilities for interpreting and processing mass spectrometry data.
tags: [mass2chem, mass-spectrometry, metabolomics, proteomics]
author: oxo-call-community
source_url: "https://github.com/shuzhao-li/mass2chem"
---

## Concepts

- **Tool Overview**: mass2chem provides utilities for mass spectrometry data interpretation.
- **Core Function**: Processes and analyzes mass spectrometry data for metabolomics and proteomics.
- **Mass Calculation**: Computes molecular masses and isotopic distributions.
- **Peak Matching**: Identifies compounds based on mass-to-charge ratios.
- **Input/Output**: Accepts mass spec data files, produces annotated results.
- **Installation**: `conda install -c bioconda mass2chem`

## Pitfalls

- **Data Quality**: Requires high-quality mass spec data for accurate results.
- **Calibration**: Mass calibration affects identification accuracy.
- **Adduct Formation**: May misidentify compounds due to adduct formation.
- **Isotope Overlap**: Isotopic peaks can complicate peak identification.
- **Computation Time**: Processing large datasets can be slow.
- **Memory Usage**: High memory requirements for complex analyses.

## Examples

### Calculate molecular mass
**Args:** `mass2chem mass -f "C6H12O6"`
**Explanation:** Computes mass of glucose molecule.

### Annotate peaks
**Args:** `mass2chem annotate -i peaks.mzML -o annotated.csv`
**Explanation:** Annotates mass spec peaks with compound information.

### Isotope distribution
**Args:** `mass2chem isotope -f "C6H12O6"`
**Explanation:** Shows isotopic distribution of molecule.

### Batch processing
**Args:** `mass2chem batch -d data/ -o results/`
**Explanation:** Processes multiple mass spec files.

### Database search
**Args:** `mass2chem search -i peaks.txt -db metabolites.db -o matches.csv`
**Explanation:** Searches metabolite database for matching peaks.

### Help documentation
**Args:** `mass2chem --help`
**Explanation:** Displays available commands and options.
