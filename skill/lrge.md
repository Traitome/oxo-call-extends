---
name: lrge
category: assembly
description: Genome size estimation from long read overlaps
tags: [lrge, assembly, genome-size, long-reads]
author: oxo-call-community
source_url: "https://github.com/mbhall88/lrge"
---

## Concepts

- **Tool Overview**: lrge v0.2.1 estimates genome size from long read overlaps without requiring assembly.
- **Core Function**: Uses overlap detection between long reads to infer the total genome size.
- **Overlap Detection**: Identifies overlapping regions between reads to build a coverage-based estimate.
- **Input/Output**: Input: Long reads in FASTQ or FASTA format; Output: Estimated genome size with statistics.
- **Installation**: `conda install -c bioconda lrge` or pip install.
- **Algorithm**: Based on the Lander-Waterman model with modifications for long read data.

## Pitfalls

- **Read Coverage**: Requires sufficient coverage (minimum 10x recommended) for accurate estimation.
- **Read Length**: Shorter reads may reduce estimation accuracy due to fewer overlaps.
- **Repeat Content**: High repeat content can inflate estimates due to spurious overlaps.
- **Memory Usage**: May require significant memory for large datasets.
- **Computation Time**: Processing very large datasets can be time-consuming.
- **Error Rate**: High error rates in long reads can affect overlap detection.

## Examples

### Estimate genome size
**Args:** `lrge -i reads.fastq -o genome_size.txt`
**Explanation:** Estimates genome size from long read overlaps.

### K-mer size
**Args:** `lrge -i reads.fastq -o genome_size.txt -k 21`
**Explanation:** Uses k-mer size 21 for overlap detection.

### Minimum overlap length
**Args:** `lrge -i reads.fastq -o genome_size.txt -m 500`
**Explanation:** Requires minimum 500bp overlap between reads.

### Threads
**Args:** `lrge -i reads.fastq -o genome_size.txt -t 4`
**Explanation:** Uses 4 threads for parallel processing.

### Verbose output
**Args:** `lrge -i reads.fastq -o genome_size.txt -v`
**Explanation:** Outputs detailed statistics and intermediate calculations.

### Help documentation
**Args:** `lrge --help`
**Explanation:** Displays all available options and parameters.