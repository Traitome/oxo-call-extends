---
name: aquila_stlfr
category: variant-calling
description: Diploid assembly and variants calling for stLFR and hybrid assembler for both linked-reads.
tags: [aquila_stlfr, variant-calling]
author: oxo-call-community
source_url: "https://github.com/maiziex/Aquila_stLFR"
---

## Concepts

- **Tool Overview**: aquila_stlfr (v1.2.11) - Diploid assembly and variants calling for stLFR and hybrid assembler for both linked-reads.
- **Core Function**: Diploid assembly and variants calling for stLFR and hybrid assembler for both linked-reads.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda aquila_stlfr`

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
