---
name: coverageanomalyscanner
category: qc
description: Application to find local anomalies in read coverage and to predict putative SV events.
tags: [coverageanomalyscanner, qc]
author: oxo-call-community
source_url: "https://github.com/rki-mf1/CoverageAnomalyScanner"
---

## Concepts

- **Tool Overview**: coverageanomalyscanner (v0.2.3) - Application to find local anomalies in read coverage and to predict putative SV events.
- **Core Function**: Application to find local anomalies in read coverage and to predict putative SV events.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda coverageanomalyscanner`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
