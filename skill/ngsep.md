---
name: ngsep
category: variant-calling
description: NGSEP - Next Generation Sequencing Experience Platform
tags: [ngsep, variant-calling]
author: oxo-call-community
source_url: "https://github.com/NGSEP/NGSEPcore"
---

## Concepts
- **Tool Overview**: NGSEP provides an object model to enable different kinds of analysis of DNA high throughput sequencing (HTS) data. The classic use of NGSEP is a reference guided construction and downstream analysis of large datasets of genomic variation. NGSEP performs accurate detection and genotyping of Single Nucleotide Variants (SNVs), small and large indels, short tandem repeats (STRs), inversions, and Copy Number Variants (CNVs). NGSEP also provides utilities for downstream analysis of variation in VCF files, including functional annotation of variants, filtering, format conversion, comparison, clustering, imputation, introgression analysis and different kinds of statistics.
- **Core Function**: Processes bioinformatics data for variant-calling tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda ngsep`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
