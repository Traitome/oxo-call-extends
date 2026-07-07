---
name: fufihla
category: hpc
description: HLA typing pipeline for long reads (FuFiHLA) with a location-aware CLI.
tags: [fufihla, HLA typing, long reads, genomics]
author: oxo-call-community
source_url: "https://github.com/jingqing-hu/FuFiHLA"
---

## Concepts
- **HLA Typing**: Determines HLA alleles from sequencing data.
- **Long-read Support**: Optimized for PacBio and Oxford Nanopore reads.
- **Location-aware**: Uses genomic location information for accurate typing.
- **Multi-allele Detection**: Detects multiple HLA alleles.
- **High Resolution**: Provides high-resolution HLA typing.

## Pitfalls
- **Long-read Specific**: Designed for long-read sequencing data.
- **Computational Requirements**: High computational requirements for accurate typing.
- **Memory Usage**: Requires significant memory for large datasets.
- **Reference Database**: Needs up-to-date HLA reference database.
- **Data Quality**: Requires high-quality long reads.

## Examples
### Basic HLA typing
**Args:** `fufihla --reads long_reads.fastq --output hla_types.txt`
**Explanation:** Performs HLA typing on long reads.

### With reference genome
**Args:** `fufihla --reads long_reads.fastq --reference hla_ref/ --output hla_types.txt`
**Explanation:** Uses custom HLA reference database.

### High-resolution typing
**Args:** `fufihla --reads long_reads.fastq --high-res --output hla_types.txt`
**Explanation:** Performs high-resolution HLA typing.

### Batch processing
**Args:** `fufihla --batch samples.txt --output results/`
**Explanation:** Processes multiple samples in batch.

### Generate report
**Args:** `fufihla --reads long_reads.fastq --report --output report.html`
**Explanation:** Generates HTML report of HLA typing results.