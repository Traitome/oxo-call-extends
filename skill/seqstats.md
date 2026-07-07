---
name: seqstats
category: utility
description: seqstats - Quick summary statistics on FASTA/FASTQ files
tags: ["seqstats", "utility", "FASTA", "FASTQ"]
author: oxo-call-community
source_url: "https://github.com/clwgg/seqstats"
---

## Concepts

- **Tool Overview**: seqstats (v1.0.0) provides quick summary statistics on FASTA/FASTQ(.gz) files.
- **Core Function**: Calculates statistics for sequence files.
- **Algorithm**: Implements efficient parsing and statistics calculation.
- **Input/Output**: Accepts FASTA/FASTQ files and produces statistics.
- **Statistics**: Focuses on generating sequence statistics.
- **Applications**: Quality control, data assessment, and sequence analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large files.
- **Input Format**: Requires correct FASTA/FASTQ format.
- **Performance**: May be slow for extremely large files.
- **Compression Support**: May have issues with some compression formats.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Get stats
**Args:** `seqstats input.fasta`
**Explanation:** Shows statistics for FASTA file.

### From FASTQ
**Args:** `seqstats input.fastq`
**Explanation:** Shows statistics for FASTQ file.

### Gzipped input
**Args:** `seqstats input.fastq.gz`
**Explanation:** Reads gzipped FASTQ file.

### Verbose logging
**Args:** `seqstats -v input.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqstats --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqstats --version`
**Explanation:** Shows current version.

### Output JSON
**Args:** `seqstats -j input.fasta`
**Explanation:** `-j` outputs statistics in JSON format.