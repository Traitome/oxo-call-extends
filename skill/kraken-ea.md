---
name: kraken-ea
category: metagenomics
description: Kraken modified version with FASTQ splitting based on taxonomic classification
tags: [kraken-ea, metagenomics, taxonomic-classification, FASTQ-splitting]
author: oxo-call-community
source_url: "https://github.com/ExpressionAnalysis/kraken/tree/v0.10.5-beta-ea.3"
---

## Concepts

- **Taxonomic Classification**: Assigns taxonomic labels to metagenomic sequences
- **FASTQ Splitting**: Splits reads based on taxonomic classification
- **Modified Kraken**: Enhanced version of standard Kraken
- **Metagenomics**: Designed for metagenomic studies
- **Paired-end Support**: Handles both single and paired-end reads
- **Database Compatibility**: Compatible with standard Kraken databases

## Pitfalls

- **Database Quality**: Classification depends on reference database
- **K-mer Size**: K-mer size affects sensitivity/specificity
- **Memory Usage**: Large databases require significant memory
- **Novel Organisms**: Novel organisms may be misclassified
- **Classification Threshold**: Threshold affects classification decisions
- **Read Quality**: Low-quality reads affect classification accuracy

## Examples

### Classify and split reads
**Args:** `kraken-ea --db database --fastq-input reads.fastq --split --output results/`
**Explanation:** Classifies reads and splits into separate files.

### Paired-end classification
**Args:** `kraken-ea --db database --paired reads_1.fastq reads_2.fastq --output results.kraken`
**Explanation:** Classifies paired-end reads.

### Extract specific taxon
**Args:** `kraken-ea --db database --fastq-input reads.fastq --taxid 562 --split -o e_coli/`
**Explanation:** Extracts E. coli reads by taxon ID.

### Confidence threshold
**Args:** `kraken-ea --db database --confidence 0.2 --fastq-input reads.fastq --split -o results/`
**Explanation:** Uses confidence threshold for classification.

### Generate report
**Args:** `kraken-ea --db database --fastq-input reads.fastq --report results.report --split -o results/`
**Explanation:** Creates classification report with split files.

### Batch processing
**Args:** `kraken-ea --batch -d samples/ --db database -o results/`
**Explanation:** Processes multiple samples in batch.