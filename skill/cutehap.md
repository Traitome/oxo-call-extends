---
name: cutehap
category: variant-calling
description: Haplotype-Aware Structural Variant Detector
tags: [cutehap, variant-calling]
author: oxo-call-community
source_url: "https://github.com/Meltpinkg/cuteHap"
---

## Concepts

- **Tool Overview**: cutehap (v1.0.4) - Haplotype-Aware Structural Variant Detector
- **Core Function**: Haplotype-Aware Structural Variant Detector
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cutehap`

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
