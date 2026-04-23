---
name: chromhmm
category: epigenomics
description: ChromHMM is software for learning and characterizing chromatin states. ChromHMM can integrate multiple chromatin datasets such as ChIP-seq data of various histone modifications to discover de novo the major re-occuring combinatorial and spatial patterns of marks.
tags: [chromhmm, epigenomics]
author: oxo-call-community
source_url: "https://github.com/jernst98/ChromHMM"
---

## Concepts

- **Tool Overview**: chromhmm (v1.27) - ChromHMM is software for learning and characterizing chromatin states. ChromHMM can integrate multiple chromatin datasets such as ChIP-seq data of various histone modifications to discover de novo the major re-occuring combinatorial and spatial patterns of marks.
- **Core Function**: ChromHMM is software for learning and characterizing chromatin states. ChromHMM can integrate multiple chromatin datasets such as ChIP-seq data of various histone modifications to discover de novo the major re-occuring combinatorial and spatial patterns of marks.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda chromhmm`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r reference.fasta -o methylation.tsv`
**Explanation:** Analyze epigenomic modifications
