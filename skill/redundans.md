---
name: redundans
category: assembly
description: Redundans is a pipeline that assists an assembly of heterozygous/polymorphic genomes.
tags: ["redundans", "assembly"]
author: oxo-call-community
source_url: "https://github.com/Gabaldonlab/redundans/"
---

## Concepts

- **Tool Overview**: Redundans is a pipeline that assists an assembly of heterozygous/polymorphic genomes. (version 2.01)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda redundans`

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

