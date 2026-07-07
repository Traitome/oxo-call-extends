---
name: ucsc-fastqtofa
category: utility
description: UCSC fastqToFa - Tool for converting FASTQ to FASTA.
tags: [ucsc-fastqtofa, ucsc, fastq, fasta, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC fastqToFa - A tool for converting FASTQ to FASTA format.
- **Core Function**: Converts FASTQ sequences to FASTA format.
- **Input**: FASTQ file.
- **Output**: FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, sequence analysis, data preparation.

## Pitfalls

- **File Format**: Requires proper FASTQ format.
- **Quality Scores**: Quality scores are discarded in FASTA format.

## Examples

### Convert to FASTA
**Args:** `fastqToFa input.fastq > output.fa`
**Explanation:** Convert FASTQ to FASTA.

### With options
**Args:** `fastqToFa -strip input.fastq > output.fa`
**Explanation:** Convert and strip quality information.
