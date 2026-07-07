---
name: genform
category: mass-spectrometry
description: GenForm - Generation of molecular formulas by high-resolution MS and MS/MS data.
tags: [genform, mass-spectrometry, metabolomics, molecular-formula]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/genform"
---

## Concepts
- **Molecular Formula Generation**: Generates possible molecular formulas from MS data.
- **High-Resolution MS**: Analyzes high-resolution mass spectrometry data.
- **MS/MS Analysis**: Uses tandem mass spectrometry data.
- **Isotope Pattern Matching**: Matches observed isotope patterns.
- **Elemental Composition**: Determines elemental composition of molecules.

## Pitfalls
- **Resolution Dependency**: Requires high-resolution mass spectrometry data.
- **Complex Mixtures**: Complex samples may produce ambiguous results.
- **Noise Handling**: Requires careful noise filtering.
- **Isotope Interference**: Isotope peaks can interfere with analysis.
- **Database Dependence**: Results depend on reference databases.

## Examples
### Generate molecular formulas
**Args:** `genform -i ms_data.mzML -o formulas.txt`
**Explanation:** Generates molecular formulas from mass spectrometry data.

### With MS/MS data
**Args:** `genform -i ms_data.mzML -ms2 msms_data.mzML -o formulas.txt`
**Explanation:** Uses both MS and MS/MS data for formula generation.

### Set mass tolerance
**Args:** `genform -i ms_data.mzML -t 5ppm -o formulas.txt`
**Explanation:** Sets mass tolerance to 5 parts per million.

### Filter by elements
**Args:** `genform -i ms_data.mzML -e C,H,O,N -o formulas.txt`
**Explanation:** Restricts formula generation to specific elements.

### Batch processing
**Args:** `genform -i ./ms_files/ -o ./formulas/`
**Explanation:** Processes multiple mass spectrometry files in batch.