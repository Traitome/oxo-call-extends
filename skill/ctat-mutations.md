---
name: ctat-mutations
category: variant-calling
description: Mutation detection in RNA-Seq using GATK-v4.0 in RNA-Seq variant calling, several sources of variant annotation, and filtering based on CRAVAT.
tags: [ctat-mutations, variant-calling]
author: oxo-call-community
source_url: "https://github.com/NCIP/ctat-mutations"
---

## Concepts

- **Tool Overview**: ctat-mutations (v2.1.0) - Mutation detection in RNA-Seq using GATK-v4.0 in RNA-Seq variant calling, several sources of variant annotation, and filtering based on CRAVAT.
- **Core Function**: Mutation detection in RNA-Seq using GATK-v4.0 in RNA-Seq variant calling, several sources of variant annotation, and filtering based on CRAVAT.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ctat-mutations`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
