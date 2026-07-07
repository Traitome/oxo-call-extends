---
name: lotus3
category: metagenomics
description: LotuS3 - Lightweight amplicon sequencing pipeline supporting 16S/18S/ITS
tags: [lotus3, metagenomics, amplicon, 16S, ITS, bioinformatics]
author: oxo-call-community
source_url: "https://lotus3.earlham.ac.uk/"
---

## Concepts

- **Amplicon Sequencing**: Analysis of amplicon sequencing data
- **16S rRNA**: 16S ribosomal RNA analysis
- **18S rRNA**: 18S ribosomal RNA analysis
- **ITS**: Internal transcribed spacer analysis
- **Microbiome Analysis**: Microbiome community analysis
- **Pipeline Workflow**: Complete analysis workflow

## Pitfalls

- **Read Quality**: Poor quality reads affect analysis
- **Primer Dimer**: Primer dimers may affect results
- **PCR Bias**: PCR amplification bias may affect results
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization

## Examples

### Run pipeline
**Args:** `lotus3 -i reads.fastq -o results/`
**Explanation:** Runs complete amplicon sequencing pipeline.

### 16S mode
**Args:** `lotus3 -i reads.fastq -o results/ --16s`
**Explanation:** Optimized for 16S rRNA analysis.

### ITS mode
**Args:** `lotus3 -i reads.fastq -o results/ --its`
**Explanation:** Optimized for ITS analysis.

### Threads
**Args:** `lotus3 -i reads.fastq -o results/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Reference database
**Args:** `lotus3 -i reads.fastq -o results/ --ref-db silva`
**Explanation:** Uses SILVA reference database.

### Verbose output
**Args:** `lotus3 -i reads.fastq -o results/ -v`
**Explanation:** Provides detailed output.