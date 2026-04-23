---
name: spades
category: assembly
description: SPAdes (St. Petersburg genome assembler) is intended for both standard isolates and single-cell MDA bacteria assemblies.
tags: [spades, assembly]
author: oxo-call-community
source_url: "https://ablab.github.io/spades"
---

## Concepts

- **Tool Overview**: spades (v4.2.0) - SPAdes (St. Petersburg genome assembler) is intended for both standard isolates and single-cell MDA bacteria assemblies.
- **Core Function**: SPAdes (St. Petersburg genome assembler) is intended for both standard isolates and single-cell MDA bacteria assemblies.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spades`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spades -i <reads.fastq> -o <output_dir>`
**Explanation:** Run spades with typical input and output options.
