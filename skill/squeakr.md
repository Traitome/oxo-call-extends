---
name: squeakr
category: kmer-analysis
description: Squeakr - Exact and approximate k-mer counting system
tags: [squeakr, kmer-analysis, kmer-counting, bioinformatics, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/splatlab/squeakr"
---

## Concepts

- **Tool Overview**: squeakr (v0.8) - A k-mer counting system
- **Core Function**: Provides exact and approximate k-mer counting for sequence data
- **Input/Output**: Accepts sequence files; outputs k-mer counts
- **Algorithm**: Squeakr k-mer counting algorithm
- **Installation**: `conda install -c bioconda squeakr`
- **Key Features**: K-mer counting, exact and approximate, fast processing

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence files
- **K-mer Size**: K-mer size affects counting accuracy and memory
- **Memory Usage**: Large k-mer sets require significant memory
- **Counting Mode**: Exact vs approximate affects accuracy and speed
- **Output Format**: Output format depends on configuration
- **Counting Accuracy**: Accuracy depends on k-mer size and mode

## Examples

### Display help
**Args:** `squeakr --help`
**Explanation:** Shows available options and usage information.

### Basic k-mer counting
**Args:** `squeakr -i sequences.fasta -o kmer_counts.sqk`
**Explanation:** Count k-mers in sequences.

### With k-mer size
**Args:** `squeakr -i sequences.fasta -o kmer_counts.sqk -k 31`
**Explanation:** Set k-mer size for counting.

### With counting mode
**Args:** `squeakr -i sequences.fasta -o kmer_counts.sqk --mode exact`
**Explanation:** Set counting mode (exact/approximate).

### Multiple files
**Args:** `squeakr -i seq1.fasta seq2.fasta -o kmer_counts.sqk`
**Explanation:** Count k-mers from multiple files.

### Output detailed results
**Args:** `squeakr -i sequences.fasta -o kmer_counts.sqk --detailed`
**Explanation:** Output detailed k-mer information.

### Output statistics
**Args:** `squeakr -i sequences.fasta -o kmer_counts.sqk --stats`
**Explanation:** Output counting statistics.

### Generate report
**Args:** `squeakr -i sequences.fasta -o kmer_counts.sqk --report`
**Explanation:** Generate counting report.

### With threads
**Args:** `squeakr -i sequences.fasta -o kmer_counts.sqk -p 8`
**Explanation:** Use multiple threads for counting.