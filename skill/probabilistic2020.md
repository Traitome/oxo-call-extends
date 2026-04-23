---
name: probabilistic2020
category: variant-calling
description: Simulates somatic mutations, and calls statistically significant oncogenes and tumor suppressor genes based on a randomization-based test
tags: ["probabilistic2020", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/KarchinLab/probabilistic2020"
---

## Concepts

- **Tool Overview**: Simulates somatic mutations, and calls statistically significant oncogenes and tumor suppressor genes based on a randomization-based test (version 1.2.3)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda probabilistic2020`

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

