---
name: acdc
category: qc
description: Automated contamination detection and confidence estimation for single-cell genome data.
tags: [acdc, qc, contamination, single-cell, genome-binning]
author: oxo-call-community
source_url: "https://github.com/mlux86/acdc"
---

## Concepts

- **Tool Overview**: Detects contamination and estimates confidence in single-cell genome data. Version 1.02.
- **Core Function**: Identifies contaminated bins in single-cell genomics and estimates confidence scores for genome quality assessment.
- **Input/Output**: Input is genome bins/profiles; output is contamination reports and confidence scores.
- **Installation**: Install via bioconda: `conda install -c bioconda acdc`
- **Platform Support**: Linux (x86_64)
- **Single-Cell Focus**: Designed for single-cell genomics where contamination from other cells is a common issue.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Input Format**: Requires specific input format for genome bins or profiles. Check documentation.
- **Single-Cell Specific**: Optimized for single-cell data. May not be suitable for bulk genomic data.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Check for contamination
**Args:** `-i genome_bins/ -o contamination_report.txt`
**Explanation:** Analyzes genome bins for contamination and outputs a detailed report with confidence scores.

### Run with custom threshold
**Args:** `-i bins/ --threshold 0.05 -o report.txt`
**Explanation:** Uses a custom contamination threshold of 5%. Lower thresholds are more sensitive but may increase false positives.
