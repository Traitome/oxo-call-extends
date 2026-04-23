---
name: kleborate
category: annotation
description: Kleborate: a tool for typing and screening pathogen genome assemblies.
tags: [kleborate, annotation]
author: oxo-call-community
source_url: "https://kleborate.readthedocs.io"
---

## Concepts

- **Tool Overview**: kleborate v3.2.4 - Kleborate: a tool for typing and screening pathogen genome assemblies..
- **Core Function**: Kleborate: a tool for typing and screening pathogen genome assemblies.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kleborate`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Screen assemblies
**Args:** `--assembly input.fasta -o results.txt`
**Explanation:** Screens Klebsiella genome assembly for species, MLST, and resistance markers.

