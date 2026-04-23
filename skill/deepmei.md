---
name: deepmei
category: variant-calling
description: A tool to detect mobile elements insertion.
tags: [deepmei, variant-calling, transposon, insertion, deep-learning]
author: oxo-call-community
source_url: "https://github.com/Kanglu123/deepmei/tree/deepmei-v1.6.24"
---

## Concepts

- **Tool Overview**: DeepMEI v1.6.24 - Deep learning tool for detecting mobile element insertions (MEI) in genomic data.
- **Core Function**: Identifies mobile element insertion events using deep learning from sequencing data.
- **Input/Output**: Expects BAM/CRAM alignment files; outputs VCF with MEI calls.
- **Installation**: `conda install -c bioconda deepmei`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly aligned BAM/CRAM files with index.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepmei --bam input.bam --reference ref.fa --output mei_calls.vcf`
**Explanation:** Detects mobile element insertions from aligned reads.
