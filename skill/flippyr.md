---
name: flippyr
category: formatting
description: This package is designed to align a PLINK fileset with a FASTA reference genome.
tags: [flippyr, formatting]
author: oxo-call-community
source_url: "https://github.com/BEFH/flippyr"
---

## Concepts
- **Tool Overview**: Flippy is a simple, fast script to ensure that PLINK filesets are aligned to a reference genome in FASTA format. It identifies and fixes strand flipping, and reversed alleles. It removes ambiguous (palindromic) alleles and sites that do not match the reference genome. It also recognizes and removes multi- allelic sites and indels by default. Instructions and more details can be found on GitHub.
- **Core Function**: This package is designed to align a PLINK fileset with a FASTA reference genome.
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda flippyr`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
