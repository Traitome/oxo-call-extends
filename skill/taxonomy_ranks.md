---
name: taxonomy_ranks
category: metagenomics
description: To get taxonomy ranks information for taxid, species name, or higher ranks (e.g., genus, family) with ETE3 from NCBI Taxonomy database.
tags: [taxonomy_ranks, metagenomics]
author: oxo-call-community
source_url: "https://github.com/linzhi2013/taxonomy_ranks"
---

## Concepts

- **Tool Overview**: taxonomy_ranks (v0.0.10) - To get taxonomy ranks information for taxid, species name, or higher ranks (e.g., genus, family) with ETE3 from NCBI Taxonomy database.
- **Core Function**: To get taxonomy ranks information for taxid, species name, or higher ranks (e.g., genus, family) with ETE3 from NCBI Taxonomy database.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxonomy_ranks`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxonomy_ranks -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run taxonomy_ranks with typical input and output options.
