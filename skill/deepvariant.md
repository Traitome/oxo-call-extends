---
name: deepvariant
category: variant-calling
description: DeepVariant is an analysis pipeline that uses a deep neural network to call genetic variants from next-generation DNA sequencing data.
tags: [deepvariant, variant-calling, deep-learning, snp, indel]
author: oxo-call-community
source_url: "https://github.com/google/deepvariant"
---

## Concepts

- **Tool Overview**: DeepVariant v1.10.0 - Google's deep learning-based variant caller for NGS data, achieving high accuracy across multiple sequencing platforms.
- **Core Function**: Calls SNPs and indels using a convolutional neural network trained on real data, treating variant calling as an image classification problem.
- **Input/Output**: Expects BAM/CRAM files and reference genome; outputs VCF with variant calls.
- **Installation**: `conda install -c bioconda deepvariant`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly aligned BAM/CRAM with index and reference genome.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepvariant --model_type WGS --ref ref.fa --reads sample.bam --output_vcf sample.vcf`
**Explanation:** Calls variants from WGS BAM file using the WGS model.
