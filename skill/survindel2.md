---
name: survindel2
category: variant-calling
description: A CNV caller for Illumina paired-end WGS data.
tags: [survindel2, variant-calling]
author: oxo-call-community
source_url: "https://github.com/kensung-lab/SurVIndel2"
---

## Concepts

- **Tool Overview**: survindel2 (v1.1.4) - A CNV caller for Illumina paired-end WGS data.
- **Core Function**: A CNV caller for Illumina paired-end WGS data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda survindel2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `survindel2 -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run survindel2 with typical input and output options.
