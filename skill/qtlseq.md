---
name: qtlseq
category: variant-calling
description: QTL-seq: pipeline to identify causative mutations responsible for a phenotype.
tags: ["qtlseq", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/YuSugihara/QTL-seq"
---

## Concepts

- **Tool Overview**: QTL-seq: pipeline to identify causative mutations responsible for a phenotype. (version 2.3.0)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qtlseq`

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

