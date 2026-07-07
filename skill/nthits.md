---
name: nthits
category: qc
description: ntHits efficiently counts and filters k-mers based on their frequencies for quality control.
tags: [nthits, qc, k-mer, filtering]
author: oxo-call-community
source_url: "https://github.com/bcgsc/ntHits"
---

## Concepts

- **Tool Overview**: ntHits performs efficient k-mer counting and frequency-based filtering.
- **Core Function**: Counts k-mer frequencies and filters based on thresholds.
- **Algorithm**: Uses efficient data structures for k-mer counting.
- **Input Format**: Accepts FASTQ/FASTA sequencing reads.
- **Output**: Produces k-mer counts and filtered k-mer sets.
- **Use Case**: Quality control, genome assembly, and sequencing analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large k-mer sets require memory.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Threshold Selection**: Requires careful frequency threshold selection.
- **Computational Cost**: Large datasets can be computationally intensive.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `nthits --help`
**Explanation:** Shows available options and usage instructions.

### Count k-mers
**Args:** `nthits -k 21 -i reads.fastq -o kmer_counts.txt`
**Explanation:** Counts k-mers from sequencing reads.

### Filter by frequency
**Args:** `nthits -k 21 -i reads.fastq -f 5-1000 -o filtered_kmers.txt`
**Explanation:** Filters k-mers by frequency range.

### Multiple k-mer sizes
**Args:** `nthits -k 21,31,51 -i reads.fastq -o kmer_counts.txt`
**Explanation:** Counts multiple k-mer sizes.

### Paired-end reads
**Args:** `nthits -k 21 -i reads_1.fastq -i2 reads_2.fastq -o kmer_counts.txt`
**Explanation:** Processes paired-end reads.

### Threads
**Args:** `nthits -k 21 -i reads.fastq -t 8 -o kmer_counts.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nthits -k 21 -i reads.fastq -v -o kmer_counts.txt`
**Explanation:** Runs with verbose output.