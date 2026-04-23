---
name: shigeifinder
category: assembly
description: Cluster informed Shigella and EIEC serotyping tool from Illumina reads and assemblies
tags: [shigeifinder, assembly]
author: oxo-call-community
source_url: "https://github.com/LanLab/ShigEiFinder"
---

## Concepts

- **Tool Overview**: shigeifinder (v1.3.5) - Cluster informed Shigella and EIEC serotyping tool from Illumina reads and assemblies
- **Core Function**: Cluster informed Shigella and EIEC serotyping tool from Illumina reads and assemblies
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shigeifinder`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shigeifinder -i <reads.fastq> -o <output_dir>`
**Explanation:** Run shigeifinder with typical input and output options.
