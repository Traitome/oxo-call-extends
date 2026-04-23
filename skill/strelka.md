---
name: strelka
category: variant-calling
description: Strelka calls somatic and germline small variants from mapped sequencing reads
tags: [strelka, variant-calling]
author: oxo-call-community
source_url: "https://github.com/Illumina/strelka"
---

## Concepts

- **Tool Overview**: strelka (v2.9.10) - Strelka calls somatic and germline small variants from mapped sequencing reads
- **Core Function**: Strelka calls somatic and germline small variants from mapped sequencing reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strelka`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strelka -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run strelka with typical input and output options.
