---
name: deltamsi
category: variant-calling
description: DeltaMSI - AI-based modeling of microsatellite instability scoring on NGS data.
tags: [deltamsi, variant-calling, msi, microsatellite, deep-learning]
author: oxo-call-community
source_url: "https://github.com/RADar-AZDelta/DeltaMSI"
---

## Concepts

- **Tool Overview**: DeltaMSI v1.0.1 - AI-based tool for microsatellite instability (MSI) scoring from NGS data.
- **Core Function**: Detects and scores microsatellite instability using artificial intelligence models on next-generation sequencing data.
- **Input/Output**: Expects BAM files and reference genome; outputs MSI scores and classifications.
- **Installation**: `conda install -c bioconda deltamsi`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly aligned BAM files with microsatellite loci coverage.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deltamsi --bam sample.bam --ref ref.fa --output msi_report.tsv`
**Explanation:** Scores microsatellite instability from NGS data.
