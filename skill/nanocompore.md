---
name: nanocompore
category: epigenomics
description: Nanocompore identifies raw signal changes between two conditions dRNA-Seq data.
tags: [nanocompore, epigenomics, nanopore, rna-modification, signal]
author: oxo-call-community
source_url: "https://github.com/tleonardi/nanocompore"
---

## Concepts

- **Tool Overview**: Nanocompore v1.0.4 - identifies raw signal changes in direct RNA-Seq data.
- **Core Function**: Detects RNA modifications by comparing raw signal between two conditions in dRNA-Seq.
- **Input/Output**: Takes eventalign data from Nanopolish; outputs modification sites.
- **Installation**: `conda install -c bioconda nanocompore`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires eventalign output from Nanopolish.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i sample1_eventalign.tsv -c control_eventalign.tsv -o output_dir`
**Explanation:** Identifies signal changes between sample and control conditions.
