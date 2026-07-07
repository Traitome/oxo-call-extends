---
name: diapysef
category: annotation
description: diaPASEF - Analysis and visualization of diaPASEF proteomics data.
tags: [diapysef, annotation, proteomics, dia-pasef, mass-spectrometry]
author: oxo-call-community
source_url: "https://github.com/Roestlab/dia-pasef"
---

## Concepts

- **Tool Overview**: diapysef (v1.0.10+) is a Python tool for analysis, conversion and visualization of diaPASEF mass spectrometry data.
- **Core Function**: Processes data-independent acquisition with parallel accumulation-serial fragmentation (diaPASEF) data for proteomics analysis.
- **Input/Output**: Input: Bruker diaPASEF .d files, mzML files. Output: Converted data, analyzed results, visualizations.
- **Algorithm**: Parses Bruker raw data format and converts to standard proteomics formats for downstream analysis.
- **Key Features**: Data conversion, visualization, quality control, supports multiple input formats, open source.
- **Installation**: `conda install -c bioconda diapysef`

## Pitfalls

- **Input Requirements**: Requires Bruker diaPASEF format data or mzML files.
- **Memory Usage**: May require significant memory for large mass spectrometry datasets.
- **File Size**: Raw diaPASEF files can be very large.
- **Software Dependencies**: Requires specific Python packages and Bruker libraries.
- **Data Quality**: Results depend on input data quality and acquisition parameters.

## Examples

### Convert diaPASEF data
**Args:** `convert --input sample.d --output sample.mzml`
**Explanation:** Converts Bruker diaPASEF .d file to mzML format.

### Generate visualization
**Args:** `visualize --input sample.d --output plot.png`
**Explanation:** Generate visualization of diaPASEF acquisition scheme.

### Quality control report
**Args:** `qc --input sample.d --output qc_report.html`
**Explanation:** Generate quality control report for diaPASEF data.

### Batch conversion
**Args:** `convert --input-dir raw_data/ --output-dir mzml_data/`
**Explanation:** Convert multiple diaPASEF files in batch.

### Extract specific scan range
**Args:** `convert --input sample.d --output subset.mzml --scan-range 100-500`
**Explanation:** Extract specific scan range from diaPASEF data.