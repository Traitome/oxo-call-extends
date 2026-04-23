---
name: sweepfinder2
category: variant-calling
description: A program written in C that can perform genomic scans for recent selective sweeps selection while controlling for background selection and mutation rate variation.
tags: [sweepfinder2, variant-calling]
author: oxo-call-community
source_url: "https://degiorgiogroup.fau.edu/sf2.html"
---

## Concepts

- **Tool Overview**: sweepfinder2 (v1.0) - A program written in C that can perform genomic scans for recent selective sweeps selection while controlling for background selection and mutation rate variation.
- **Core Function**: A program written in C that can perform genomic scans for recent selective sweeps selection while controlling for background selection and mutation rate variation.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sweepfinder2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sweepfinder2 -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sweepfinder2 with typical input and output options.
