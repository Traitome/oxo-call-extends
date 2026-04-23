---
name: quickmerge
category: assembly
description: Quickmerge uses a simple concept to improve contiguity of genome assemblies based on long molecule sequences.
tags: ["quickmerge", "assembly"]
author: oxo-call-community
source_url: "https://github.com/mahulchak/quickmerge"
---

## Concepts

- **Tool Overview**: Quickmerge uses a simple concept to improve contiguity of genome assemblies based on long molecule sequences. (version 0.3)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda quickmerge`

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

