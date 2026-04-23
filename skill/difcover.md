---
name: difcover
category: qc
description: Pipeline to identify genomic regions with read coverage differences between pairs of samples.
tags: [difcover, qc, coverage, differential, cnv]
author: oxo-call-community
source_url: "https://github.com/timnat/DifCover"
---

## Concepts

- **Tool Overview**: DifCover v3.0.1 - Pipeline for identifying genomic regions with differential read coverage between sample pairs.
- **Core Function**: Detects coverage differences that may indicate copy number variations or other structural changes.
- **Input/Output**: Expects BAM files; outputs genomic regions with significant coverage differences.
- **Installation**: `conda install -c bioconda difcover`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly indexed BAM files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `difcover --sample1 a.bam --sample2 b.bam --output diff_regions.bed`
**Explanation:** Identifies regions with differential coverage between samples.
