---
name: rvtests
category: variant-calling
description: Rare variant test software for next generation sequencing data
tags: ["rvtests", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/zhanxw/rvtests"
---

## Concepts

- **Tool Overview**: Rare variant test software for next generation sequencing data (version 2.0.7)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rvtests`

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

