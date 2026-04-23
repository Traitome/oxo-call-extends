---
name: rjchallis-assembly-stats
category: assembly
description: Assembly metric visualisations to facilitate rapid assessment and comparison of assembly quality.
tags: ["rjchallis-assembly-stats", "assembly"]
author: oxo-call-community
source_url: "https://github.com/rjchallis/assembly-stats"
---

## Concepts

- **Tool Overview**: Assembly metric visualisations to facilitate rapid assessment and comparison of assembly quality. (version 17.02)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rjchallis-assembly-stats`

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

