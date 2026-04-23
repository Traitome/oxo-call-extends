---
name: nanovar
category: variant-calling
description: Structural variant caller using low-depth long reads
tags: [nanovar, variant-calling, structural-variation, nanopore, low-depth]
author: oxo-call-community
source_url: "https://github.com/cytham/nanovar"
---

## Concepts

- **Tool Overview**: NanoVar v1.8.3 - structural variant caller for low-depth long reads.
- **Core Function**: Detects structural variants from low-coverage Nanopore or other long-read data.
- **Input/Output**: Takes aligned BAM files; outputs SV calls in VCF format.
- **Installation**: `conda install -c bioconda nanovar`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires aligned BAM from long-read aligners.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Detects structural variants from low-depth long reads.
