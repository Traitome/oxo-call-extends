---
name: sansa
category: variant-calling
description: Structural variant annotation
tags: ["sansa", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/dellytools/sansa"
---

## Concepts

- **Tool Overview**: Structural variant annotation (version 0.2.5)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sansa`

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

