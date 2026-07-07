---
name: meta-sparse
category: metagenomics
description: SPARSE indexes reference genomes in public databases into hierarchical clusters and uses it to predict origins of metagenomic reads.
tags: [meta-sparse, metagenomics, read-classification]
author: oxo-call-community
source_url: "https://github.com/zheminzhou/SPARSE/"
---

## Concepts

- **Tool Overview**: SPARSE v0.1.12 is a metagenomic read classification tool that indexes reference genomes into hierarchical clusters for efficient taxonomic assignment.
- **Core Function**: Predicts the taxonomic origins of metagenomic reads using hierarchical clustering of reference genomes.
- **Hierarchical Indexing**: Builds hierarchical indexes of reference genomes for fast and accurate classification.
- **Read Classification**: Assigns metagenomic reads to their likely taxonomic origins.
- **Input/Output**: Accepts FASTQ reads; outputs taxonomic assignments with confidence scores.
- **Scalability**: Designed for large-scale metagenomic datasets.

## Pitfalls

- **Index Size**: Building indexes for large genome collections may require significant storage.
- **Database Completeness**: Classification accuracy depends on reference database completeness.
- **Memory Requirements**: Processing large datasets may require significant memory.
- **False Positives**: May produce false positive classifications.
- **Runtime**: Index construction can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.

## Examples

### Build hierarchical index
**Args:** `sparse build -i genomes/ -o index/`
**Explanation:** Builds a hierarchical index from reference genomes.

### Classify reads
**Args:** `sparse classify -i reads.fastq -d index/ -o results.txt`
**Explanation:** Classifies metagenomic reads using the built index.

### With confidence threshold
**Args:** `sparse classify -i reads.fastq -d index/ -o results.txt -c 0.8`
**Explanation:** Applies minimum confidence threshold of 0.8.

### Output detailed report
**Args:** `sparse classify -i reads.fastq -d index/ -o results.txt -v`
**Explanation:** Generates detailed classification report with verbose output.

### Batch processing
**Args:** `sparse classify -i fastq/ -d index/ -o results/`
**Explanation:** Processes multiple FASTQ files in batch mode.