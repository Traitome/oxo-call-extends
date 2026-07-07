---
name: ctxcore
category: utility
description: Core functions for pycisTarget and the SCENIC tool suite.
tags: [ctxcore, utility, SCENIC, pycisTarget, gene-regulatory-network, transcription-factors]
author: oxo-call-community
source_url: "https://ctxcore.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: ctxcore (v0.2.0+) provides core functions for pycisTarget and the SCENIC tool suite for gene regulatory network analysis.
- **Core Function**: Implements motif discovery, transcription factor binding analysis, and gene regulatory network inference.
- **Input/Output**: Input: Gene expression matrices, genomic regions, motif databases. Output: Regulatory networks, TF-target gene relationships.
- **SCENIC Integration**: Part of the SCENIC pipeline for single-cell regulatory network inference.
- **Key Features**: Motif enrichment analysis, cis-regulatory module identification, transcription factor footprinting.
- **Installation**: `conda install -c bioconda ctxcore`

## Pitfalls

- **Memory Requirements**: Large expression matrices may require significant memory; consider downsampling.
- **Motif Databases**: Requires motif databases in specific format; use `ctxcore download` to fetch.
- **Version Compatibility**: Ensure compatibility with SCENIC pipeline version.
- **Annotation Dependencies**: Requires gene annotations matching expression data.
- **Computational Time**: Motif enrichment analysis can be time-consuming for large datasets.

## Examples

### Load motif database
**Args:** `ctxcore motifs download --species hg38 --output motifs/`
**Explanation:** Download motif databases for human genome.

### Run motif enrichment
**Args:** `ctxcore enrichment -i peaks.bed -m motifs/ -o enrichment.tsv`
**Explanation:** Perform motif enrichment analysis on genomic peaks.

### Identify regulatory modules
**Args:** `ctxcore modules -i expression.csv -o modules.tsv --tf-list tfs.txt`
**Explanation:** Identify cis-regulatory modules from gene expression data.
