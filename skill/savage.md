---
name: savage
category: assembly
description: SAVAGE (Strain Aware VirAl GEnome assembly) reconstructs individual (viral) haplotypes from a mixed sample.
tags: ["savage", "assembly", "sam"]
author: oxo-call-community
source_url: "https://github.com/HaploConduct/HaploConduct/tree/master/savage"
---

## Concepts

- **Tool Overview**: SAVAGE (Strain Aware VirAl GEnome assembly) reconstructs individual (viral) haplotypes from a mixed sample. (version 0.4.2)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda savage`

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

