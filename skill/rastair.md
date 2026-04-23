---
name: rastair
category: variant-calling
description: Fast and flexible extraction of methylation information from BAM files.
tags: ["rastair", "variant-calling", "bam", "bam"]
author: oxo-call-community
source_url: "https://docs.rastair.com"
---

## Concepts

- **Tool Overview**: Fast and flexible extraction of methylation information from BAM files. (version 2.1.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rastair`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Call variants
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Identifies variants from aligned reads.

