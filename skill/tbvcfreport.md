---
name: tbvcfreport
category: variant-calling
description: Parses SnpEff annotated M.tb VCF(s) and generates an interactive HTML-based report.
tags: [tbvcfreport, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/COMBAT-TB/tbvcfreport/blob/master/README.md"
---

## Concepts

- **Tool Overview**: tbvcfreport (v1.0.1) - Parses SnpEff annotated M.tb VCF(s) and generates an interactive HTML-based report.
- **Core Function**: Parses SnpEff annotated M.tb VCF(s) and generates an interactive HTML-based report.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tbvcfreport`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tbvcfreport -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run tbvcfreport with typical input and output options.
