---
name: kraken-all
category: metagenomics
description: Kraken2 - taxonomic classification system using exact k-mer matching
tags: [kraken-all, metagenomics, taxonomic-classification, k-mer, Kraken2]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/kraken2/"
---

## Concepts

- **Taxonomic Classification**: Classifies sequencing reads taxonomically
- **K-mer Based**: Uses exact k-mer matching against database
- **Lowest Common Ancestor**: Resolves ambiguous classifications with LCA
- **High-throughput**: Handles millions of reads efficiently
- **Confidence Scoring**: Provides confidence scores for classifications
- **Database Building**: Supports custom database construction

## Pitfalls

- **Database Quality**: Classification depends on database completeness
- **K-mer Size**: K-mer size affects sensitivity and specificity
- **Memory Usage**: Large databases require significant memory
- **Novel Organisms**: Novel organisms may be misclassified
- **Classification Threshold**: Threshold affects sensitivity
- **Database Size**: Large databases increase memory requirements

## Examples

### Classify reads
**Args:** `kraken2 --db database --threads 8 --input reads.fastq --output results.kraken`
**Explanation:** Classifies reads using Kraken2 database.

### Standard report
**Args:** `kraken2 --db database --threads 8 --input reads.fastq --output results.kraken --report results.report`
**Explanation:** Generates classified reads and summary report.

### Paired-end reads
**Args:** `kraken2 --db database --paired reads_1.fastq reads_2.fastq --output results.kraken`
**Explanation:** Processes paired-end reads.

### Confidence filtering
**Args:** `kraken2 --db database --confidence 0.2 --input reads.fastq --output results.kraken`
**Explanation:** Uses confidence threshold of 0.2.

### Build custom database
**Args:** `kraken2-build --build --db custom_db --threads 8`
**Explanation:** Builds custom Kraken2 database.

### Add sequences to database
**Args:** `kraken2-build --add-to-library sequences.fna --db custom_db`
**Explanation:** Adds custom sequences to database library.