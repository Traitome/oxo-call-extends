---
name: dodge
category: metagenomics
description: DODGE - Dynamic Outbreak Detection for Genomic Epidemiology.
tags: [dodge, metagenomics, outbreak-detection, epidemiology, genomic-surveillance]
author: oxo-call-community
source_url: "https://github.com/LanLab/dodge"
---

## Concepts

- **Tool Overview**: DODGE v1.0.1 - Automated point source bacterial outbreak detection using genomic surveillance data.
- **Core Function**: Detects bacterial outbreaks from cumulative long-term genomic surveillance data.
- **Input/Output**: Expects genomic surveillance data; outputs outbreak detection alerts.
- **Installation**: `conda install -c bioconda dodge`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires cumulative genomic surveillance data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dodge --input surveillance.tsv --output outbreak_alerts.tsv`
**Explanation:** Detects potential outbreaks from genomic surveillance data.
