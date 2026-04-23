---
name: aquila
category: variant-calling
description: Diploid personal genome assembly and comprehensive variant detection based on linked-reads
tags: [aquila, variant-calling]
author: oxo-call-community
source_url: "https://github.com/maiziex/Aquila"
---

## Concepts

- **Tool Overview**: aquila (v1.0.0) - Diploid personal genome assembly and comprehensive variant detection based on linked-reads
- **Core Function**: Diploid personal genome assembly and comprehensive variant detection based on linked-reads
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda aquila`

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
