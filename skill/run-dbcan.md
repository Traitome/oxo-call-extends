---
name: run-dbcan
category: annotation
description: Standalone version of dbCAN annotation tool for automated CAZyme annotation
tags: ["run-dbcan", "annotation"]
author: oxo-call-community
source_url: "https://github.com/linnabrown/run_dbcan"
---

## Concepts

- **Tool Overview**: Standalone version of dbCAN annotation tool for automated CAZyme annotation (version 2.0.11)
- **Core Function**: Processes bioinformatics data related to annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda run-dbcan`

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

