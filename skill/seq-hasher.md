---
name: seq-hasher
category: variant-calling
description: Compute hash digests for DNA sequences in a FASTA file, with support for circular permutations
tags: [seq-hasher, variant-calling, fasta]
author: oxo-call-community
source_url: "https://github.com/apcamargo/seq-hasher"
---

## Concepts

- **Tool Overview**: seq-hasher (v0.2.0) - Compute hash digests for DNA sequences in a FASTA file, with support for circular permutations
- **Core Function**: Compute hash digests for DNA sequences in a FASTA file, with support for circular permutations
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seq-hasher`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seq-hasher -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run seq-hasher with typical input and output options.
