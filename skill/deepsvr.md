---
name: deepsvr
category: variant-calling
description: DeepSVR - deep somatic variant refinement using deep learning to classify real somatic and anomalous variants.
tags: [deepsvr, variant-calling, somatic, deep-learning, filtering]
author: oxo-call-community
source_url: "https://github.com/griffithlab/deepsvr"
---

## Concepts

- **Tool Overview**: DeepSVR v0.1.0 - Deep learning tool for classifying somatic variants in paired tumor sequencing data.
- **Core Function**: Distinguishes real somatic variants from sequencing artifacts and germline variants using deep learning.
- **Input/Output**: Expects VCF files with somatic calls; outputs refined variant calls with confidence scores.
- **Installation**: `conda install -c bioconda deepsvr`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires paired tumor-normal VCF files for best results.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepsvr classify --vcf somatic.vcf --output refined.vcf`
**Explanation:** Classifies and filters somatic variants using deep learning.
