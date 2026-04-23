---
name: dipcall
category: variant-calling
description: Reference-based variant calling pipeline for phased haplotype assemblies.
tags: [dipcall, variant-calling, haplotype, phased, assembly]
author: oxo-call-community
source_url: "https://github.com/lh3/dipcall"
---

## Concepts

- **Tool Overview**: dipcall v0.3 - Variant calling pipeline for diploid genomes from phased haplotype assemblies.
- **Core Function**: Calls small variants and long indels from phased assembly alignments against a reference.
- **Input/Output**: Expects phased assembly FASTA and reference genome; outputs VCF with variant calls.
- **Installation**: `conda install -c bioconda dipcall`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires phased haplotype assemblies and reference genome.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dipcall -g ref.fa -o output/ hap1.fa hap2.fa`
**Explanation:** Calls variants from phased haplotype assemblies.
