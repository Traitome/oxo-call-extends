---
name: recombass
category: variant-calling
description: Detect recombination hot/cold spots from SNP matrices using wavelet denoising
tags: ["recombass", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/xyfans111/recombass"
---

## Concepts

- **Tool Overview**: Detect recombination hot/cold spots from SNP matrices using wavelet denoising (version 0.1.7)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda recombass`

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

