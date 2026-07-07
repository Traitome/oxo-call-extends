---
name: kractor
category: metagenomics
description: Extract reads from FASTQ files based on Kraken2 taxonomic classification
tags: [kractor, metagenomics, Kraken2, read-extraction, taxonomic-classification]
author: oxo-call-community
source_url: "https://github.com/Sam-Sims/kractor"
---

## Concepts

- **Read Extraction**: Extracts reads based on taxonomic classification
- **Kraken2 Integration**: Uses Kraken2 for taxonomic assignment
- **FASTQ Processing**: Handles FASTQ format read files
- **Targeted Analysis**: Enables targeted metagenomics
- **Paired-end Support**: Supports both single and paired-end reads
- **Flexible Taxonomic Ranks**: Extract reads at any taxonomic level

## Pitfalls

- **Kraken2 Dependency**: Requires pre-installed Kraken2 database
- **Classification Accuracy**: Depends on Kraken2 classification accuracy
- **Database Coverage**: Limited by reference database completeness
- **Memory Requirements**: Large Kraken2 databases require significant memory
- **Read Quality**: Low-quality reads may be misclassified
- **Threshold Selection**: Classification threshold affects extraction

## Examples

### Extract reads by taxon
**Args:** `kractor extract -i reads.fastq -t "Escherichia coli" -o extracted/`
**Explanation:** Extracts reads classified as E. coli.

### Specify taxonomic rank
**Args:** `kractor extract -i reads.fastq --taxon "Proteobacteria" --rank phylum -o results/`
**Explanation:** Extracts reads at phylum level.

### Paired-end mode
**Args:** `kractor extract -1 reads_1.fastq -2 reads_2.fastq -t "Staphylococcus" -o results/`
**Explanation:** Extracts paired reads for Staphylococcus.

### Confidence threshold
**Args:** `kractor extract -i reads.fastq -t "Bacteria" --min-score 2.0 -o results/`
**Explanation:** Uses minimum confidence score for extraction.

### Batch extraction
**Args:** `kractor batch -d samples/ -t "Viruses" -o results/`
**Explanation:** Extracts viral reads from multiple samples.

### Exclude taxon
**Args:** `kractor extract -i reads.fastq -t "Homo sapiens" --exclude -o results/`
**Explanation:** Extracts non-human reads by exclusion.