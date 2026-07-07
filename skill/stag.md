---
name: stag
category: metagenomics
description: A hierarchical taxonomic classifier for metagenomic sequences.
tags: [stag, metagenomics, taxonomy, classification]
author: oxo-call-community
source_url: "https://github.com/zellerlab/stag"
---

## Concepts

- **Tool Overview**: stag (v0.8.3) is a hierarchical taxonomic classifier for metagenomic sequences, using a tree-based approach for accurate classification.
- **Core Function**: Classifies metagenomic reads into taxonomic categories using a hierarchical classification strategy.
- **Algorithm**: Uses a Bayesian approach with hierarchical priors to propagate taxonomic assignments from root to leaves.
- **Input/Output**: Input: FASTQ reads or FASTA sequences; Output: Taxonomic classification with confidence scores.
- **Database**: Uses NCBI taxonomy and custom databases for classification.
- **Installation**: `conda install -c bioconda stag` or download from GitHub repository.

## Pitfalls

- **Database Compatibility**: Requires compatible database format; outdated databases affect classification accuracy.
- **Read Length**: Short reads may not provide enough information for confident classification.
- **Memory Requirements**: Large databases require significant memory for efficient classification.
- **False Positives**: May produce false positive classifications for highly conserved regions.
- **Computational Time**: Classification of large datasets can be computationally intensive.
- **Species-level Resolution**: May not resolve closely related species without sufficient discriminatory markers.

## Examples

### Display help
**Args:** `stag --help`
**Explanation:** Shows available options and usage information.

### Basic classification
**Args:** `stag classify -i reads.fastq -d database/ -o results.txt`
**Explanation:** Classify metagenomic reads using default settings.

### Build database
**Args:** `stag build -i reference_genomes/ -o database/`
**Explanation:** Build custom classification database from reference genomes.

### With confidence threshold
**Args:** `stag classify -i reads.fastq -d database/ -o results.txt -c 0.8`
**Explanation:** Set minimum confidence threshold for classifications.

### Output format options
**Args:** `stag classify -i reads.fastq -d database/ -o results.txt --format csv`
**Explanation:** Output results in CSV format.

### Batch processing
**Args:** `stag classify -i sample1.fastq sample2.fastq -d database/ -o results/`
**Explanation:** Process multiple samples together.

### Verbose mode
**Args:** `stag classify -i reads.fastq -d database/ -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Memory optimization
**Args:** `stag classify -i reads.fastq -d database/ -o results.txt --low-memory`
**Explanation:** Use memory-efficient mode for large datasets.
