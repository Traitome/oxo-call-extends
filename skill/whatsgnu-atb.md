---
name: whatsgnu-atb
category: expression
description: WhatsGNU protein allele frequency analysis for AllTheBacteria (2.4M+ genomes)
tags: [whatsgnu-atb, expression]
author: oxo-call-community
source_url: "https://allthebacteria.readthedocs.io/en/latest/whatsgnu.html"
---

## Concepts

- **Tool Overview**: whatsgnu-atb (v1.0.0) - A custom reimplementation of WhatsGNU optimised for AllTheBacteria scale. Builds an LMDB-backed sharded database of protein allele frequencies across 2,438,285 bacterial genomes, and provides fast querying of any bacterial genome to obtain per-protein allele counts and species distributions. Includes a downloader for the pre-built database hosted on OSF.
- **Core Function**: WhatsGNU protein allele frequency analysis for AllTheBacteria (2.4M+ genomes)
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda whatsgnu-atb`

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
