---
name: isocor
category: proteomics
description: Isotope correction for mass spectrometry labeling experiments, handling natural isotopic abundance and tracer incorporation.
tags: [isocor, proteomics, mass spectrometry, isotope labeling, metabolomics]
author: oxo-call-community
source_url: "https://isocor.readthedocs.io/"
---

## Concepts

- **Natural Isotope Correction**: Adjusts mass spectrometry data to account for naturally occurring isotopes (e.g., 13C, 15N) that interfere with tracer analysis.
- **Tracer Incorporation Analysis**: Quantifies the incorporation of stable isotope tracers (e.g., 13C-glucose) in metabolic labeling experiments.
- **Isotopologue Distribution**: Computes the relative abundance of different isotopic forms (isotopologues) of metabolites or proteins.
- **Mass Resolution Handling**: Accounts for mass spectrometer resolution limitations when distinguishing isotopic peaks.
- **Fragmentation Pattern Correction**: Corrects isotope ratios considering the fragmentation patterns observed in MS/MS experiments.
- **Standalone and Pipeline Integration**: Can be used as a standalone tool or integrated into larger proteomics/metabolomics analysis pipelines.

## Pitfalls

- **Tracer Purity**: Impure tracer compounds can introduce systematic errors in isotope ratio calculations.
- **Instrument Drift**: Mass spectrometer calibration drift over time affects isotope ratio accuracy.
- **Over-correction**: Excessive correction can distort true biological isotope incorporation signals.
- **Complex Molecules**: Molecules with many isotopic positions require careful handling to avoid computational errors.
- **Data Dependence**: Results heavily depend on the quality and completeness of input mass spectrometry data.
- **Isotope Interference**: Overlapping isotopic peaks from different molecules can confound correction algorithms.

## Examples

### Basic isotope correction
**Args:** `isocor --input data.csv --output corrected_data.csv --tracer 13C`
**Explanation:** Performs isotope correction on mass spectrometry data for 13C-labeled samples.

### Metabolomics mode
**Args:** `isocor -i metabolites.mzML -o corrected_metabolites.csv --mode metabolomics --formula-file formulas.txt`
**Explanation:** Processes metabolomics data with compound formula information for accurate correction.

### Protein-centric analysis
**Args:** `isocor -i proteins.mgf -o corrected_proteins.csv --mode proteomics --fasta proteins.fasta`
**Explanation:** Corrects isotope ratios in proteomics data using protein sequence information.

### Custom tracer configuration
**Args:** `isocor -i data.csv -o output.csv --tracer-config custom_tracer.yaml`
**Explanation:** Uses a custom configuration file for defining tracer isotopes and labeling patterns.

### Batch processing
**Args:** `isocor --batch samples.txt --output-dir results/`
**Explanation:** Processes multiple samples listed in a batch file.

### Report generation
**Args:** `isocor -i data.csv -o output.csv --generate-report`
**Explanation:** Generates a comprehensive report with correction statistics and quality metrics.