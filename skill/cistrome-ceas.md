---
name: cistrome-ceas
category: annotation
description: Cistrome-CEAS -- Cis-regulatory Element Annotation System
tags: [cistrome-ceas, annotation]
author: oxo-call-community
source_url: "http://liulab.dfci.harvard.edu/CEAS/"
---

## Concepts

- **Tool Overview**: cistrome-ceas (v1.0.2b1) - Cistrome-CEAS -- Cis-regulatory Element Annotation System
- **Core Function**: Tool to characterize genome-wide protein-DNA interaction patterns from ChIP-chip and ChIP-Seq of both sharp and broad binding factors
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda cistrome-ceas`

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
