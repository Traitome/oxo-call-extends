---
name: tritimap
category: alignment
description: Triti-Map is a Snakemake-based pipeline for gene mapping in Triticeae.
tags: [tritimap, alignment]
author: oxo-call-community
source_url: "https://github.com/fei0810/Triti-Map/wiki"
---

## Concepts

- **Tool Overview**: tritimap (v0.9.7) - Triti-Map is a Snakemake-based pipeline for gene mapping in Triticeae, which contains a suite of user-friendly computational packages and web-interface integrating multi-omics data from Triticeae species including genomic, epigenomic, evolutionary and homologous information.  Triti-Map could efficiently explore trait-related genes or functional elements not present in the reference genome and reduce the time and labor required for gene mapping in large genome species.
- **Core Function**: Triti-Map is a Snakemake-based pipeline for gene mapping in Triticeae.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda tritimap`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
