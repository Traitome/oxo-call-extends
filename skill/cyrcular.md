---
name: cyrcular
category: variant-calling
description: Tool for calling circles from nanopore reads
tags: [cyrcular, variant-calling]
author: oxo-call-community
source_url: "https://github.com/tedil/cyrcular"
---

## Concepts

- **Tool Overview**: cyrcular (v0.3.0) - Tool for calling circles from nanopore reads
- **Core Function**: Tool for calling circles from nanopore reads
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cyrcular`

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
