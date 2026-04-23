---
name: diphase
category: variant-calling
description: A diploid genome phasing tool.
tags: [diphase, variant-calling, phasing, diploid, haplotype]
author: oxo-call-community
source_url: "https://github.com/zhangjuncsu/Diphase"
---

## Concepts

- **Tool Overview**: Diphase v1.0.3 - Tool for phasing diploid genome assemblies.
- **Core Function**: Separates haplotype phases in diploid genome assemblies using variant information.
- **Input/Output**: Expects assembly FASTA and variant calls; outputs phased haplotype sequences.
- **Installation**: `conda install -c bioconda diphase`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires diploid assembly and variant information.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `diphase --assembly diploid.fa --variants variants.vcf --output phased/`
**Explanation:** Phases diploid genome assembly into haplotypes.
