---
name: snoopy
category: variant-calling
description: Metagenomic SNP caller for strain-level variant detection in long reads.
tags: [snoopy, variant-calling]
author: oxo-call-community
source_url: "https://github.com/RolandFaure/snoopy"
---

## Concepts

- **Tool Overview**: snoopy (v0.4.3) - Metagenomic SNP caller for strain-level variant detection in long reads.
- **Core Function**: Metagenomic SNP caller for strain-level variant detection in long reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snoopy`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snoopy -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run snoopy with typical input and output options.
