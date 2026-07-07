---
name: fastutils
category: formatting
description: "A light toolkit for parsing, manipulating and analysis of FASTA and FASTQ files"
tags: [fastutils, formatting, FASTA, FASTQ, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/haghshenas/fastutils"
---

## Concepts

- **Tool Overview**: fastutils is a lightweight toolkit for parsing, manipulating, and analyzing FASTA and FASTQ files with efficient performance.
- **Core Function**: Provides utilities for sequence file parsing, manipulation, and analysis.
- **Input/Output**: Input: FASTA/FASTQ files. Output: Processed sequences, statistics, transformed files.
- **Algorithm**: Implements efficient parsing algorithms for sequence files.
- **Key Features**: Lightweight design, FASTA/FASTQ support, sequence manipulation, statistics generation, cross-platform.
- **Installation**: `conda install -c bioconda fastutils`

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Format Compatibility**: Requires standard FASTA/FASTQ format.
- **File Size**: Optimized for small to medium files.
- **Quality Scores**: Assumes standard Phred quality encoding.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Read and parse
**Args:** `fastutils parse -i input.fasta -o parsed.txt`
**Explanation:** Parses FASTA file and outputs data.

### Statistics
**Args:** `fastutils stats -i input.fastq -o stats.txt`
**Explanation:** Generates sequence statistics.

### Convert formats
**Args:** `fastutils convert -i input.fastq -o output.fasta -f fasta`
**Explanation:** Converts between FASTA and FASTQ formats.

### Filter sequences
**Args:** `fastutils filter -i input.fasta -o filtered.fasta -l 100`
**Explanation:** Filters sequences by minimum length.

### Extract subsequence
**Args:** `fastutils subseq -i input.fasta -o subseq.fasta -s 10 -e 100`
**Explanation:** Extracts subsequence from sequences.