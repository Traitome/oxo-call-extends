---
name: longphase
category: epigenomics
description: LongPhase is an ultra-fast program for simultaneously co-phasing SNPs, small indels, large SVs, and (5mC) modifications for Nanopore and PacBio platforms.
tags: [longphase, epigenomics]
author: oxo-call-community
source_url: "https://github.com/twolinin/longphase"
---

## Concepts

- **Tool Overview**: longphase v2.0.1 - LongPhase is an ultra-fast program for simultaneously co-phasing SNPs, small indels, large SVs, and (5mC) modifications for Nanopore and PacBio platforms..
- **Core Function**: LongPhase is an ultra-fast program for simultaneously co-phasing SNPs, small indels, large SVs, and (5mC) modifications for Nanopore and PacBio platforms.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda longphase`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Phase haplotypes
**Args:** `longphase haplotype -r reference.fa -b reads.bam -o phased_output`
**Explanation:** Phases haplotypes from long-read data.

