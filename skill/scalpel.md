---
name: scalpel
category: variant-calling
description: Sensitive detection of INDELs (INsertions and DELetions).
tags: ["scalpel", "variant-calling"]
author: oxo-call-community
source_url: "https://scalpel.sourceforge.net"
---

## Concepts

- **Tool Overview**: Sensitive detection of INDELs (INsertions and DELetions). (version 0.5.4)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda scalpel`

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

