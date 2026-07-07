---
name: dsk
category: expression
description: "DSK is a k-mer counter for reads or genomes."
tags: [dsk, expression, k-mer, counting, genome-analysis]
author: oxo-call-community
source_url: "https://github.com/GATB/dsk"
---

## Concepts

- **Tool Overview**: DSK (Disk Streaming of K-mers) is a fast and memory-efficient k-mer counter for sequencing reads and genomes.
- **Core Function**: Counts k-mer occurrences in large sequencing datasets with minimal memory usage.
- **Input/Output**: Input: Sequencing reads (FASTA/FASTQ) or genome sequences. Output: K-mer count files.
- **Algorithm**: Uses disk streaming and bloom filters for efficient k-mer counting.
- **Key Features**: Low memory footprint, parallel processing, supports large k values, solid and non-solid k-mer output.
- **Installation**: `conda install -c bioconda dsk`

## Pitfalls

- **Disk Space**: Requires sufficient disk space for temporary files during counting.
- **K-mer Size**: Very large k values may reduce counting efficiency.
- **Memory Limits**: Despite efficiency, extremely large datasets may still require substantial resources.
- **Solid K-mers**: Threshold for solid k-mers affects downstream analysis.
- **Reverse Complement**: Consider strand-specific counting options.

## Examples

### Basic k-mer counting
**Args:** `-file reads.fastq -kmer-size 21 -out counts.txt`
**Explanation:** Counts 21-mers in sequencing reads.

### Count with abundance threshold
**Args:** `-file reads.fastq -kmer-size 31 -abundance-min 2 -out counts.txt`
**Explanation:** Counts 31-mers with minimum abundance of 2.

### Parallel counting
**Args:** `-file reads.fastq -kmer-size 21 -nb-cores 8 -out counts.txt`
**Explanation:** Uses 8 CPU cores for parallel k-mer counting.

### Solid k-mers only
**Args:** `-file reads.fastq -kmer-size 21 -solid -out solid_kmers.txt`
**Explanation:** Outputs only solid k-mers (above abundance threshold).

### Multiple files
**Args:** `-file file1.fastq file2.fastq -kmer-size 21 -out counts.txt`
**Explanation:** Counts k-mers across multiple input files.