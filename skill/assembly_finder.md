---
name: assembly_finder
category: assembly
description: Snakemake-powered cli pipeline to download genomes with NCBI datasets
tags: [assembly_finder, assembly]
author: oxo-call-community
source_url: "https://metagenlab.github.io/assembly_finder"
---

## Concepts

- **Tool Overview**: assembly_finder (v0.9.0) - Snakemake-powered cli pipeline to download genomes with NCBI datasets
- **Core Function**: Snakemake-powered cli pipeline to download genomes with NCBI datasets
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda assembly_finder`

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
