---
name: snap-aligner
category: alignment
description: Scalable Nucleotide Alignment Program -- a fast and accurate read aligner for high-throughput sequencing data.
tags: [snap-aligner, alignment]
author: oxo-call-community
source_url: "https://www.microsoft.com/en-us/research/project/snap"
---

## Concepts

- **Tool Overview**: snap-aligner (v2.0.5) - Scalable Nucleotide Alignment Program -- a fast and accurate read aligner for high-throughput sequencing data.
- **Core Function**: Scalable Nucleotide Alignment Program -- a fast and accurate read aligner for high-throughput sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snap-aligner`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snap-aligner -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run snap-aligner with typical input and output options.
