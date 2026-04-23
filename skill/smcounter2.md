---
name: smcounter2
category: variant-calling
description: smCounter2: an accurate low-frequency variant caller for targeted sequencing data with unique molecular identifiers
tags: [smcounter2, variant-calling]
author: oxo-call-community
source_url: "https://github.com/qiaseq/qiaseq-smcounter-v2"
---

## Concepts

- **Tool Overview**: smcounter2 (v0.1.2018.08.28) - smCounter2: an accurate low-frequency variant caller for targeted sequencing data with unique molecular identifiers
- **Core Function**: smCounter2: an accurate low-frequency variant caller for targeted sequencing data with unique molecular identifiers
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smcounter2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smcounter2 -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run smcounter2 with typical input and output options.
