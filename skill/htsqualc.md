---
name: htsqualc
category: qc
description: HTSQualC is an automated quality control analysis tool for a single and paired-end high-throughput sequencing data (HTS)
tags: [htsqualc, qc]
author: oxo-call-community
source_url: "https://reneshbedre.github.io/blog/htseqqc.html"
---

## Concepts

- **Tool Overview**: htsqualc (v1.1) - HTSQualC is an automated quality control analysis tool for a single and paired-end high-throughput sequencing data (HTS)
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda htsqualc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
