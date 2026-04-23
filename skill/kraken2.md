---
name: kraken2
category: metagenomics
description: Kraken2 is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies.
tags: [kraken2, metagenomics]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/kraken2"
---

## Concepts

- **Tool Overview**: kraken2 v2.17.1 - Kraken2 is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies..
- **Core Function**: Kraken2 is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kraken2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Classify reads
**Args:** `--db /path/to/db --threads 8 --paired reads_1.fastq reads_2.fastq`
**Explanation:** Classifies paired-end reads against a Kraken2 database using 8 threads.

### Build database
**Args:** `kraken2-build --download-taxonomy --db mydb`
**Explanation:** Downloads taxonomy data for building a custom Kraken2 database.

