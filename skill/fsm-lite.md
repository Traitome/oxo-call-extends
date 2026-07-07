---
name: fsm-lite
category: expression
description: Frequency-based String Mining (lite) - count k-mers in populations of genomes.
tags: [fsm-lite, k-mer counting, frequency analysis, genomics]
author: oxo-call-community
source_url: "https://github.com/nvalimak/fsm-lite"
---

## Concepts
- **K-mer Counting**: Counts k-mer frequencies in genomic sequences.
- **Population Analysis**: Analyzes k-mer frequencies across multiple genomes.
- **Single-core Implementation**: Lightweight single-threaded implementation.
- **FASTA Input**: Accepts FASTA format sequence files.
- **Frequency Profiling**: Generates k-mer frequency profiles.

## Pitfalls
- **Single-core Only**: No parallel processing support.
- **Memory Requirements**: High memory usage for large k-mer sizes.
- **K-mer Size**: Limited k-mer size range.
- **Output Size**: May generate large output files.
- **Format Limitations**: Only supports FASTA input.

## Examples
### Count k-mers in genome
**Args:** `fsm-lite -i genome.fasta -k 21 -o kmers.txt`
**Explanation:** Counts 21-mers in the genome.

### Multiple genomes
**Args:** `fsm-lite -i genome1.fasta genome2.fasta -k 31 -o kmers.txt`
**Explanation:** Counts k-mers across multiple genomes.

### With abundance threshold
**Args:** `fsm-lite -i genome.fasta -k 21 -t 10 -o kmers.txt`
**Explanation:** Only outputs k-mers with count >= 10.

### Output binary format
**Args:** `fsm-lite -i genome.fasta -k 21 -b -o kmers.bin`
**Explanation:** Outputs in binary format for efficiency.

### Count with quality filter
**Args:** `fsm-lite -i genome.fasta -k 21 -q 20 -o kmers.txt`
**Explanation:** Filters low-quality bases before counting.