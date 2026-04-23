---
name: dfast
category: annotation
description: DDBJ Fast Annotation and Submission Tool - Prokaryotic genome annotation pipeline.
tags: [dfast, annotation, prokaryote, genome, pipeline]
author: oxo-call-community
source_url: "https://dfast.nig.ac.jp"
---

## Concepts

- **Tool Overview**: DFAST v1.3.9 - Prokaryotic genome annotation and submission pipeline from DDBJ.
- **Core Function**: Annotates prokaryotic genomes with gene predictions, functional assignments, and prepares submission-ready files.
- **Input/Output**: Expects genome FASTA files; outputs annotated genomes in GFF/GBK format and submission files.
- **Installation**: `conda install -c bioconda dfast`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires assembled genome in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dfast --genome assembly.fa --output annotation/`
**Explanation:** Annotates prokaryotic genome and generates submission files.
