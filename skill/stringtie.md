---
name: stringtie
category: expression
description: StringTie employs efficient algorithms for transcript structure recovery and abundance estimation from bulk RNA-Seq reads aligned to a reference genome.
tags: [stringtie, expression]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/stringtie/index.shtml?t=manual"
---

## Concepts

- **Tool Overview**: stringtie (v3.0.3) - StringTie employs efficient algorithms for transcript structure recovery and abundance estimation from bulk RNA-Seq reads aligned to a reference genome.
- **Core Function**: StringTie employs efficient algorithms for transcript structure recovery and abundance estimation from bulk RNA-Seq reads aligned to a reference genome.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stringtie`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stringtie -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run stringtie with typical input and output options.
