---
name: scaffold_builder
category: assembly
description: Scaffold_builder: Combining de novo and reference-guided assembly with Scaffold_builder.
tags: ["scaffold_builder", "assembly"]
author: oxo-call-community
source_url: "http://edwards.sdsu.edu/scaffold_builder"
---

## Concepts

- **Tool Overview**: Scaffold_builder: Combining de novo and reference-guided assembly with Scaffold_builder. (version 2.3)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda scaffold_builder`

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

