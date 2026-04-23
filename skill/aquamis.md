---
name: aquamis
category: assembly
description: AQUAMIS is a snakemake pipeline for routine assembly and quality assessment of microbial isolate sequencing experiments.
tags: [aquamis, assembly]
author: oxo-call-community
source_url: "https://gitlab.com/bfr_bioinformatics/AQUAMIS"
---

## Concepts

- **Tool Overview**: aquamis (v1.4.0) - AQUAMIS is a snakemake pipeline for routine assembly and quality assessment of microbial isolate sequencing experiments.
- **Core Function**: AQUAMIS is a snakemake pipeline for routine assembly and quality assessment of microbial isolate sequencing experiments.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda aquamis`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
