---
name: diting
category: metagenomics
description: DiTing - A Snakemake pipeline to infer and compare biogeochemical pathways in metagenomic data.
tags: [diting, metagenomics, pathways, biogeochemical, snakemake]
author: oxo-call-community
source_url: "https://github.com/SilentGene/DiTing"
---

## Concepts

- **Tool Overview**: DiTing v2.0.2 - Snakemake-based pipeline for inferring biogeochemical pathways from metagenomic data.
- **Core Function**: Identifies and compares metabolic pathways and biogeochemical cycles in metagenomic samples.
- **Input/Output**: Expects metagenomic assemblies and annotations; outputs pathway abundance and comparison results.
- **Installation**: `conda install -c bioconda diting`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires assembled contigs and gene annotations.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `diting run --config config.yaml --output results/`
**Explanation:** Runs biogeochemical pathway analysis pipeline.
