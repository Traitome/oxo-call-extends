---
name: kssd
category: alignment
description: K-mer substring space decomposition
tags: [kssd, alignment, sequence, alignment]
author: oxo-call-community
source_url: "https://github.com/yhg926/public_kssd"
---

## Concepts

- **Tool Overview**: kssd v2.21 - Kssd is a command-line tool for large-scale sequences sketching and resemblance- and containment-analysis. It sketches sequences by k-mer substring space sampling/shuffling. It handles DNA sequences of both fasta or fastq format, whether gzipped or not..
- **Core Function**: K-mer substring space decomposition
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kssd`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
