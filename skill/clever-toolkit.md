---
name: clever-toolkit
category: variant-calling
description: The CLEVER Toolkit.
tags: [clever-toolkit, variant-calling]
author: oxo-call-community
source_url: "https://bitbucket.org/tobiasmarschall/clever-toolkit/wiki/Home"
---

## Concepts

- **Tool Overview**: clever-toolkit (v2.4) - The CLEVER Toolkit.
- **Core Function**: CTK is a suite of tools to analyze next-generation sequencing data and, in particular, to discover and genotype insertions and deletions from paired-end reads.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda clever-toolkit`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
