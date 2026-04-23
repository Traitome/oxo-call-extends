---
name: pyclone
category: variant-calling
description: PyClone: A probabilistic model for inferring clonal population structure from deep NGS sequencing.
tags: ["pyclone", "variant-calling", "sam"]
author: oxo-call-community
source_url: "https://github.com/Roth-Lab/pyclone/"
---

## Concepts

- **Tool Overview**: PyClone: A probabilistic model for inferring clonal population structure from deep NGS sequencing. (version 0.13.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pyclone`

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

