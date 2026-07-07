---
name: conterminator
category: qc
description: Detect contamination in large sequence datasets
tags: [conterminator, contamination, quality-control, sequence-analysis, metagenomics]
author: oxo-call-community
source_url: "https://github.com/martin-steinegger/conterminator"
---

## Concepts

- **Tool Overview**: Conterminator is software designed to detect contamination in large sequence datasets, particularly useful for genome assemblies and metagenomic data.
- **Core Function**: Identifies contaminated sequences by comparing against reference databases and detecting anomalous sequence characteristics.
- **Algorithm**: Uses k-mer based similarity search and taxonomic classification to identify foreign sequences.
- **Input**: Sequence assemblies in FASTA format or raw reads.
- **Output**: Contamination report with identified contaminants and confidence scores.
- **Application**: Genome assembly QC, metagenomic bin validation, and sequence dataset cleaning.
- **Installation**: Install via bioconda: `conda install -c bioconda conterminator`

## Pitfalls

- **Database Completeness**: Detection depends on reference database coverage.
- **Threshold Settings**: Sensitivity vs specificity trade-off in contamination detection.
- **Horizontal Gene Transfer**: May flag genuine HGT events as contamination.
- **Closely Related Species**: Difficult to distinguish contamination from closely related organisms.
- **Sequence Length**: Short sequences may produce unreliable classifications.

## Examples

### Detect contamination in assemblies
**Args:** `conterminator -i assembly.fasta -o contamination_report/`
**Explanation:** Scans genome assembly for contaminated sequences.

### With custom database
**Args:** `conterminator -i assembly.fasta -d custom_db/ -o contamination_report/`
**Explanation:** Uses custom reference database for contamination detection.

### Set contamination threshold
**Args:** `conterminator -i assembly.fasta -t 0.95 -o contamination_report/`
**Explanation:** Sets 95% identity threshold for contamination detection.

### Display help
**Args:** `conterminator --help`
**Explanation:** Shows all available options and usage information.