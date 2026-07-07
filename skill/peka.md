---
name: peka
category: utility
description: peka analyzes kmers around locations of interest.
tags: [peka, utility, kmer, analysis]
author: oxo-call-community
source_url: "https://github.com/ulelab/peka"
---

## Concepts

- **Tool Overview**: peka analyzes kmer patterns.
- **Core Function**: Identifies kmers around target locations.
- **Algorithm**: Uses kmer frequency analysis.
- **Input Format**: Accepts location and sequence files.
- **Output**: Produces kmer analysis results.
- **Use Case**: Sequence analysis, motif discovery.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Location Quality**: Results depend on location accuracy.
- **Kmer Size**: Kmer size affects results.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peka --help`
**Explanation:** Shows available options and usage instructions.

### Analyze kmers
**Args:** `peka -i locations.bed -s sequences.fasta -o kmer_analysis.txt`
**Explanation:** Analyzes kmers around locations.

### With kmer size
**Args:** `peka -i locations.bed -s sequences.fasta -k 6 -o kmer_analysis.txt`
**Explanation:** Uses 6-mer for analysis.

### Verbose mode
**Args:** `peka -v -i locations.bed -s sequences.fasta -o kmer_analysis.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peka -t 4 -i locations.bed -s sequences.fasta -o kmer_analysis.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peka -i locations.bed -s sequences.fasta -o kmer_analysis.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peka -i locations.bed -s sequences.fasta -o kmer_analysis.txt --report report.html`
**Explanation:** Generates HTML report.