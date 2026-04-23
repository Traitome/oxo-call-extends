---
name: tepid
category: variant-calling
description: TEPID uses paired-end illumina sequencing reads to identify novel TE variants.
tags: [tepid, variant-calling]
author: oxo-call-community
source_url: "https://github.com/ListerLab/TEPID"
---

## Concepts

- **Tool Overview**: tepid (v0.10) - TEPID uses paired-end illumina sequencing reads to identify novel TE variants.
- **Core Function**: TEPID uses paired-end illumina sequencing reads to identify novel TE variants.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tepid`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tepid -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run tepid with typical input and output options.
