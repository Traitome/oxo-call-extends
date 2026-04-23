---
name: cassiopee
category: annotation
description: scan an input genomic sequence (dna/rna/protein) and search for a subsequence with exact match or allowing substitutions (Hamming distance) and/or insertion/deletions
tags: [cassiopee, annotation]
author: oxo-call-community
source_url: "https://github.com/osallou/cassiopee-c"
---

## Concepts

- **Tool Overview**: cassiopee (v1.0.9) - scan an input genomic sequence (dna/rna/protein) and search for a subsequence with exact match or allowing substitutions (Hamming distance) and/or insertion/deletions
- **Core Function**: scan an input genomic sequence (dna/rna/protein) and search for a subsequence with exact match or allowing substitutions (Hamming distance) and/or insertion/deletions
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cassiopee`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o annotation.gff`
**Explanation:** Annotate genomic features
