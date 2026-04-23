---
name: salsa2
category: assembly
description: Salsa is a tool to scaffold long read assemblies with Hi-C.
tags: ["salsa2", "assembly"]
author: oxo-call-community
source_url: "https://github.com/marbl/SALSA"
---

## Concepts

- **Tool Overview**: Salsa is a tool to scaffold long read assemblies with Hi-C. (version 2.3)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda salsa2`

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

