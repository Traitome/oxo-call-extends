---
name: livekraken
category: metagenomics
description: LiveKraken - Real-time metagenomic classifier for Illumina sequencing
tags: [livekraken, metagenomics, real-time, classification, Illumina, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.com/SimonHTausch/LiveKraken"
---

## Concepts

- **Real-time Classification**: Real-time metagenomic classification
- **K-mer Analysis**: K-mer based taxonomic classification
- **Illumina Sequencing**: Optimized for Illumina sequencing data
- **Streaming Analysis**: Streaming analysis of sequencing data
- **Taxonomic Profiling**: Taxonomic profiling of metagenomic samples
- **Rapid Detection**: Rapid detection of pathogens

## Pitfalls

- **Reference Database**: Requires large reference database
- **Memory Usage**: Memory-intensive for real-time processing
- **Speed vs Accuracy**: Trade-off between speed and accuracy
- **Parameter Tuning**: Requires careful parameter optimization
- **Data Rate**: Must handle high data rates
- **False Positives**: May produce false positive identifications

## Examples

### Real-time classification
**Args:** `livekraken -i reads.fastq -o results.txt`
**Explanation:** Performs real-time metagenomic classification.

### Stream from stdin
**Args:** `cat reads.fastq | livekraken -o results.txt`
**Explanation:** Processes reads from standard input.

### Custom database
**Args:** `livekraken -i reads.fastq -o results.txt -d custom_db`
**Explanation:** Uses custom reference database.

### Threads
**Args:** `livekraken -i reads.fastq -o results.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum confidence
**Args:** `livekraken -i reads.fastq -o results.txt -c 0.8`
**Explanation:** Sets minimum confidence threshold to 0.8.

### Output format
**Args:** `livekraken -i reads.fastq -o results.json -f json`
**Explanation:** Outputs results in JSON format.