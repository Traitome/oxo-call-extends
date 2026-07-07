---
name: kmerstream
category: utility
description: Streaming algorithm for computing k-mer statistics for massive genomics datasets
tags: [kmerstream, utility, streaming, k-mer, statistics, genomics]
author: oxo-call-community
source_url: "https://github.com/pmelsted/KmerStream"
---

## Concepts

- **Streaming Algorithm**: Processes data in streaming mode without loading entire dataset
- **K-mer Statistics**: Computes statistics on k-mer frequencies
- **Memory Efficiency**: Uses constant memory regardless of dataset size
- **Massive Datasets**: Designed for large-scale genomics data
- **Distribution Analysis**: Analyzes k-mer frequency distributions
- **Diversity Estimation**: Estimates species diversity from sequencing data

## Pitfalls

- **Streaming Limitations**: Cannot perform operations requiring full dataset
- **K-mer Size**: Large k-mer sizes increase memory requirements
- **Data Quality**: Low-quality data affects statistics
- **Accuracy Trade-offs**: Streaming may sacrifice some accuracy for efficiency
- **Single-pass Processing**: Can only process data once
- **Result Interpretation**: Statistics require careful interpretation

## Examples

### Compute k-mer statistics
**Args:** `kmerstream -i reads.fastq -k 21 -o statistics.txt`
**Explanation:** Computes k-mer statistics from sequencing data.

### Estimate diversity
**Args:** `kmerstream -i metagenome.fastq -k 31 --diversity -o diversity.txt`
**Explanation:** Estimates species diversity from metagenomic data.

### Large dataset processing
**Args:** `kmerstream -i large_file.fastq -k 25 -o stats.txt`
**Explanation:** Processes large dataset with streaming algorithm.

### Generate distribution
**Args:** `kmerstream -i reads.fastq -k 21 --distribution -o dist.txt`
**Explanation:** Generates k-mer frequency distribution.

### Compare samples
**Args:** `kmerstream -i sample1.fastq -i sample2.fastq --compare -o compare.txt`
**Explanation:** Compares k-mer statistics between two samples.

### Batch mode
**Args:** `kmerstream --batch -d samples/ -k 21 -o results/`
**Explanation:** Processes multiple samples in batch mode.