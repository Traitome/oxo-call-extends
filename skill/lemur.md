---
name: lemur
category: metagenomics
description: Rapid and accurate taxonomic profiling for long-read metagenomic datasets
tags: [lemur, metagenomics, taxonomic-profiling, long-read, nanopore, sequencing]
author: oxo-call-community
source_url: "https://github.com/treangenlab/lemur"
---

## Concepts

- **Long-read Metagenomics**: Optimized for long-read sequencing data
- **Taxonomic Profiling**: Identifies and quantifies microbial taxa
- **Rapid Analysis**: Fast processing of metagenomic datasets
- **Accurate Classification**: High accuracy taxonomic assignments
- **Nanopore Support**: Works with Oxford Nanopore data
- **K-mer Based**: Uses k-mer based classification approach

## Pitfalls

- **Read Quality**: Poor quality reads affect classification
- **Database Size**: Large databases increase memory usage
- **Species Coverage**: Limited database coverage affects results
- **Computational Resources**: Requires significant compute resources
- **Read Length**: Very short reads may classify poorly
- **Memory Usage**: Large datasets need careful memory management

## Examples

### Profile metagenome
**Args:** `lemur profile -i reads.fastq -o profile.txt`
**Explanation:** Performs taxonomic profiling on long reads.

### Specify database
**Args:** `lemur profile -i reads.fastq -d custom_db/ -o profile.txt`
**Explanation:** Uses custom reference database.

### Set k-mer size
**Args:** `lemur profile -i reads.fastq -k 31 -o profile.txt`
**Explanation:** Uses k-mer size of 31 for classification.

### Paired-end mode
**Args:** `lemur profile -1 reads_1.fastq -2 reads_2.fastq -o profile.txt`
**Explanation:** Processes paired-end reads.

### Generate report
**Args:** `lemur profile -i reads.fastq -o profile.txt --report`
**Explanation:** Creates detailed analysis report.

### Batch processing
**Args:** `lemur batch -d samples/ -o results/`
**Explanation:** Processes multiple samples.