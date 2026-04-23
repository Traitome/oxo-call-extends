---
name: gffread
category: qc
description: GFF/GTF utility providing format conversions, region filtering, FASTA sequence extraction and more.
tags: [gffread, qc, FASTA, GFF, GTF]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/stringtie/gff.shtml#gffread"
---

## Concepts

- **Tool Overview**: gffread (v0.12.9) - GFF/GTF utility providing format conversions, region filtering, FASTA sequence extraction and more.
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda gffread`

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
