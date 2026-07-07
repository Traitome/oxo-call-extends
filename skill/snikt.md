---
name: snikt
category: qc
description: SNIKT - Identify and remove adapter/systemic contamination in metagenomic sequencing data
tags: [snikt, qc, metagenomics, contamination, adapter-removal]
author: oxo-call-community
source_url: "https://github.com/piyuranjan/SNIKT"
---

## Concepts

- **Tool Overview**: snikt (v0.5.0) - A tool for identifying and removing contamination in metagenomic data
- **Core Function**: Detects and removes adapter and systemic contamination from metagenomic sequences
- **Input/Output**: Accepts FASTQ reads; outputs cleaned reads and contamination reports
- **Algorithm**: Uses reference databases to identify and filter contamination
- **Installation**: `conda install -c bioconda snikt`
- **Key Features**: Contamination detection, adapter removal, metagenomics QC

## Pitfalls

- **Database Requirements**: Requires contamination reference databases
- **Input Format**: Requires properly formatted FASTQ files
- **Memory Usage**: Large datasets require significant memory
- **Detection Accuracy**: May miss novel contamination sources
- **Over-filtering**: May remove legitimate sequences
- **Database Updates**: Databases need regular updates

## Examples

### Display help
**Args:** `snikt --help`
**Explanation:** Shows available options and usage information.

### Basic contamination removal
**Args:** `snikt -i reads.fastq -o clean_reads.fastq`
**Explanation:** Remove contamination from reads.

### With contamination report
**Args:** `snikt -i reads.fastq -o clean_reads.fastq -r contamination_report.txt`
**Explanation:** Generate contamination report.

### With custom database
**Args:** `snikt -i reads.fastq -o clean_reads.fastq -d custom_db.fasta`
**Explanation:** Use custom contamination database.

### Paired-end processing
**Args:** `snikt -i reads_1.fastq reads_2.fastq -o clean_1.fastq clean_2.fastq`
**Explanation:** Process paired-end reads.

### With adapter removal
**Args:** `snikt -i reads.fastq -o clean_reads.fastq --remove-adapters`
**Explanation:** Remove adapters along with contamination.

### Filter by type
**Args:** `snikt -i reads.fastq -o clean_reads.fastq --filter-type human,adapter`
**Explanation:** Filter specific contamination types.

### Generate statistics
**Args:** `snikt -i reads.fastq -o clean_reads.fastq --stats`
**Explanation:** Generate contamination statistics.