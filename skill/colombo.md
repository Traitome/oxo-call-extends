---
name: colombo
category: annotation
description: A software framework equipped with a GUI for the prediction of genomic islands (GIs) in prokaryotes.
tags: [colombo, annotation]
author: oxo-call-community
source_url: "https://www.uni-goettingen.de/en/research/185810.html"
---

## Concepts

- **Tool Overview**: colombo (v4.0) - A software framework equipped with a GUI for the prediction of genomic islands (GIs) in prokaryotes.
- **Core Function**: COLOMBO is a software framework equipped with a GUI for the prediction of genomic islands (GIs) in prokaryotes. It can be equipped with different plugins that actually perform the prediction. The curr...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda colombo`

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
