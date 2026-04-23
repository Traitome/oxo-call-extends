---
name: metabat2
category: metagenomics
description: Metagenome binning.
tags: [metabat2, metagenomics]
author: oxo-call-community
source_url: "https://bitbucket.org/berkeleylab/metabat"
---

## Concepts

- **Tool Overview**: metabat2 v2.18 - Metagenome binning..
- **Core Function**: Metagenome binning.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda metabat2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Bin contigs
**Args:** `metabat2 -i assembly.fa -a depth.txt -o bins/bin`
**Explanation:** Bins metagenomic contigs into MAGs using depth information.

