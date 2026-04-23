---
name: nasp
category: variant-calling
description: NASP: an accurate, rapid method for the identification of SNPs in WGS datasets that supports flexible input and output formats
tags: [nasp, variant-calling, snp, wgs, identification]
author: oxo-call-community
source_url: "https://github.com/TGenNorth/nasp"
---

## Concepts

- **Tool Overview**: NASP v1.2.1 - accurate SNP identification in WGS datasets.
- **Core Function**: Identifies SNPs in whole genome sequencing data with flexible input/output format support.
- **Input/Output**: Takes BAM/FASTQ and reference; outputs SNP matrices in various formats.
- **Installation**: `conda install -c bioconda nasp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports multiple input formats including BAM and FASTQ.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-r reference.fasta -i aligned.bam -o snp_matrix.tsv`
**Explanation:** Identifies SNPs from WGS alignment data.
