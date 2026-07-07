---
name: sourmash
category: sequence-analysis
description: Sourmash - Quickly search, compare, and analyze genomic data
tags: [sourmash, sequence-analysis, k-mer, comparison, search, signatures]
author: oxo-call-community
source_url: "https://sourmash.readthedocs.io/"
---

## Concepts

- **Tool Overview**: sourmash (v4.9.4) - A genomic data search and comparison tool
- **Core Function**: Searches, compares, and analyzes genomic and metagenomic data
- **Input/Output**: Accepts FASTA/FASTQ; outputs k-mer signatures and comparisons
- **Algorithm**: Uses MinHash sketches for efficient comparison
- **Installation**: `conda install -c bioconda sourmash`
- **Key Features**: K-mer signatures, genome comparison, fast search

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTA/FASTQ files
- **K-mer Size**: K-mer size affects signature quality
- **Sketch Size**: Sketch size affects comparison accuracy
- **Memory Usage**: Large genomes require significant memory
- **Database**: Requires database for searching
- **Output Format**: Output format depends on analysis type

## Examples

### Display help
**Args:** `sourmash --help`
**Explanation:** Shows available options and usage information.

### Create signature
**Args:** `sourmash sketch dna -k 31 genome.fasta -o genome.sig`
**Explanation:** Create k-mer signature from genome.

### Compare signatures
**Args:** `sourmash compare genome1.sig genome2.sig -o comparison.csv`
**Explanation:** Compare two genome signatures.

### Search database
**Args:** `sourmash search genome.sig database/ -o matches.csv`
**Explanation:** Search signature against database.

### Gather metagenome
**Args:** `sourmash gather metagenome.sig database/ -o gather.csv`
**Explanation:** Gather components from metagenome.

### Index database
**Args:** `sourmash index database.sbt genome1.sig genome2.sig`
**Explanation:** Create searchable database index.

### Compute abundance
**Args:** `sourmash sketch dna -k 31 --abundance reads.fastq -o abundance.sig`
**Explanation:** Create abundance-weighted signature.

### Plot comparison
**Args:** `sourmash plot comparison.csv -o comparison.png`
**Explanation:** Plot comparison results.