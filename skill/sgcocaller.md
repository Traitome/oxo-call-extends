---
name: sgcocaller
category: variant-calling
description: Personalized haplotype construction and crossover calling in single-cell DNA sequenced gamete cells.
tags: [sgcocaller, variant-calling]
author: oxo-call-community
source_url: "https://gitlab.svi.edu.au/biocellgen-public/sgcocaller"
---

## Concepts

- **Tool Overview**: sgcocaller (v0.3.9) - Personalized haplotype construction and crossover calling in single-cell DNA sequenced gamete cells.
- **Core Function**: Personalized haplotype construction and crossover calling in single-cell DNA sequenced gamete cells.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sgcocaller`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sgcocaller -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sgcocaller with typical input and output options.
