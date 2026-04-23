---
name: nanosv
category: variant-calling
description: Structural variation detection tool for Oxford Nanopore data.
tags: [nanosv, variant-calling, structural-variation, nanopore, sv]
author: oxo-call-community
source_url: "https://github.com/mroosmalen/nanosv"
---

## Concepts

- **Tool Overview**: NanoSV v1.2.4 - structural variation detection for Oxford Nanopore data.
- **Core Function**: Detects structural variants from Nanopore long-read alignments.
- **Input/Output**: Takes aligned BAM files; outputs SV calls in VCF format.
- **Installation**: `conda install -c bioconda nanosv`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires aligned BAM from Nanopore reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-b aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Detects structural variants from Nanopore alignments.
