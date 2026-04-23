---
name: sylph
category: metagenomics
description: sylph quickly enables querying of genomes against even low-coverage shotgun metagenomes to find nearest neighbour ANI.
tags: [sylph, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/sylph/blob/v0.9.0/README.md"
---

## Concepts

- **Tool Overview**: sylph (v0.9.0) - sylph quickly enables querying of genomes against even low-coverage shotgun metagenomes to find nearest neighbour ANI.
- **Core Function**: sylph quickly enables querying of genomes against even low-coverage shotgun metagenomes to find nearest neighbour ANI.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sylph`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sylph -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run sylph with typical input and output options.
