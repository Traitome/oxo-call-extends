---
name: ntcard
category: utility
description: ntCard estimates k-mer coverage histograms from genomic sequencing data.
tags: [ntcard, utility, k-mer, coverage]
author: oxo-call-community
source_url: "https://github.com/BirolLab/ntCard"
---

## Concepts

- **Tool Overview**: ntCard efficiently computes k-mer coverage histograms.
- **Core Function**: Counts k-mer frequencies and generates coverage histograms.
- **Algorithm**: Uses counting and hashing for efficient k-mer processing.
- **Input Format**: Accepts FASTQ/FASTA sequencing reads.
- **Output**: Produces k-mer coverage histogram and statistics.
- **Use Case**: Genome assembly, sequencing depth analysis, and quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large k-mer sets require memory.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Computational Cost**: Large datasets can be computationally intensive.
- **Disk Space**: Temporary files may require significant space.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ntcard --help`
**Explanation:** Shows available options and usage instructions.

### Compute k-mer histogram
**Args:** `ntcard -k 21 -i reads.fastq -o histogram.txt`
**Explanation:** Computes k-mer histogram with k=21.

### Multiple k-mer sizes
**Args:** `ntcard -k 21,31,51 -i reads.fastq -o histogram.txt`
**Explanation:** Computes histograms for multiple k-mer sizes.

### Paired-end reads
**Args:** `ntcard -k 21 -i reads_1.fastq -i2 reads_2.fastq -o histogram.txt`
**Explanation:** Processes paired-end reads.

### Memory limit
**Args:** `ntcard -k 21 -i reads.fastq -o histogram.txt -m 10G`
**Explanation:** Limits memory usage to 10GB.

### Output statistics
**Args:** `ntcard -k 21 -i reads.fastq -o histogram.txt --stats`
**Explanation:** Outputs detailed statistics.

### Verbose mode
**Args:** `ntcard -k 21 -i reads.fastq -o histogram.txt -v`
**Explanation:** Runs with verbose output.