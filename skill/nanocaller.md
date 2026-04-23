---
name: nanocaller
category: variant-calling
description: NanoCaller for accurate detection of SNPs and indels in difficult-to-map regions from long-read sequencing.
tags: [nanocaller, variant-calling, nanopore, snp, indel]
author: oxo-call-community
source_url: "https://github.com/WGLab/NanoCaller"
---

## Concepts

- **Tool Overview**: NanoCaller v3.6.2 - variant caller for long-read sequencing data.
- **Core Function**: Detects SNPs and indels in difficult-to-map regions from Nanopore/PacBio long reads.
- **Input/Output**: Takes aligned BAM files; outputs VCF with variant calls.
- **Installation**: `conda install -c bioconda nanocaller`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires aligned BAM from long-read aligners.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-b aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls SNPs and indels from long-read alignments.
