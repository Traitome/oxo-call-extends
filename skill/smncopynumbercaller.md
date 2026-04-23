---
name: smncopynumbercaller
category: variant-calling
description: Call copy number of SMN1, SMN2, and SMN2Δ7–8 from a BAM file.
tags: [smncopynumbercaller, variant-calling, bam]
author: oxo-call-community
source_url: "https://github.com/Illumina/SMNCopyNumberCaller"
---

## Concepts

- **Tool Overview**: smncopynumbercaller (v1.1.2) - Call copy number of SMN1, SMN2, and SMN2Δ7–8 from a BAM file.
- **Core Function**: Call copy number of SMN1, SMN2, and SMN2Δ7–8 from a BAM file.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smncopynumbercaller`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smncopynumbercaller -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run smncopynumbercaller with typical input and output options.
