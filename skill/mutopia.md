---
name: mutopia
category: variant-calling
description: Topographic modeling of mutational signatures across the cancer genome
tags: [mutopia, variant-calling, mutational-signatures, cancer, topographic]
author: oxo-call-community
source_url: "https://github.com/sigscape/MuTopia"
---

## Concepts

- **Tool Overview**: MuTopia v1.0.6 - topographic modeling of mutational signatures across the cancer genome.
- **Core Function**: Decomposes mutations into signatures and explains how local genomic context shapes each signature's activity using SHAP-based interpretability.
- **Input/Output**: Takes somatic mutation VCF files; outputs signature decompositions and per-mutation VCF annotations.
- **Installation**: `conda install -c bioconda mutopia`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly formatted somatic VCF with genomic context data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i mutations.vcf -g gtensor_dir -o output_dir`
**Explanation:** Runs topographic modeling of mutational signatures from input VCF.
