---
name: kraken2
category: metagenomics
description: Kraken2 is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies.
tags: [kraken2, metagenomics, classification, taxonomy, sequencing]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/kraken2"
---

## Concepts

- **Tool Overview**: Kraken2 (v2.1.7+) is a fast and accurate taxonomic classifier for metagenomic sequencing reads. It uses k-mer based exact alignment to quickly assign taxonomic labels to DNA sequences.
- **Core Function**: Classifies short DNA reads by mapping k-mers to a pre-built database containing reference genomes from various taxa.
- **Input/Output**: Input: FASTQ reads (single-end or paired-end). Output: Classification report, sequence tags, and optional report files.
- **Algorithm**: Uses a compact hash table to store k-mer to taxon mappings, enabling fast lookup and classification.
- **Key Features**: Supports paired-end reads, custom databases, and provides confidence scoring for classifications.
- **Installation**: `conda install -c bioconda kraken2`

## Pitfalls

- **Database Requirements**: Requires a pre-built Kraken2 database. Default databases can be large (数十GB). Use `kraken2-build` to create custom databases.
- **Memory Usage**: Database loading requires significant memory. Consider using smaller databases or increasing memory allocation for large databases.
- **Read Length**: Kraken2 performs best with reads ≥50bp. Short reads may yield lower classification accuracy.
- **Database Updates**: Databases need regular updates to include new reference genomes and taxonomy changes.
- **False Positives**: May produce false positive classifications for highly conserved sequences. Use confidence thresholds to filter results.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Classify paired-end reads
**Args:** `--db /path/to/db --threads 8 --paired reads_1.fastq reads_2.fastq --output classifications.txt`
**Explanation:** Classifies paired-end reads against a Kraken2 database using 8 threads, outputting results to classifications.txt.

### Build a custom database
**Args:** `kraken2-build --download-taxonomy --db mydb`
**Explanation:** Downloads taxonomy data for building a custom Kraken2 database.

### Download reference sequences
**Args:** `kraken2-build --download-library bacteria --db mydb`
**Explanation:** Downloads bacterial reference sequences from NCBI for inclusion in the custom database.

### Build the database index
**Args:** `kraken2-build --build --db mydb --threads 8`
**Explanation:** Builds the Kraken2 database index from downloaded sequences using 8 threads.

### Generate summary report
**Args:** `--db /path/to/db --threads 8 --paired reads_1.fastq reads_2.fastq --output classifications.txt --report report.txt`
**Explanation:** Classifies reads and generates a comprehensive report with taxonomic composition statistics.

### Filter by confidence
**Args:** `--db /path/to/db --threads 8 --confidence 0.1 --paired reads_1.fastq reads_2.fastq --output filtered.txt`
**Explanation:** Classifies reads with a minimum confidence score of 0.1, reducing false positive classifications.

### Generate Kraken-style output
**Args:** `--db /path/to/db --threads 8 --paired reads_1.fastq reads_2.fastq --output-format kraken --output kraken_output.txt`
**Explanation:** Outputs results in the original Kraken (version 1) format for compatibility with downstream tools.