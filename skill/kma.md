---
name: kma
category: alignment
description: KMA is a mapping method designed to map raw reads directly against redundant databases using seed and extend.
tags: [kma, alignment, mapping, metagenomics, database]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/kma"
---

## Concepts

- **Redundant Database Mapping**: Maps reads efficiently against large, redundant databases
- **Seed and Extend**: Uses k-mer seeding with extension for rapid alignment
- **Metagenomic Analysis**: Designed for metagenomic sample profiling
- **Template Clustering**: Clusters templates sharing sequence identity
- **Consensus Calling**: Generates consensus sequences from mappings
- **Multi-threaded**: Supports parallel processing for large datasets

## Pitfalls

- **Database Size**: Very large databases increase memory and time requirements
- **K-mer Size Selection**: K-mer size affects sensitivity and specificity
- **Redundancy Handling**: Redundant databases may cause ambiguous mappings
- **Score Threshold**: Threshold settings affect mapping sensitivity
- **Memory Usage**: Large databases require significant RAM
- **Database Indexing**: Initial database indexing can be time-consuming

## Examples

### Index database
**Args:** `kma_index -i reference.fasta -o db_name -t 4`
**Explanation:** Creates KMA index from reference sequences using 4 threads.

### Map reads to database
**Args:** `kma -i reads.fastq -o output -t_db db_name -t 4`
**Explanation:** Maps reads against indexed template database.

### Metagenomic profiling
**Args:** `kma -i metagenome.fastq -o results -t_db marker_db -mp`
**Explanation:** Performs metagenomic profiling against marker gene database.

### Single-end reads
**Args:** `kma -i reads.fastq -o output -t_db db_name -sp`
**Explanation:** Maps single-end reads to database.

### Paired-end reads
**Args:** `kma -i reads_1.fastq reads_2.fastq -o output -t_db db_name -p`
**Explanation:** Maps paired-end reads to template database.

### Generate consensus
**Args:** `kma -i reads.fastq -o consensus -t_db db_name -a`
**Explanation:** Generates consensus sequence from alignments.