---
name: cats-rb
category: expression
description: Reference-based transcriptome assembly quality assessment tool.
tags: [cats-rb, expression]
author: oxo-call-community
source_url: "https://github.com/bodulic/CATS-rb/blob/main/README.md"
---

## Concepts

- **Tool Overview**: cats-rb (v1.0.3) - Reference-based transcriptome assembly quality assessment tool.
- **Core Function**: CATS-rb evaluates transcriptome assemblies using the reference genome of the corresponding species.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cats-rb`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
