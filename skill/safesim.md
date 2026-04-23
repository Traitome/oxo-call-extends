---
name: safesim
category: variant-calling
description: SafeSeqS variant simulator
tags: ["safesim", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/genetronhealth/safesim"
---

## Concepts

- **Tool Overview**: SafeSeqS variant simulator (version 0.1.6.8d44580)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda safesim`

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

