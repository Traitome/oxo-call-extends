---
name: samplot
category: variant-calling
description: Plot structural variant signals from BAMs and CRAMs.
tags: ["samplot", "variant-calling", "bam", "sam", "bam"]
author: oxo-call-community
source_url: "https://github.com/ryanlayer/samplot"
---

## Concepts

- **Tool Overview**: Plot structural variant signals from BAMs and CRAMs. (version 1.3.0)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda samplot`

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

