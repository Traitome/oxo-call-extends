---
name: decenttree
category: variant-calling
description: Scalable Neighbour-Joining and related algorithms for phylogenetic inference
tags: [decenttree, variant-calling]
author: oxo-call-community
source_url: "https://github.com/iqtree/decenttree"
---

## Concepts

- **Tool Overview**: decenttree (v1.0.0) - Scalable Neighbour-Joining and related algorithms for phylogenetic inference
- **Core Function**: DecentTree is a fast and memory-efficient implementation of distance-based phylogenetic tree construction methods, including Neighbour-Joining and its variants.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda decenttree`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
