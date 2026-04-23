---
name: clustalw
category: alignment
description: ClustalW2 is a general purpose multiple sequence alignment program for DNA or proteins.
tags: [clustalw, alignment]
author: oxo-call-community
source_url: "http://www.clustal.org/download/clustalw_help.txt"
---

## Concepts

- **Tool Overview**: clustalw (v2.1) - ClustalW2 is a general purpose multiple sequence alignment program for DNA or proteins.
- **Core Function**: ClustalW2 is a general purpose multiple sequence alignment program for DNA or proteins.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda clustalw`

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
