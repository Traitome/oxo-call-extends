---
name: comparems2
category: formatting
description: Compare MS/MS spectra between two MGF datasets
tags: [comparems2, mass-spectrometry, proteomics, mgf, spectral-comparison]
author: oxo-call-community
source_url: "http://www.ms-utils.org/compareMS2.html"
---

## Concepts

- **Tool Overview**: compareMS2 is a simple tool for globally comparing all tandem mass spectrometry (MS/MS) spectra between two datasets in Mascot Generic Format (MGF).
- **Core Function**: Compares MS/MS spectra from two experiments to identify common and unique spectra, useful for replicate comparison or method evaluation.
- **Algorithm**: Uses spectral similarity metrics to match MS/MS spectra based on fragment ion patterns.
- **Input**: Two MGF files containing MS/MS spectra from different experiments.
- **Output**: Comparison report with common and unique spectra, similarity scores.
- **Application**: Proteomics quality control, replicate comparison, and method validation.
- **Installation**: Install via bioconda: `conda install -c bioconda comparems2`

## Pitfalls

- **File Format**: Requires properly formatted MGF files.
- **Spectral Quality**: Low-quality spectra may produce false negatives.
- **Similarity Threshold**: Threshold settings affect matching sensitivity.
- **File Size**: Large MGF files may require significant processing time.
- **Precursor Mass**: Precursor mass tolerance affects matching accuracy.

## Examples

### Compare two MGF files
**Args:** `comparems2 -i experiment1.mgf experiment2.mgf -o comparison.txt`
**Explanation:** Compares spectra between two MGF datasets.

### With custom similarity threshold
**Args:** `comparems2 -i exp1.mgf exp2.mgf -t 0.8 -o comparison.txt`
**Explanation:** Uses 0.8 similarity threshold for spectral matching.

### Generate detailed report
**Args:** `comparems2 -i exp1.mgf exp2.mgf -v -o detailed_report.txt`
**Explanation:** Generates verbose report with all spectral matches.

### Display help
**Args:** `comparems2 --help`
**Explanation:** Shows all available options and usage information.