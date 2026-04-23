---
name: demuxem
category: expression
description: DemuxEM is the demultiplexing module of Pegasus for cell-hashing and nucleus-hashing genomics data.
tags: [demuxem, expression, demultiplexing, single-cell, cell-hashing]
author: oxo-call-community
source_url: "https://github.com/lilab-bcb/demuxEM"
---

## Concepts

- **Tool Overview**: DemuxEM v0.1.8 - Demultiplexing tool for single-cell cell-hashing and nucleus-hashing data, part of the Pegasus ecosystem.
- **Core Function**: Assigns cell barcodes to sample identities using hashtag oligonucleotide (HTO) data from cell-hashing experiments.
- **Input/Output**: Expects gene expression and HTO count matrices; outputs cell-to-sample assignments.
- **Installation**: `conda install -c bioconda demuxem`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires paired gene expression and HTO count data from cell-hashing experiments.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `demuxem demux --rna rna.h5 --hto hto.h5 --output assignments.tsv`
**Explanation:** Demultiplexes cells using gene expression and HTO data.
