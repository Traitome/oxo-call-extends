---
name: kmer-jellyfish
category: expression
description: Fast, memory-efficient k-mer counting for DNA sequences
tags: [kmer-jellyfish, expression, k-mer, counting, genomics]
author: oxo-call-community
source_url: "https://genome.umd.edu/jellyfish.html"
---

## Concepts

- **K-mer Counting**: Counts k-mers in DNA sequences with high efficiency
- **Memory Efficiency**: Uses hash-based algorithm for memory efficiency
- **Multi-threading**: Supports parallel processing for faster counting
- **Database Format**: Stores k-mer counts in binary database format
- **Histogram Generation**: Generates k-mer abundance histograms
- **Query Support**: Allows querying k-mer counts from database

## Pitfalls

- **Memory Allocation**: Large k-mer sizes require more memory
- **K-mer Size Limits**: Maximum k-mer size is limited by implementation
- **Disk Usage**: Binary database files can be large
- **Hash Collisions**: Hash-based approach may have collisions
- **Duplicate Reads**: May count duplicate reads without filtering
- **Compatibility**: Binary format may not be compatible with all tools

## Examples

### Count k-mers
**Args:** `jellyfish count -m 21 -s 100M -t 4 -o reads.jf reads.fastq`
**Explanation:** Counts 21-mers using 100MB hash size and 4 threads.

### Generate histogram
**Args:** `jellyfish histo -h reads.jf -o histogram.txt`
**Explanation:** Generates k-mer abundance histogram.

### Query k-mer count
**Args:** `jellyfish query -s reads.jf ATCGATCGATCG`
**Explanation:** Queries count for a specific k-mer sequence.

### Paired-end reads
**Args:** `jellyfish count -m 25 -s 200M -t 8 -o paired.jf read1.fastq read2.fastq`
**Explanation:** Counts k-mers from paired-end reads.

### Multi-file counting
**Args:** `jellyfish count -m 21 -s 100M -o output.jf file1.fastq file2.fastq`
**Explanation:** Combines k-mer counts from multiple files.

### Dump database
**Args:** `jellyfish dump -o kmer_counts.fa reads.jf`
**Explanation:** Exports k-mer database to FASTA format.