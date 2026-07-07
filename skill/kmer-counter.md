---
name: kmer-counter
category: expression
description: An efficient k-mer counter for large sequencing read sets
tags: [kmer-counter, expression, k-mer, counting, tensorflow]
author: oxo-call-community
source_url: "https://github.com/CobiontID/kmer-counter"
---

## Concepts

- **Efficient K-mer Counting**: Counts k-mers from large sequencing datasets
- **FASTA Parsing**: Uses Needletail for fast FASTA/FASTQ parsing
- **NumPy Export**: Outputs k-mer counts as NumPy arrays
- **TensorFlow Integration**: Designed for TensorFlow-based downstream analysis
- **Memory Efficiency**: Optimized for large-scale k-mer counting
- **Streaming Processing**: Handles large files without loading entire dataset

## Pitfalls

- **Memory Usage**: Very large datasets may exceed memory limits
- **K-mer Size**: Larger k-mers increase memory requirements
- **File Format**: Requires properly formatted input files
- **Duplicate Handling**: May count duplicate reads if not filtered
- **Output Size**: Large k-mer sets produce large output files
- **Parallelization**: Performance depends on available CPU cores

## Examples

### Count k-mers from FASTQ
**Args:** `kmer-counter -i reads.fastq -k 21 -o counts.npy`
**Explanation:** Counts 21-mers and outputs as NumPy array.

### Specify k-mer size
**Args:** `kmer-counter -i input.fastq -k 31 -o output.npy`
**Explanation:** Uses k-mer size of 31 for counting.

### Process FASTA file
**Args:** `kmer-counter -i genome.fasta -k 25 -o genome_kmers.npy`
**Explanation:** Counts k-mers from a genome FASTA file.

### Batch processing
**Args:** `kmer-counter batch -d reads_dir/ -k 21 -o output_dir/`
**Explanation:** Processes multiple FASTQ files in batch mode.

### With TensorFlow
**Args:** `kmer-counter -i reads.fastq -k 21 -o counts.npy --tf-compatible`
**Explanation:** Outputs TF-compatible NumPy array for TensorFlow.

### Quality filtering
**Args:** `kmer-counter -i reads.fastq -k 21 -o filtered.npy -q 20`
**Explanation:** Only counts k-mers from high-quality reads (Q20+).