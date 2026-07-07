---
name: metabuli
category: metagenomics
description: Metagenomic classification via joint analysis of DNA and amino acid sequences.
tags: [metabuli, metagenomics, classification]
author: oxo-call-community
source_url: "https://github.com/steineggerlab/Metabuli"
---

## Concepts

- **Tool Overview**: Metabuli classifies metagenomic sequences using DNA and protein analysis.
- **Core Function**: Joint DNA-amino acid classification.
- **Dual Analysis**: Analyzes both nucleotide and protein sequences.
- **High Specificity**: Achieves high classification specificity.
- **Sensitive Detection**: Detects low-abundance organisms.
- **Installation**: `conda install -c bioconda metabuli`

## Pitfalls

- **Memory Requirements**: High memory for large databases.
- **Computation Time**: Slow for large datasets.
- **Database Size**: Large reference database required.
- **Parameter Tuning**: Requires careful configuration.
- **False Positives**: May misclassify sequences.
- **Data Quality**: Depends on input sequence quality.

## Examples

### Classify reads
**Args:** `metabuli -i reads.fastq -o classification.txt`
**Explanation:** Classifies metagenomic reads.

### With custom database
**Args:** `metabuli -i reads.fastq -d custom_db/ -o classification.txt`
**Explanation:** Uses custom reference database.

### High sensitivity
**Args:** `metabuli -i reads.fastq --sensitive -o classification.txt`
**Explanation:** Runs in sensitive mode.

### Threaded processing
**Args:** `metabuli -i reads.fastq -t 16 -o classification.txt`
**Explanation:** Uses 16 threads.

### Help documentation
**Args:** `metabuli --help`
**Explanation:** Displays available options.
