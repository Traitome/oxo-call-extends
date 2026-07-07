---
name: dia_umpire
category: annotation
description: DIA-Umpire - Computational analysis of DIA mass spectrometry proteomics data.
tags: [dia_umpire, annotation, proteomics, mass-spectrometry, dia]
author: oxo-call-community
source_url: "https://github.com/Nesvilab/DIA-Umpire"
---

## Concepts

- **Tool Overview**: dia_umpire (v2.1.6+) is an open source tool for data-independent acquisition (DIA) mass spectrometry proteomics data analysis.
- **Core Function**: Performs untargeted peptide/protein identification and quantitation from DIA-MS data using targeted extraction strategies.
- **Input/Output**: Input: mzML/mzXML mass spectrometry files. Output: Peptide/protein identifications, quantifications, statistical reports.
- **Algorithm**: Uses targeted extraction of fragment ion chromatograms for peptide identification and quantification.
- **Key Features**: Untargeted analysis, DIA-MS support, peptide quantification, FDR control, open source.
- **Installation**: `conda install -c bioconda dia_umpire`

## Pitfalls

- **Input Requirements**: Requires DIA mass spectrometry data in mzML/mzXML format.
- **Memory Usage**: May require significant memory for large DIA datasets.
- **Computational Time**: Analysis can be time-consuming for complex samples.
- **Data Quality**: Results depend on mass spectrometry data quality and acquisition parameters.
- **Software Dependencies**: Requires Java and specific libraries.

## Examples

### Process DIA-MS data
**Args:** `dia_umpire --input sample.mzML --output results/`
**Explanation:** Processes DIA-MS data for peptide identification and quantification.

### With custom parameters
**Args:** `dia_umpire --input sample.mzML --output results/ --params config.xml`
**Explanation:** Use custom parameter configuration file.

### Generate FDR-controlled results
**Args:** `dia_umpire --input sample.mzML --output results/ --fdr 0.01`
**Explanation:** Apply 1% FDR threshold for peptide identification.

### Batch processing
**Args:** `dia_umpire --input-dir mzml_files/ --output-dir results/`
**Explanation:** Process multiple DIA-MS files in batch.

### Extract specific m/z range
**Args:** `dia_umpire --input sample.mzML --output results/ --mz-range 400-1200`
**Explanation:** Limit analysis to specific m/z range.