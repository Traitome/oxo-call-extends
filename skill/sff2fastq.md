---
name: sff2fastq
category: formatting
description: Extract 454 Genome Sequencer reads from a SFF file and convert them into a FASTQ formatted output
tags: [sff2fastq, formatting, fastq]
author: oxo-call-community
source_url: "https://github.com/indraniel/sff2fastq"
---

## Concepts

- **Tool Overview**: sff2fastq (v0.9.2) - Extract 454 Genome Sequencer reads from a SFF file and convert them into a FASTQ formatted output
- **Core Function**: Extract 454 Genome Sequencer reads from a SFF file and convert them into a FASTQ formatted output
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sff2fastq`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sff2fastq -i <input_file> -o <output_file>`
**Explanation:** Run sff2fastq with typical input and output options.
