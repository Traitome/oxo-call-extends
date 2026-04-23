---
name: dinosaur
category: annotation
description: Dinosaur - peptide feature detection for mass spectrometry data.
tags: [dinosaur, annotation, proteomics, ms, feature-detection]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: Dinosaur - Peptide feature detection tool for mass spectrometry proteomics data.
- **Core Function**: Detects and quantifies peptide features (chromatographic peaks) from LC-MS data.
- **Input/Output**: Expects mzML mass spectrometry files; outputs detected features with retention time and intensity.
- **Installation**: `conda install -c bioconda dinosaur`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires mzML format mass spectrometry data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dinosaur --input sample.mzML --output features.tsv`
**Explanation:** Detects peptide features from LC-MS data.
