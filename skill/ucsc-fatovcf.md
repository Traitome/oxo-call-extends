---
name: ucsc-fatovcf
category: utility
description: UCSC faToVcf - Tool for converting FASTA to VCF format.
tags: [ucsc-fatovcf, ucsc, fasta, vcf, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faToVcf - A tool for converting FASTA sequences to VCF format.
- **Core Function**: Creates VCF file from reference sequences.
- **Input**: FASTA file.
- **Output**: VCF file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, variant analysis, genome comparison.

## Pitfalls

- **Chromosome Names**: Requires matching chromosome names.
- **Memory**: May require significant memory for large sequences.

## Examples

### Convert to VCF
**Args:** `faToVcf input.fa > output.vcf`
**Explanation:** Convert FASTA to VCF format.

### With options
**Args:** `faToVcf -ref=hg38 input.fa > output.vcf`
**Explanation:** Convert with reference specification.
