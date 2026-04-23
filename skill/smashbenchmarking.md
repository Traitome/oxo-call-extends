---
name: smashbenchmarking
category: utility
description: Check the accuracy of one VCF callset against another
tags: [smashbenchmarking, utility, vcf]
author: oxo-call-community
source_url: "http://github.com/amplab/smash/"
---

## Concepts

- **Tool Overview**: smashbenchmarking (v1.0.1) - Check the accuracy of one VCF callset against another
- **Core Function**: Check the accuracy of one VCF callset against another
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smashbenchmarking`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smashbenchmarking -i <input_file> -o <output_file>`
**Explanation:** Run smashbenchmarking with typical input and output options.
