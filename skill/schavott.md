---
name: schavott
category: assembly
description: Assembly and scaffolding of bacterial genomes in real time using MinION-sequencing.
tags: ["schavott", "assembly"]
author: oxo-call-community
source_url: "http://github.com/emilhaegglund/schavott"
---

## Concepts

- **Tool Overview**: Assembly and scaffolding of bacterial genomes in real time using MinION-sequencing. (version 0.5.0)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda schavott`

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

