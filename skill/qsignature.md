---
name: qsignature
category: variant-calling
description: qsignature is a simple and highly effective method for detecting potential sample mix-ups using distance measurements between SNP
tags: ["qsignature", "variant-calling", "sam"]
author: oxo-call-community
source_url: "http://sourceforge.net/p/adamajava/wiki/Home/"
---

## Concepts

- **Tool Overview**: qsignature is a simple and highly effective method for detecting potential sample mix-ups using distance measurements between SNP (version 0.1pre)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qsignature`

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

