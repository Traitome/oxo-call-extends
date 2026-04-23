---
name: danbing-tk
category: variant-calling
description: Toolkit for VNTR genotyping and repeat-pan genome graph construction
tags: [danbing-tk, variant-calling]
author: oxo-call-community
source_url: "https://github.com/ChaissonLab/danbing-tk"
---

## Concepts

- **Tool Overview**: danbing-tk (v1.3.2.5) - Toolkit for VNTR genotyping and repeat-pan genome graph construction
- **Core Function**: Toolkit for VNTR genotyping and repeat-pan genome graph construction
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda danbing-tk`

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
