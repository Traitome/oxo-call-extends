---
name: spestimator
category: annotation
description: A tool to predict bacterial species from fasta files using RefSeq 16S.
tags: [spestimator, annotation, fasta]
author: oxo-call-community
source_url: "https://github.com/erinyoung/Spestimator"
---

## Concepts

- **Tool Overview**: spestimator (v0.3.0.234) - A tool to predict bacterial species from fasta files using RefSeq 16S.
- **Core Function**: A tool to predict bacterial species from fasta files using RefSeq 16S.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spestimator`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spestimator -i <input.fasta> -o <output.gff>`
**Explanation:** Run spestimator with typical input and output options.
