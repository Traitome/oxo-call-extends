---
name: scapp
category: assembly
description: Plasmid assembly in metagenomes
tags: ["scapp", "assembly"]
author: oxo-call-community
source_url: "https://github.com/Shamir-Lab/SCAPP"
---

## Concepts

- **Tool Overview**: Plasmid assembly in metagenomes (version 0.1.4)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda scapp`

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

