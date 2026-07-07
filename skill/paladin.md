---
name: paladin
category: alignment
description: PALADIN is a protein sequence alignment tool for functional characterization of metagenomes.
tags: [paladin, alignment, metagenomics, protein]
author: oxo-call-community
source_url: "https://github.com/ToniWestbrook/paladin"
---

## Concepts

- **Tool Overview**: PALADIN aligns metagenomic reads to protein databases.
- **Core Function**: Performs protein-level alignment for metagenomics.
- **Algorithm**: Uses BLAST-like alignment optimized for metagenomics.
- **Input Format**: Accepts FASTQ reads and protein databases.
- **Output**: Produces alignment results and functional annotations.
- **Use Case**: Metagenomics, functional profiling, and protein characterization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Database Size**: May require large protein databases.
- **Speed**: May be slower than nucleotide aligners.
- **Sensitivity**: May miss distant homologs.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paladin --help`
**Explanation:** Shows available options and usage instructions.

### Align reads
**Args:** `paladin align -i reads.fastq -d nr -o results.sam`
**Explanation:** Aligns reads to NCBI nr database.

### Build index
**Args:** `paladin index -d proteins.fasta -o index/`
**Explanation:** Creates index for protein database.

### With custom database
**Args:** `paladin align -i reads.fastq -d my_db -o results.sam`
**Explanation:** Uses custom protein database.

### Verbose mode
**Args:** `paladin align -v -i reads.fastq -d nr -o results.sam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `paladin align -t 16 -i reads.fastq -d nr -o results.sam`
**Explanation:** Uses 16 threads for parallel processing.

### Output format
**Args:** `paladin align -i reads.fastq -d nr -o results.bam --bam`
**Explanation:** Outputs in BAM format.