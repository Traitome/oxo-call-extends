---
name: mzmine
category: utility
description: Integrative analysis of multimodal mass spectrometry data.
tags: [mzmine, utility, mass-spectrometry, metabolomics, lipidomics]
author: oxo-call-community
source_url: "https://github.com/mzmine/mzmine"
---

## Concepts

- **Tool Overview**: MZmine v4.7.29 - open-source mass spectrometry data processing and visualization software.
- **Core Function**: Enables large-scale metabolomics and lipidomics research via spectral preprocessing, feature detection, and compound identification.
- **Input/Output**: Takes raw MS data (mzML, mzXML, etc.); outputs feature tables, identified compounds, and visualizations.
- **Installation**: `conda install -c bioconda mzmine`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports mzML, mzXML, and other common MS formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.mzML -o output_dir`
**Explanation:** Processes mass spectrometry data for feature detection and identification.
