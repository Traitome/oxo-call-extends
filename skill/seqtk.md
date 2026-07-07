---
name: seqtk
category: utility
description: seqtk - Fast and lightweight tool for processing FASTA/FASTQ sequences
tags: ["seqtk", "utility", "FASTA", "FASTQ"]
author: oxo-call-community
source_url: "https://github.com/lh3/seqtk/blob/v1.5/README.md"
---

## Concepts

- **Tool Overview**: seqtk (v1.5) is a fast and lightweight tool for processing sequences in FASTA or FASTQ format.
- **Core Function**: Provides various utilities for sequence manipulation and analysis.
- **Algorithm**: Implements efficient sequence processing algorithms in C.
- **Input/Output**: Accepts FASTA/FASTQ files and produces processed sequences.
- **Sequence Processing**: Focuses on fast and memory-efficient sequence operations.
- **Applications**: Sequence filtering, trimming, subsampling, and format conversion.

## Pitfalls

- **Memory Usage**: High memory requirements for large FASTQ files.
- **Input Format**: Requires correct FASTA/FASTQ format.
- **Performance**: May be slow for extremely large files.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Subsample reads
**Args:** `seqtk sample -s100 input.fastq 10000 > sampled.fastq`
**Explanation:** Samples 10,000 reads with seed 100.

### Trim reads
**Args:** `seqtk trimfq input.fastq > trimmed.fastq`
**Explanation:** Trims low-quality bases from reads.

### Reverse complement
**Args:** `seqtk seq -r input.fasta > reversed.fasta`
**Explanation:** Produces reverse complement.

### Convert FASTQ to FASTA
**Args:** `seqtk seq -A input.fastq > output.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Help command
**Args:** `seqtk --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqtk version`
**Explanation:** Shows current version.

### Filter by quality
**Args:** `seqtk quality -q 20 input.fastq > filtered.fastq`
**Explanation:** Filters reads by quality score.