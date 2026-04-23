---
name: snvphyl-tools
category: population-genomics
description: The SNVPhyl (Single Nucleotide Variant PHYLogenomics) pipeline is a pipeline for identifying Single Nucleotide Variants (SNV) within a collection of microbial genomes and constructing a phylogenetic tree
tags: [snvphyl-tools, population-genomics]
author: oxo-call-community
source_url: "https://github.com/phac-nml/snvphyl-tools"
---

## Concepts

- **Tool Overview**: snvphyl-tools (v1.8.2) - The SNVPhyl (Single Nucleotide Variant PHYLogenomics) pipeline is a pipeline for identifying Single Nucleotide Variants (SNV) within a collection of microbial genomes and constructing a phylogenetic tree
- **Core Function**: The SNVPhyl (Single Nucleotide Variant PHYLogenomics) pipeline is a pipeline for identifying Single Nucleotide Variants (SNV) within a collection of microbial genomes and constructing a phylogenetic tree
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snvphyl-tools`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snvphyl-tools -i <input.vcf> -o <output_dir>`
**Explanation:** Run snvphyl-tools with typical input and output options.
