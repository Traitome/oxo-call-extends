---
name: fastq-tools
category: formatting
description: "A collection of fastq manipulation scripts written in C for speed."
tags: [fastq-tools, formatting, FASTQ, manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dcjones/fastq-tools"
---

## Concepts

- **Tool Overview**: fastq-tools is a collection of high-performance FASTQ manipulation utilities written in C for speed.
- **Core Function**: Provides various FASTQ manipulation operations with optimized performance.
- **Input/Output**: Input: FASTQ files. Output: Processed sequences, statistics, transformed files.
- **Algorithm**: Implements efficient C-based parsing and processing algorithms.
- **Key Features**: Fast C implementation, multiple utilities, sequence manipulation, statistics, format conversion.
- **Installation**: `conda install -c bioconda fastq-tools`

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Format Compatibility**: Requires standard FASTQ format.
- **Quality Scores**: Assumes standard Phred quality encoding.
- **Platform Dependencies**: May have platform-specific behavior.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Count sequences
**Args:** `fastq-count reads.fastq`
**Explanation:** Counts sequences in FASTQ file.

### Convert to FASTA
**Args:** `fastq-to-fasta reads.fastq > output.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Reverse complement
**Args:** `fastq-revcomp reads.fastq > reversed.fastq`
**Explanation:** Generates reverse complement of sequences.

### Quality statistics
**Args:** `fastq-qual reads.fastq`
**Explanation:** Shows quality statistics.

### Filter by length
**Args:** `fastq-filter reads.fastq --min-length 100 > filtered.fastq`
**Explanation:** Filters reads by minimum length.