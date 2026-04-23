---
name: spingo
category: metagenomics
description: Species level IdentificatioN of metaGenOmic amplicons
tags: [spingo, metagenomics]
author: oxo-call-community
source_url: "https://github.com/GuyAllard/SPINGO"
---

## Concepts

- **Tool Overview**: spingo (v1.3) - Species level IdentificatioN of metaGenOmic amplicons
- **Core Function**: Species level IdentificatioN of metaGenOmic amplicons
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spingo`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spingo -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run spingo with typical input and output options.
