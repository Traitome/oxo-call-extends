---
name: spacerextractor
category: metagenomics
description: Extract CRISPR spacers from metagenome short reads.
tags: [spacerextractor, metagenomics]
author: oxo-call-community
source_url: "https://code.jgi.doe.gov/SRoux/spacerextractor/-/blob/0.9.8/README.md"
---

## Concepts

- **Tool Overview**: spacerextractor (v0.9.8) - Extract CRISPR spacers from metagenome short reads.
- **Core Function**: Extract CRISPR spacers from metagenome short reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spacerextractor`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spacerextractor -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run spacerextractor with typical input and output options.
