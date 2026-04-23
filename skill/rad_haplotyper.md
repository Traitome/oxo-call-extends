---
name: rad_haplotyper
category: variant-calling
description: A program for building SNP haplotypes from RAD sequencing data
tags: ["rad_haplotyper", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/chollenbeck/rad_haplotyper"
---

## Concepts

- **Tool Overview**: A program for building SNP haplotypes from RAD sequencing data (version 1.1.9)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rad_haplotyper`

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

