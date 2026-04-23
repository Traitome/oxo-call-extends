---
name: pymochi
category: variant-calling
description: Neural networks to quantify energies, energetic couplings, epistasis and allostery from deep mutational scanning data
tags: ["pymochi", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/lehner-lab/MoCHI"
---

## Concepts

- **Tool Overview**: Neural networks to quantify energies, energetic couplings, epistasis and allostery from deep mutational scanning data (version 1.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pymochi`

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

