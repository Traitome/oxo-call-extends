---
name: dammit
category: expression
description: simple de novo transcriptome annotator
tags: [dammit, expression]
author: oxo-call-community
source_url: "http://dib-lab.github.io/dammit/"
---

## Concepts

- **Tool Overview**: dammit (v1.2) - simple de novo transcriptome annotator
- **Core Function**: simple de novo transcriptome annotator
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda dammit`

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
