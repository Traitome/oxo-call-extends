---
name: kmerinshort
category: expression
description: KmerInShort counts kmers from FASTA/FASTQ files for FEELnc pipeline
tags: [kmerinshort, expression, FEELnc, lncRNA, k-mer]
author: oxo-call-community
source_url: "https://github.com/rizkg/KmerInShort"
---

## Concepts

- **Short K-mer Counting**: Counts k-mers with length less than 15
- **FEELnc Integration**: Part of the FEELnc pipeline for lncRNA analysis
- **FASTA/FASTQ Support**: Processes both FASTA and FASTQ file formats
- **Batch Processing**: Handles multiple input files
- **Text Output**: Outputs results in human-readable text format
- **Efficient Algorithm**: Optimized for counting short k-mers

## Pitfalls

- **K-mer Length Limit**: Only supports k < 15, not suitable for longer k-mers
- **Memory Usage**: Large datasets can consume significant memory
- **Input Format**: Requires properly formatted input files
- **Duplicate Handling**: May count duplicate k-mers multiple times
- **Output Size**: Large k-mer sets produce large output files
- **Compatibility**: Specifically designed for FEELnc, may not suit other purposes

## Examples

### Count k-mers from FASTQ
**Args:** `KmerInShort -i reads.fastq -k 12 -o kmer_counts.txt`
**Explanation:** Counts 12-mers from FASTQ file.

### Process multiple files
**Args:** `KmerInShort -i file1.fastq file2.fastq -k 10 -o output.txt`
**Explanation:** Counts k-mers from multiple input files.

### Use file list
**Args:** `KmerInShort -l files.lst -k 12 -o kmer_counts.txt`
**Explanation:** Processes files listed in a text file.

### FASTA input
**Args:** `KmerInShort -i genome.fasta -k 14 -o kmer_counts.txt`
**Explanation:** Counts k-mers from FASTA genome file.

### Filter by count
**Args:** `KmerInShort -i reads.fastq -k 12 -o output.txt --min-count 2`
**Explanation:** Only outputs k-mers with count >= 2.

### Verbose output
**Args:** `KmerInShort -i reads.fastq -k 12 -o output.txt -v`
**Explanation:** Provides verbose output during processing.