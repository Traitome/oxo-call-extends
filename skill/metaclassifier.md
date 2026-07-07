---
name: metaclassifier
category: alignment
description: MetaClassifier is an integrated pipeline for classifying and quantifying DNA metabarcoding data into taxonomy groups
tags: [metaclassifier, alignment, metabarcoding, taxonomy, classification]
author: oxo-call-community
source_url: "https://github.com/ewafula/MetaClassifier"
---

## Concepts

- **Tool Overview**: MetaClassifier v1.0.1 is an integrated pipeline for classifying and quantifying DNA metabarcoding data into taxonomic groups, originally designed for analyzing honey floral composition.
- **Core Function**: Utilizes marker sequence databases to classify high-throughput metabarcoding reads into taxonomic groups and quantify taxon abundance.
- **Database Integration**: Uses reference databases of marker sequences with corresponding taxonomy lineage information for classification.
- **Multi-purpose**: Can be employed in barcoding, metabarcoding, and metagenomics studies for characterizing ecological communities.
- **Input/Output**: Accepts sequencing reads in FASTQ format; outputs taxonomic classifications with abundance estimates.
- **Abundance Quantification**: Provides quantitative analysis of taxon abundance in samples.

## Pitfalls

- **Database Completeness**: Classification accuracy depends on reference database completeness.
- **PCR Bias**: PCR amplification biases can affect taxon abundance estimates.
- **Marker Selection**: Choice of marker gene impacts classification results.
- **Sequence Quality**: Low-quality reads may produce incorrect classifications.
- **Taxonomic Resolution**: Limited by the taxonomic resolution of the reference database.
- **Chimera Formation**: Chimeric sequences can lead to false positive classifications.

## Examples

### Classify metabarcoding reads
**Args:** `metaclassifier -i reads.fastq -o results/`
**Explanation:** Classifies metabarcoding reads into taxonomic groups.

### With custom database
**Args:** `metaclassifier -i reads.fastq -d custom_db/ -o results/`
**Explanation:** Uses a custom reference database for classification.

### Paired-end analysis
**Args:** `metaclassifier -i reads_1.fastq reads_2.fastq -o results/`
**Explanation:** Processes paired-end sequencing data.

### Generate abundance report
**Args:** `metaclassifier -i reads.fastq -o results/ --report`
**Explanation:** Generates a comprehensive abundance report.

### Filter by confidence
**Args:** `metaclassifier -i reads.fastq -o results/ -c 0.8`
**Explanation:** Filters classifications to minimum confidence score of 0.8.