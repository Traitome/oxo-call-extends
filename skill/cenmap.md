---
name: cenmap
category: alignment
description: A centromere mapping and annotation pipeline for T2T human and primate genome assemblies implemented in Snakemake.
tags: [cenmap, alignment]
author: oxo-call-community
source_url: "https://github.com/logsdon-lab/CenMAP/blob/v1.2.0/README.md"
---

## Concepts

- **Tool Overview**: cenmap (v1.2.0) - A centromere mapping and annotation pipeline for T2T human and primate genome assemblies implemented in Snakemake.
- **Core Function**: A centromere mapping and annotation pipeline for T2T human and primate genome assemblies implemented in Snakemake.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cenmap`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
