---
name: strainscan
category: metagenomics
description: One efficient and accurate strain-level microbiome composition analysis tool based on reference genomes and k-mers.
tags: [strainscan, metagenomics]
author: oxo-call-community
source_url: "https://github.com/liaoherui/StrainScan"
---

## Concepts

- **Tool Overview**: strainscan (v1.0.14) - One efficient and accurate strain-level microbiome composition analysis tool based on reference genomes and k-mers.
- **Core Function**: One efficient and accurate strain-level microbiome composition analysis tool based on reference genomes and k-mers.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strainscan`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strainscan -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run strainscan with typical input and output options.
