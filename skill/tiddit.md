---
name: tiddit
category: variant-calling
description: TIDDIT - structural variant calling.
tags: [tiddit, variant-calling]
author: oxo-call-community
source_url: "https://github.com/SciLifeLab/TIDDIT/blob/TIDDIT-3.9.5/README.md"
---

## Concepts

- **Tool Overview**: tiddit (v3.9.5) - TIDDIT - structural variant calling.
- **Core Function**: TIDDIT - structural variant calling.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tiddit`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tiddit -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run tiddit with typical input and output options.
