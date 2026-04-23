---
name: age-metasv
category: alignment
description: optimal alignment of sequences with structural variants (SVs), modifiied for MetaSV integration
tags: [age-metasv, alignment]
author: oxo-call-community
source_url: "https://github.com/marghoob/AGE/tree/simple-parseable-output"
---

## Concepts

- **Tool Overview**: age-metasv (v2015.01.29.3) - optimal alignment of sequences with structural variants (SVs), modifiied for MetaSV integration
- **Core Function**: optimal alignment of sequences with structural variants (SVs), modifiied for MetaSV integration
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda age-metasv`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
