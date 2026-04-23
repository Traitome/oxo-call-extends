---
name: sharkmer
category: expression
description: Kmer counter and seeded de Bruijn graph assembler for in silico PCR and genome size estimation
tags: [sharkmer, expression]
author: oxo-call-community
source_url: "https://github.com/caseywdunn/sharkmer"
---

## Concepts

- **Tool Overview**: sharkmer (v3.1.0) - Kmer counter and seeded de Bruijn graph assembler for in silico PCR and genome size estimation
- **Core Function**: Kmer counter and seeded de Bruijn graph assembler for in silico PCR and genome size estimation
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sharkmer`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sharkmer -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run sharkmer with typical input and output options.
