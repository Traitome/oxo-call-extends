---
name: longtrack
category: metagenomics
description: LongTrack - Track FMT strains using long-read metagenomic assemblies
tags: [longtrack, metagenomics, FMT, strain-tracking, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fanglab/LongTrack"
---

## Concepts

- **FMT Tracking**: Tracking fecal microbiota transplantation strains
- **Strain Identification**: Identifying specific microbial strains
- **Metagenomics**: Analysis of metagenomic sequencing data
- **Long-read Data**: Using long reads for strain resolution
- **Strain Tracking**: Monitoring strain presence over time
- **Microbiome Analysis**: Comprehensive microbiome analysis

## Pitfalls

- **Read Quality**: Poor quality reads affect tracking
- **Strain Complexity**: Highly similar strains may be difficult to distinguish
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive strain identifications

## Examples

### Track strains
**Args:** `longtrack --assemblies assemblies/ --output tracking_results/`
**Explanation:** Tracks FMT strains across samples.

### Reference database
**Args:** `longtrack --assemblies assemblies/ --ref-db reference.fasta --output tracking_results/`
**Explanation:** Uses custom reference database.

### Threads
**Args:** `longtrack --assemblies assemblies/ --output tracking_results/ --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum coverage
**Args:** `longtrack --assemblies assemblies/ --output tracking_results/ --min-cov 10`
**Explanation:** Sets minimum coverage threshold.

### Output format
**Args:** `longtrack --assemblies assemblies/ --output tracking_results.json --format json`
**Explanation:** Outputs results in JSON format.

### Verbose output
**Args:** `longtrack --assemblies assemblies/ --output tracking_results/ --verbose`
**Explanation:** Provides detailed output.