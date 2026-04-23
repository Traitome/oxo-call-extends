---
name: dia_umpire
category: annotation
description: DIA-Umpire - computational analysis of data independent acquisition (DIA) mass spectrometry proteomics data.
tags: [dia_umpire, annotation, proteomics, mass-spectrometry, dia]
author: oxo-call-community
source_url: "https://github.com/Nesvilab/DIA-Umpire"
---

## Concepts

- **Tool Overview**: DIA-Umpire v2.1.6 - Open source tool for DIA mass spectrometry proteomics data analysis.
- **Core Function**: Performs untargeted peptide/protein identification and quantitation from DIA-MS data with targeted extraction.
- **Input/Output**: Expects mzML/mzXML mass spectrometry files; outputs peptide/protein identifications and quantifications.
- **Installation**: `conda install -c bioconda dia_umpire`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires DIA mass spectrometry data in mzML/mzXML format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dia_umpire --input sample.mzML --output results/`
**Explanation:** Processes DIA-MS data for peptide identification and quantification.
