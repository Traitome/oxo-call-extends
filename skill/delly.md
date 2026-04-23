---
name: delly
category: variant-calling
description: Structural variant discovery by integrated paired-end and split-read analysis.
tags: [delly, variant-calling, structural-variants, sv, indel]
author: oxo-call-community
source_url: "https://github.com/dellytools/delly"
---

## Concepts

- **Tool Overview**: Delly - Structural variant caller using paired-end and split-read analysis for detecting deletions, duplications, inversions, and translocations.
- **Core Function**: Discovers structural variants (SVs) from paired-end sequencing data using split-read and read-pair signatures.
- **Input/Output**: Expects BAM files and reference genome; outputs VCF with SV calls.
- **Installation**: `conda install -c bioconda delly`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly aligned BAM files with index.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `delly call -g ref.fa -o svs.vcf sample.bam`
**Explanation:** Calls structural variants from aligned reads.
