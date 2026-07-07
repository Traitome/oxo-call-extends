---
name: kraken
category: metagenomics
description: Kraken - taxonomic classification system for metagenomic sequences
tags: [kraken, metagenomics, taxonomic-classification, k-mer, microbiome]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/kraken"
---

## Concepts

- **K-mer Based Classification**: Uses k-mer matching for taxonomic assignment
- **Lowest Common Ancestor**: Resolves ambiguous matches using LCA algorithm
- **High Sensitivity**: Sensitive detection of taxonomic content
- **Reference Database**: Uses curated reference genome database
- **Fast Processing**: Rapid classification of millions of reads
- **Multiple Ranks**: Reports classifications at all taxonomic ranks

## Pitfalls

- **Database Dependency**: Classification quality depends on database
- **K-mer Size**: 31-mer default may miss some relationships
- **Memory Requirements**: Database size affects memory usage
- **Novel Organisms**: Novel species may be unclassifiable
- **Classification Threshold**: Threshold setting affects results
- **Chimeric Reads**: Reads from multiple organisms cause issues

## Examples

### Basic classification
**Args:** `kraken --db /path/to/db --threads 8 --fastq-input reads.fastq --output results.kraken`
**Explanation:** Classifies reads against Kraken database.

### With report
**Args:** `kraken --db database --threads 8 --fastq-input reads.fastq --output results.kraken --report results.report`
**Explanation:** Creates both classified output and summary report.

### Paired-end reads
**Args:** `kraken --db database --paired reads_1.fastq reads_2.fastq --output results.kraken`
**Explanation:** Processes paired-end sequencing data.

### Confidence threshold
**Args:** `kraken --db database --confidence 0.2 --fastq-input reads.fastq --output results.kraken`
**Explanation:** Only classifies reads above confidence threshold.

### Build database
**Args:** `kraken-build --build --db new_database --threads 8`
**Explanation:** Builds a new Kraken database from genomic sequences.

### Add to library
**Args:** `kraken-build --add-to-library genome.fna --db existing_database`
**Explanation:** Adds custom genomes to existing database.