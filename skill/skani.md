---
name: skani
category: assembly
description: skani is a fast and robust tool for calculating ANI between metagenome assembled genomes and contigs.
tags: [skani, assembly]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/skani"
---

## Concepts

- **Tool Overview**: skani (v0.3.1) - skani is a fast and robust tool for calculating ANI between metagenome assembled genomes and contigs.
- **Core Function**: skani is a fast and robust tool for calculating ANI between metagenome assembled genomes and contigs.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda skani`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `skani -i <reads.fastq> -o <output_dir>`
**Explanation:** Run skani with typical input and output options.
