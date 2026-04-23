---
name: kraken
category: metagenomics
description: Kraken is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies.
tags: [kraken, metagenomics]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/kraken"
---

## Concepts

- **Tool Overview**: kraken v1.1.1 - Kraken is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies..
- **Core Function**: Kraken is a system for assigning taxonomic labels to short DNA sequences, usually obtained through metagenomic studies.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kraken`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Classify reads
**Args:** `--db /path/to/db --threads 8 --fastq-input reads.fastq`
**Explanation:** Classifies reads against a Kraken database.

