---
name: microbecensus
category: utility
description: A command-line tool for estimating average genome size from shotgun sequence data
tags: [microbecensus, utility, metagenomics]
author: oxo-call-community
source_url: "https://github.com/snayfach/MicrobeCensus"
---

## Concepts

- **Tool Overview**: MicrobeCensus v1.1.1 estimates average genome size from shotgun sequencing data.
- **Core Function**: Estimates average genome size from metagenomic reads.
- **k-mer Analysis**: Uses k-mer frequency analysis for estimation.
- **Metagenomic Data**: Optimized for metagenomic sequencing data.
- **Input/Output**: Accepts sequencing reads; outputs genome size estimates.
- **Community Analysis**: Provides insights into microbial community characteristics.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal estimation.
- **Data Quality**: Estimation accuracy depends on input data quality.
- **Community Complexity**: Results may vary with community complexity.
- **Runtime**: Analysis of large datasets can be time-consuming.

## Examples

### Estimate genome size
**Args:** `microbecensus -i reads.fastq -o estimate.txt`
**Explanation:** Estimates average genome size from sequencing data.

### With custom k-mer size
**Args:** `microbecensus -i reads.fastq -o estimate.txt -k 21`
**Explanation:** Uses k-mer size of 21 for analysis.

### Paired-end analysis
**Args:** `microbecensus -i reads_1.fastq -r reads_2.fastq -o estimate.txt`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `microbecensus -i fastq/ -o estimates/`
**Explanation:** Processes multiple samples in batch mode.

### Detailed output
**Args:** `microbecensus -i reads.fastq -o estimate.txt -v`
**Explanation:** Generates detailed estimation report.