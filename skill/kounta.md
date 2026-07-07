---
name: kounta
category: kmer
description: Generate multi-sample k-mer count matrix
tags: [kounta, kmer, k-mer, matrix, multi-sample]
author: oxo-call-community
source_url: "https://github.com/tseemann/kounta"
---

## Concepts

- **K-mer Counting**: Generates k-mer counts across multiple samples
- **Multi-sample Matrix**: Creates combined count matrices
- **Genomic Comparison**: Enables comparison of k-mer content
- **Presence/Absence**: Supports binary presence/absence analysis
- **Read Processing**: Handles raw sequencing reads
- **Efficient Storage**: Optimized storage of count matrices

## Pitfalls

- **K-mer Size**: K-mer size affects detection sensitivity
- **Memory Usage**: Large matrices require significant memory
- **Disk Space**: Count matrices can be very large
- **Abundance Threshold**: Threshold selection affects results
- **Sample Number**: More samples increase matrix complexity
- **Hash Collisions**: Hash collisions affect count accuracy

## Examples

### Generate count matrix
**Args:** `kounta -i samples.txt -o matrix.tsv`
**Explanation:** Generates k-mer count matrix from sample list.

### Specify k-mer size
**Args:** `kounta -i samples.txt -k 31 -o matrix.tsv`
**Explanation:** Uses k-mer size of 31 for counting.

### Set minimum count
**Args:** `kounta -i samples.txt -m 5 -o matrix.tsv`
**Explanation:** Only includes k-mers with count >= 5.

### Binary matrix mode
**Args:** `kounta -i samples.txt --binary -o presence_matrix.tsv`
**Explanation:** Generates binary presence/absence matrix.

### Paired-end reads
**Args:** `kounta -1 reads_1.txt -2 reads_2.txt -o matrix.tsv`
**Explanation:** Processes paired-end read files.

### Export counts
**Args:** `kounta -i samples.txt -o counts.tsv --export-all`
**Explanation:** Exports complete k-mer count table.