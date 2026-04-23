---
name: nanomotif
category: epigenomics
description: Identifying methlyation motifs in nanopore data.
tags: [nanomotif, epigenomics, nanopore, methylation, motif]
author: oxo-call-community
source_url: "https://github.com/MicrobialDarkMatter/nanomotif"
---

## Concepts

- **Tool Overview**: NanoMotif v1.1.2 - identifies methylation motifs in Nanopore data.
- **Core Function**: Discovers and identifies DNA methylation motifs from Nanopore sequencing data.
- **Input/Output**: Takes modified base calls; outputs methylation motifs and their positions.
- **Installation**: `conda install -c bioconda nanomotif`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires modified base calls from Nanopore basecalling.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i modified_bases.tsv -g assembly.fasta -o motifs.tsv`
**Explanation:** Identifies methylation motifs from Nanopore modification calls.
