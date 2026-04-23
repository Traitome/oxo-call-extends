---
name: pyrad
category: assembly
description: Assembly and analysis of RADseq data sets
tags: ["pyrad", "assembly"]
author: oxo-call-community
source_url: "https://github.com/dereneaton/pyrad"
---

## Concepts

- **Tool Overview**: Assembly and analysis of RADseq data sets (version 3.0.66)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pyrad`

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

