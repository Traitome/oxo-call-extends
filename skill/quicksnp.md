---
name: quicksnp
category: variant-calling
description: A python script to quickly build a Neighbor Joining tree using only a SNP distance matrix.
tags: ["quicksnp", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/k-florek/QuickSNP"
---

## Concepts

- **Tool Overview**: A python script to quickly build a Neighbor Joining tree using only a SNP distance matrix. (version 1.0.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda quicksnp`

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

