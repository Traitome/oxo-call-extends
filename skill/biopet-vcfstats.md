---
name: biopet-vcfstats
category: variant-calling
description: Vcfstats is a tool that can generate metrics from a vcf file.
tags: [biopet-vcfstats, variant-calling, SAM, VCF]
author: oxo-call-community
source_url: "https://github.com/biopet/vcfstats"
---

## Concepts

- **Tool Overview**: biopet-vcfstats (v1.2) - Vcfstats is a tool that can generate metrics from a vcf file.
- **Core Function**: Vcfstats is a tool that can generate metrics from a vcf file.   - General stats (default, can be disabled)  - Genotype stats (default, can be disabled)  - Sample compare (default, can be disabled)  - ...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda biopet-vcfstats`

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
