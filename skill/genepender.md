---
name: genepender
category: variant-calling
description: Annotates overlapping BED-defined regions to variants in a VCF file. Used primarily for providing a gene/exon context to variants (see:bedtarget).
tags: [genepender, variant-calling, VCF, BED]
author: oxo-call-community
source_url: "https://github.com/BioTools-Tek/genepender"
---

## Concepts

- **Tool Overview**: genepender (vv2.6) - Annotates overlapping BED-defined regions to variants in a VCF file. Used primarily for providing a gene/exon context to variants (see:bedtarget).
- **Core Function**: Provides functionality for variant-calling tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda genepender`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
