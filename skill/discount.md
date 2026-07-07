---
name: discount
category: utility
description: DISCOunt - Fast k-mer counting tool.
tags: [discount, utility, k-mer, counting, sequencing]
author: oxo-call-community
source_url: "https://github.com/GATB/discount"
---

## Concepts

- **Tool Overview**: DISCOunt is a fast k-mer counting tool for sequencing data.
- **Core Function**: Counts k-mer occurrences in sequencing reads efficiently.
- **Input/Output**: Input: FASTQ files. Output: k-mer count tables, frequency distributions.
- **Algorithm**: Uses efficient data structures for fast k-mer counting.
- **Key Features**: Fast k-mer counting, memory efficient, multiple k-mer sizes, frequency filtering, batch processing.
- **Installation**: `conda install -c bioconda discount`

## Pitfalls

- **Input Format**: Requires FASTQ format reads.
- **K-mer Size**: Maximum k-mer size may be limited.
- **Memory Usage**: Large datasets may require significant memory.
- **Read Quality**: Poor quality reads affect k-mer counting accuracy.
- **Output Size**: Large k-mer sets produce large output files.

## Examples

### Count k-mers
**Args:** `discount --input reads.fq --kmer 31 --output kmers.tsv`
**Explanation:** Counts k-mer occurrences in sequencing data.

### Multiple k-mer sizes
**Args:** `discount --input reads.fq --kmer 21,31,41 --output kmers/`
**Explanation:** Count k-mers at multiple sizes simultaneously.

### Filter by frequency
**Args:** `discount --input reads.fq --kmer 31 --output kmers.tsv --min-count 5`
**Explanation:** Filter k-mers by minimum occurrence count.

### Batch processing
**Args:** `discount --input-dir fastq_files/ --kmer 31 --output-dir results/`
**Explanation:** Process multiple FASTQ files in batch.

### Generate frequency distribution
**Args:** `discount --input reads.fq --kmer 31 --output kmers.tsv --histogram freq.png`
**Explanation:** Generate k-mer frequency distribution plot.