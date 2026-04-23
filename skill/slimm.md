---
name: slimm
category: metagenomics
description: SLIMM - Species Level Identification of Microbes from Metagenomes
tags: [slimm, metagenomics]
author: oxo-call-community
source_url: "https://github.com/seqan/slimm/blob/master/README.md"
---

## Concepts

- **Tool Overview**: slimm (v0.3.4) - SLIMM - Species Level Identification of Microbes from Metagenomes
- **Core Function**: SLIMM - Species Level Identification of Microbes from Metagenomes
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda slimm`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `slimm -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run slimm with typical input and output options.
