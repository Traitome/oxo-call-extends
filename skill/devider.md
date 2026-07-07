---
name: devider
category: variant-calling
description: devider - haplotyping heterogeneous samples using SNP-encoded positional de Bruijn graphs.
tags: [devider, variant-calling, haplotyping, long-read, de-bruijn]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/devider"
---

## Concepts

- **Tool Overview**: devider (v0.0.1+) is a haplotyping tool for heterogeneous long-read sequencing samples using SNP-encoded positional de Bruijn graphs.
- **Core Function**: Reconstructs individual haplotypes from mixed population samples by leveraging SNP positions to build positional de Bruijn graphs.
- **Input/Output**: Input: Long reads (FASTQ/FASTA), variant sites (VCF). Output: Haplotype-resolved sequences, phased variants.
- **Algorithm**: Uses positional de Bruijn graphs encoded with SNP information to resolve haplotypes in heterogeneous samples.
- **Key Features**: Heterogeneous sample analysis, long-read support, SNP-aware assembly, haplotype reconstruction, variant phasing.
- **Installation**: `conda install -c bioconda devider`

## Pitfalls

- **Input Requirements**: Requires long reads with sufficient coverage for haplotype resolution.
- **Variant Quality**: Depends on high-quality variant calls as input.
- **Computational Resources**: May require significant memory for complex samples.
- **Haplotype Complexity**: May struggle with very high haplotype diversity.
- **Read Quality**: Poor quality reads may affect haplotype reconstruction.

## Examples

### Reconstruct haplotypes
**Args:** `devider --reads reads.fq --variants variants.vcf --output haplotypes/`
**Explanation:** Reconstructs haplotypes from heterogeneous long-read data using SNP positions.

### With reference genome
**Args:** `devider --reads reads.fq --variants variants.vcf --ref ref.fa --output haplotypes/`
**Explanation:** Use reference genome to guide haplotype reconstruction.

### Specify haplotype count
**Args:** `devider --reads reads.fq --variants variants.vcf --output haplotypes/ --haplotypes 4`
**Explanation:** Specify expected number of haplotypes in sample.

### With BAM input
**Args:** `devider --bam aligned.bam --variants variants.vcf --output haplotypes/`
**Explanation:** Use aligned BAM file instead of raw reads.

### Generate visualization
**Args:** `devider --reads reads.fq --variants variants.vcf --output haplotypes/ --plot haplotypes.png`
**Explanation:** Generate visualization of reconstructed haplotypes.