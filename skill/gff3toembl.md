---
name: gff3toembl
category: annotation
description: Submitting annotated genomes to EMBL is a very difficult and time consuming process. This software converts GFF3 files from the most commonly use prokaryote annotation tool Prokka into a format that is suitable for submission to EMBL. It has been used to prepare more than 30% of all annotated genomes in EMBL/GenBank.
tags: [gff3toembl, annotation, GFF]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/gff3toembl/"
---

## Concepts

- **Tool Overview**: gff3toembl (v1.1.4) - Submitting annotated genomes to EMBL is a very difficult and time consuming process. This software converts GFF3 files from the most commonly use prokaryote annotation tool Prokka into a format that is suitable for submission to EMBL. It has been used to prepare more than 30% of all annotated genomes in EMBL/GenBank.
- **Core Function**: Provides functionality for annotation tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda gff3toembl`

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
