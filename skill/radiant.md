---
name: radiant
category: annotation
description: Annotate proteomes with protein domains
tags: ["radiant", "annotation"]
author: oxo-call-community
source_url: "https://domainworld.uni-muenster.de/data/radiant-db/index.html"
---

## Concepts

- **Tool Overview**: Annotate proteomes with protein domains (version 1.1.5)
- **Core Function**: Processes bioinformatics data related to annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda radiant`

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

