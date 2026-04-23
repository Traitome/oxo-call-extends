---
name: strip_it
category: assembly
description: Strip-it is a program that extracts predefined scaffolds from organic small molecules.
tags: [strip_it, assembly]
author: oxo-call-community
source_url: "http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/software/strip-it/1.0.2/strip-it.html"
---

## Concepts

- **Tool Overview**: strip_it (v1.0.2) - Strip-it is a program that extracts predefined scaffolds from organic small molecules.
- **Core Function**: Strip-it is a program that extracts predefined scaffolds from organic small molecules.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strip_it`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strip_it -i <reads.fastq> -o <output_dir>`
**Explanation:** Run strip_it with typical input and output options.
