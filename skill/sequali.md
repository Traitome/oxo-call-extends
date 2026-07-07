---
name: sequali
category: qc
description: sequali - Fast sequencing quality metrics
tags: ["sequali", "qc", "quality-control", "metrics"]
author: oxo-call-community
source_url: "https://sequali.readthedocs.io"
---

## Concepts

- **Tool Overview**: sequali (v1.0.2) provides fast sequencing quality metrics calculation.
- **Core Function**: Calculates quality metrics for sequencing data.
- **Algorithm**: Implements efficient quality statistics computation.
- **Input/Output**: Accepts FASTQ files and produces quality metrics.
- **Quality Control**: Focuses on sequencing quality assessment.
- **Applications**: Quality control, data assessment, and sequencing analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large FASTQ files.
- **Input Format**: Requires correct FASTQ format.
- **Performance**: May be slow for extremely large files.
- **Compression Support**: May have issues with some compression formats.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Get quality metrics
**Args:** `sequali input.fastq -o results/`
**Explanation:** Calculates quality metrics for FASTQ file.

### Gzipped input
**Args:** `sequali input.fastq.gz -o results/`
**Explanation:** Reads gzipped FASTQ file.

### Paired-end
**Args:** `sequali -1 reads_1.fastq -2 reads_2.fastq -o results/`
**Explanation:** `-1/-2` paired-end reads.

### Verbose logging
**Args:** `sequali -v input.fastq -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sequali --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sequali --version`
**Explanation:** Shows current version.

### Summary only
**Args:** `sequali -s input.fastq`
**Explanation:** `-s` shows summary only.