---
name: proksee
category: assembly
description: Proksee is a suite of command line tools for performing assembly, annotation and visualization of microbial genomes.
tags: ["proksee", "assembly"]
author: oxo-call-community
source_url: "https://github.com/proksee-project/proksee-cmd"
---

## Concepts

- **Tool Overview**: Proksee is a suite of command line tools for performing assembly, annotation and visualization of microbial genomes. (version 1.0.0a6)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda proksee`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Run assembly
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assembles reads into contigs/scaffolds.

