---
name: shasta
category: assembly
description: De novo assembly from Oxford Nanopore reads.
tags: [shasta, assembly]
author: oxo-call-community
source_url: "https://paoloshasta.github.io/shasta/"
---

## Concepts

- **Tool Overview**: shasta (v0.14.0) - De novo assembly from Oxford Nanopore reads.
- **Core Function**: De novo assembly from Oxford Nanopore reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shasta`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shasta -i <reads.fastq> -o <output_dir>`
**Explanation:** Run shasta with typical input and output options.
