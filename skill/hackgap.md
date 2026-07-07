---
name: hackgap
category: bioinformatics
description: hackgap is a fast JIT-compiled k-mer counter that supports gapped k-mers for sequence analysis.
tags: [hackgap, k-mer, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.com/rahmannlab/hackgap"
---

## Concepts

- **K-mer Counting**: hackgap counts k-mers in sequence data efficiently.

- **Gapped K-mers**: Supports k-mers with gaps for flexible pattern matching.

- **JIT Compilation**: Utilizes just-in-time compilation for speed.

- **Hash-based Counting**: Uses hash tables for efficient k-mer storage.

- **Sequence Analysis**: Enables analysis of genomic sequences.

- **Pattern Discovery**: Identifies sequence patterns and motifs.

## Pitfalls

- **Memory Usage**: Large k-mer sizes may require significant memory.

- **K-mer Size**: Optimal k-mer size depends on application.

- **Sequence Quality**: Low-quality sequences may affect results.

- **Performance Tuning**: May require parameter optimization.

- **Output Size**: Large datasets may produce large output files.

## Examples

### Count k-mers
**Args:** `hackgap -i input.fastq -k 21 -o kmers.txt`
**Explanation:** Counts 21-mers in FASTQ file.

### Gapped k-mers
**Args:** `hackgap -i input.fastq -k 15 -g 3 -o gapped_kmers.txt`
**Explanation:** Counts gapped k-mers with 3 gaps.

### Paired-end reads
**Args:** `hackgap -i reads_1.fastq -i2 reads_2.fastq -k 25 -o kmers.txt`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `for f in *.fastq; do hackgap -i $f -k 21 -o ${f%.fastq}_kmers.txt; done`
**Explanation:** Processes multiple FASTQ files.

### With quality filtering
**Args:** `hackgap -i input.fastq -k 21 -q 30 -o kmers.txt`
**Explanation:** Filters reads by quality score.

### Generate histogram
**Args:** `hackgap -i input.fastq -k 21 -hist -o histogram.txt`
**Explanation:** Generates k-mer frequency histogram.

### Help command
**Args:** `hackgap --help`
**Explanation:** Shows available options and usage information.