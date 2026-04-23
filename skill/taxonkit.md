---
name: taxonkit
category: metagenomics
description: A Cross-platform and Efficient NCBI Taxonomy Toolkit
tags: [taxonkit, metagenomics]
author: oxo-call-community
source_url: "https://github.com/shenwei356/taxonkit"
---

## Concepts

- **Tool Overview**: taxonkit (v0.20.0) - A Cross-platform and Efficient NCBI Taxonomy Toolkit
- **Core Function**: A Cross-platform and Efficient NCBI Taxonomy Toolkit
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxonkit`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxonkit -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run taxonkit with typical input and output options.
