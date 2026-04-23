---
name: cofold
category: expression
description: An RNA secondary structure prediction method that takes co-transcriptional folding into account.
tags: [cofold, expression]
author: oxo-call-community
source_url: "http://www.e-rna.org/cofold/"
---

## Concepts

- **Tool Overview**: cofold (v2.0.4) - An RNA secondary structure prediction method that takes co-transcriptional folding into account.
- **Core Function**: An RNA secondary structure prediction method that takes co-transcriptional folding into account.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cofold`

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
