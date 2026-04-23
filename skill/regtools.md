---
name: regtools
category: variant-calling
description: Tools that integrate DNA-seq and RNA-seq data to help interpret mutations in a regulatory and splicing context.
tags: ["regtools", "variant-calling"]
author: oxo-call-community
source_url: "https://regtools.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: Tools that integrate DNA-seq and RNA-seq data to help interpret mutations in a regulatory and splicing context. (version 1.0.0)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda regtools`

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

