---
name: bcbio-prioritize
category: variant-calling
description: Prioritize small variants, structural variants and coverage based on biological inputs
tags: [bcbio-prioritize, variant-calling]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbio.prioritize"
---

## Concepts

- **Tool Overview**: bcbio-prioritize (v0.0.8) - Prioritize small variants, structural variants and coverage based on biological inputs
- **Core Function**: Prioritize small variants, structural variants and coverage based on biological inputs
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda bcbio-prioritize`

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
