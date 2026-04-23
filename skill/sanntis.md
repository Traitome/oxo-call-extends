---
name: sanntis
category: annotation
description: SMBGC Annotation using Neural Networks Trained on Interpro Signatures.
tags: ["sanntis", "annotation"]
author: oxo-call-community
source_url: "https://github.com/Finn-Lab/SanntiS"
---

## Concepts

- **Tool Overview**: SMBGC Annotation using Neural Networks Trained on Interpro Signatures. (version 0.9.4.1)
- **Core Function**: Processes bioinformatics data related to annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sanntis`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Annotate features
**Args:** `-i genome.fasta -o annotation.gff`
**Explanation:** Predicts and annotates genomic features.

