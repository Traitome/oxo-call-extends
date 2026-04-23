---
name: sequencetools
category: variant-calling
description: A tool (pileupCaller) for processing ancient DNA sequencing data
tags: [sequencetools, variant-calling]
author: oxo-call-community
source_url: "https://github.com/stschiff/sequenceTools"
---

## Concepts

- **Tool Overview**: sequencetools (v1.6.0.0) - A tool (pileupCaller) for processing ancient DNA sequencing data
- **Core Function**: A tool (pileupCaller) for processing ancient DNA sequencing data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sequencetools`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sequencetools -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sequencetools with typical input and output options.
