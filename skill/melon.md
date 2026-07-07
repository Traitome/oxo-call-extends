---
name: melon
category: expression
description: Metagenomic long-read-based taxonomic identification and quantification using marker genes.
tags: [melon, metagenomics, long-read]
author: oxo-call-community
source_url: "https://github.com/xinehc/melon"
---

## Concepts

- **Tool Overview**: Melon identifies and quantifies taxa from long-read metagenomic data.
- **Core Function**: Taxonomic identification using marker genes.
- **Long-read Support**: Optimized for long-read sequencing data.
- **Marker Genes**: Uses conserved marker genes for classification.
- **Quantification**: Provides relative abundance estimates.
- **Installation**: `conda install -c bioconda melon`

## Pitfalls

- **Data Quality**: Requires high-quality long-read data.
- **Marker Database**: Depends on comprehensive marker database.
- **Computation Time**: Slow for large datasets.
- **Memory Requirements**: High memory usage.
- **False Positives**: May misclassify closely related taxa.
- **Parameter Tuning**: Requires careful threshold adjustment.

## Examples

### Classify long reads
**Args:** `melon -i reads.fastq -o taxonomy.txt`
**Explanation:** Classifies long reads taxonomically.

### With custom database
**Args:** `melon -i reads.fastq -d custom_markers/ -o taxonomy.txt`
**Explanation:** Uses custom marker gene database.

### Verbose mode
**Args:** `melon -i reads.fastq -v -o taxonomy.txt`
**Explanation:** Shows detailed classification progress.

### Quantify abundance
**Args:** `melon -i reads.fastq --quantify -o abundance.txt`
**Explanation:** Quantifies taxonomic abundance.

### Help documentation
**Args:** `melon --help`
**Explanation:** Displays available options.
