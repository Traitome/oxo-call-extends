---
name: ncbi-amr
category: annotation
description: AMRFinder find acquired antimicrobial resistance genes in protein or nucleotide sequences.
tags: [ncbi-amr, annotation, antimicrobial-resistance, amr, bacteria]
author: oxo-call-community
source_url: "https://github.com/ncbi/amr/wiki"
---

## Concepts

- **Tool Overview**: AMRFinder v1.04 - finds acquired antimicrobial resistance genes in sequences.
- **Core Function**: Identifies acquired AMR genes in bacterial protein or nucleotide sequences.
- **Input/Output**: Takes protein or nucleotide FASTA; outputs AMR gene matches.
- **Installation**: `conda install -c bioconda ncbi-amr`

## Pitfalls

- **Version Differences**: Superseded by AMRFinderPlus; consider using ncbi-amrfinderplus.
- **Input Format**: Supports protein and nucleotide FASTA.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fasta -o amr_results.tsv`
**Explanation:** Finds AMR genes in input sequences.
