---
name: nanomonsv
category: variant-calling
description: Python tools for detecting structural variation from nanopore sequence data.
tags: [nanomonsv, variant-calling, structural-variation, nanopore, sv]
author: oxo-call-community
source_url: "https://github.com/friend1ws/nanomonsv"
---

## Concepts

- **Tool Overview**: nanomonsv v0.9.0 - structural variant detection from Nanopore data.
- **Core Function**: Detects structural variations (deletions, insertions, inversions, etc.) from Nanopore long reads.
- **Input/Output**: Takes aligned BAM files; outputs SV calls in VCF format.
- **Installation**: `conda install -c bioconda nanomonsv`

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
