---
name: mutamr
category: variant-calling
description: Stripped down tool for generation of annotated vcf from paired-end reads in a CPHL.
tags: [mutamr, variant-calling, vcf, annotation, paired-end]
author: oxo-call-community
source_url: "https://github.com/MDU-PHL/mutamr"
---

## Concepts

- **Tool Overview**: MutAMR v0.0.2 - generates annotated VCF from paired-end reads.
- **Core Function**: Produces annotated variant call files from paired-end sequencing data.
- **Input/Output**: Takes paired-end FASTQ or BAM files; outputs annotated VCF.
- **Installation**: `conda install -c bioconda mutamr`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct paired-end read format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-1 reads_R1.fastq -2 reads_R2.fastq -r reference.fasta -o output.vcf`
**Explanation:** Generates annotated VCF from paired-end reads against a reference.
