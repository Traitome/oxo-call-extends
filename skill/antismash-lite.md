---
name: antismash-lite
category: annotation
description: antiSMASH - the antibiotics and Secondary Metabolite Analysis SHell.
tags: [antismash-lite, annotation]
author: oxo-call-community
source_url: "https://docs.antismash.secondarymetabolites.org"
---

## Concepts

- **Tool Overview**: antismash-lite (v8.0.1) - antiSMASH - the antibiotics and Secondary Metabolite Analysis SHell.
- **Core Function**: antiSMASH allows the rapid genome-wide identification, annotation and analysis of secondary metabolite biosynthesis gene clusters.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda antismash-lite`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o annotation.gff`
**Explanation:** Annotate genomic features
