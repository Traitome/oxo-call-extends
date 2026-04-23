---
name: spliceai
category: variant-calling
description: A deep learning-based tool to identify splice variants.
tags: [spliceai, variant-calling]
author: oxo-call-community
source_url: "https://github.com/Illumina/SpliceAI"
---

## Concepts

- **Tool Overview**: spliceai (v1.3.1) - A deep learning-based tool to identify splice variants.
- **Core Function**: A deep learning-based tool to identify splice variants.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spliceai`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spliceai -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run spliceai with typical input and output options.
