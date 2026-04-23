---
name: delve-bio
category: variant-calling
description: A variant caller for mixed infections.
tags: [delve-bio, variant-calling, mixed-infection, haplotype]
author: oxo-call-community
source_url: "https://github.com/berndbohmeier/delve"
---

## Concepts

- **Tool Overview**: DELVE v0.2.0 - Variant caller designed for detecting variants in mixed infection samples.
- **Core Function**: Calls variants in samples containing multiple strains or haplotypes, common in pathogen infections.
- **Input/Output**: Expects BAM files and reference genome; outputs VCF with variant calls including strain-specific variants.
- **Installation**: `conda install -c bioconda delve-bio`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly aligned BAM files with adequate coverage for strain detection.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `delve call --bam sample.bam --ref ref.fa --output variants.vcf`
**Explanation:** Calls variants from mixed infection sample.
