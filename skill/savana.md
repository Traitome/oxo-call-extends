---
name: savana
category: variant-calling
description: SAVANA: a somatic structural variant caller for long-read data.
tags: ["savana", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/cortes-ciriano-lab/savana"
---

## Concepts

- **Tool Overview**: SAVANA: a somatic structural variant caller for long-read data. (version 1.3.7)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda savana`

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

