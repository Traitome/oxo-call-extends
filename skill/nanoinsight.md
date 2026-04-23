---
name: nanoinsight
category: annotation
description: Repeat annotation tool for insertions called by NanoVar
tags: [nanoinsight, annotation, insertion, repeat, nanopore]
author: oxo-call-community
source_url: "https://github.com/AsmaaSamyMohamedMahmoud/nanoinsight"
---

## Concepts

- **Tool Overview**: NanoInsight v0.0.3 - repeat annotation for NanoVar insertions.
- **Core Function**: Annotates repeat elements in insertions called by NanoVar from Nanopore data.
- **Input/Output**: Takes NanoVar VCF output; outputs annotated insertions with repeat information.
- **Installation**: `conda install -c bioconda nanoinsight`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires NanoVar output format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i nanovar_variants.vcf -r reference.fasta -o annotated.tsv`
**Explanation:** Annotates repeat elements in NanoVar insertions.
