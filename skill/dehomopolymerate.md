---
name: dehomopolymerate
category: utility
description: Tool for removing homopolymer runs from sequences.
tags: [dehomopolymerate, utility, sequence-processing, homopolymer]
author: oxo-call-community
source_url: "https://github.com/lskatz/dehomopolymerate"
---

## Concepts

- **Tool Overview**: dehomopolymerate - Tool for processing sequences by removing or marking homopolymer runs.
- **Core Function**: Removes or collapses homopolymer stretches in nucleotide sequences to reduce sequencing error artifacts.
- **Input/Output**: Expects FASTA/FASTQ files; outputs processed sequences with reduced homopolymers.
- **Installation**: `conda install -c bioconda dehomopolymerate`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure valid FASTA/FASTQ format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dehomopolymerate --input reads.fq --output processed.fq`
**Explanation:** Removes homopolymer stretches from input sequences.
