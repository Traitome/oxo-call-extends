---
name: alphafetcher
category: annotation
description: Interface with the AlphaFold Protein Structure Database.
tags: [alphafetcher, annotation]
author: oxo-call-community
source_url: "https://bitbucket.org/bio2byte/alphafetcher/"
---

## Concepts

- **Tool Overview**: alphafetcher (v0.2.0) - Interface with the AlphaFold Protein Structure Database.
- **Core Function**: Interface with the AlphaFold Protein Structure Database.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda alphafetcher`

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
