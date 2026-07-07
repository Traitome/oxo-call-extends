---
name: seqkit
category: utility
description: seqkit - Cross-platform ultrafast toolkit for FASTA/Q file manipulation
tags: ["seqkit", "utility", "FASTA", "FASTQ"]
author: oxo-call-community
source_url: "https://bioinf.shenwei.me/seqkit"
---

## Concepts

- **Tool Overview**: seqkit (v2.13.0) is a cross-platform ultrafast toolkit for FASTA/Q file manipulation.
- **Core Function**: Provides comprehensive utilities for sequence file processing.
- **Algorithm**: Implements efficient sequence processing algorithms in Go.
- **Input/Output**: Accepts FASTA/FASTQ files and produces processed sequences.
- **Sequence Manipulation**: Focuses on fast and efficient sequence processing.
- **Applications**: Sequence quality control, filtering, transformation, and analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large FASTQ files.
- **Input Format**: Requires correct FASTA/FASTQ format.
- **Performance**: May be slow for extremely large files.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Stats
**Args:** `seqkit stats input.fasta`
**Explanation:** Shows sequence statistics.

### Filter
**Args:** `seqkit filter -m 100 -M 1000 input.fasta -o filtered.fasta`
**Explanation:** Filters sequences by length (100-1000bp).

### Reverse complement
**Args:** `seqkit rc input.fasta -o reversed.fasta`
**Explanation:** Produces reverse complement.

### Extract IDs
**Args:** `seqkit seq -n input.fasta`
**Explanation:** Extracts sequence IDs.

### Help command
**Args:** `seqkit --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqkit version`
**Explanation:** Shows current version.

### Convert FASTQ to FASTA
**Args:** `seqkit fq2fa input.fastq -o output.fasta`
**Explanation:** Converts FASTQ to FASTA format.