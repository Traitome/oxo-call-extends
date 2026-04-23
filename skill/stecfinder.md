---
name: stecfinder
category: assembly
description: Cluster informed Shigatoxin producing E. coli (STEC) serotyping tool from Illumina reads and assemblies
tags: [stecfinder, assembly]
author: oxo-call-community
source_url: "https://github.com/LanLab/STECFinder"
---

## Concepts

- **Tool Overview**: stecfinder (v1.1.2) - Cluster informed Shigatoxin producing E. coli (STEC) serotyping tool from Illumina reads and assemblies
- **Core Function**: Cluster informed Shigatoxin producing E. coli (STEC) serotyping tool from Illumina reads and assemblies
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stecfinder`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stecfinder -i <reads.fastq> -o <output_dir>`
**Explanation:** Run stecfinder with typical input and output options.
