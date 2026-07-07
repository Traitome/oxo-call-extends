---
name: diatracer
category: annotation
description: diaTracer - Spectrum-centric analysis for diaPASEF proteomics data.
tags: [diatracer, annotation, proteomics, dia-pasef, spectrum-centric]
author: oxo-call-community
source_url: "https://diatracer.nesvilab.org/"
---

## Concepts

- **Tool Overview**: diatracer (v1.2.5+) is a spectrum-centric analysis tool for Bruker diaPASEF DIA proteomics data.
- **Core Function**: Enables spectral-library-free peptide identification and quantification from diaPASEF data.
- **Input/Output**: Input: Bruker diaPASEF .d files, optional spectral libraries. Output: Peptide identifications, quantifications, statistical reports.
- **Algorithm**: Uses spectrum-centric matching approach for peptide identification without requiring pre-built spectral libraries.
- **Key Features**: Spectral-library-free analysis, diaPASEF support, peptide quantification, open source, academic use only.
- **Installation**: `conda install -c bioconda diatracer`

## Pitfalls

- **Input Requirements**: Requires Bruker diaPASEF format data.
- **Licensing**: Available for academic research and educational purposes only.
- **Computational Resources**: May require significant computational resources for large datasets.
- **Data Quality**: Results depend on mass spectrometry data quality.
- **Software Dependencies**: Requires specific Bruker library versions.

## Examples

### Run spectrum-centric analysis
**Args:** `diatracer --input sample.d --output results/`
**Explanation:** Performs spectrum-centric analysis on diaPASEF data.

### With spectral library
**Args:** `diatracer --input sample.d --library library.msp --output results/`
**Explanation:** Use existing spectral library to supplement identification.

### Generate quantification results
**Args:** `diatracer --input sample.d --output results/ --quantify`
**Explanation:** Perform peptide quantification in addition to identification.

### Set precursor mass tolerance
**Args:** `diatracer --input sample.d --output results/ --precursor-tol 20ppm`
**Explanation:** Set precursor mass tolerance for matching.

### Batch processing
**Args:** `diatracer --input-dir samples/ --output-dir results/`
**Explanation:** Process multiple diaPASEF files in batch.