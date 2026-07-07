---
name: metaphyler
category: metagenomics
description: Estimating Bacterial Composition from Metagenomic Sequences
tags: [metaphyler, metagenomics, bacterial-composition]
author: oxo-call-community
source_url: "http://metaphyler.cbcb.umd.edu/"
---

## Concepts

- **Tool Overview**: MetaPhyler v1.25 is a computational tool for estimating bacterial composition from metagenomic sequencing data.
- **Core Function**: Determines the relative abundance of bacterial taxa in metagenomic samples.
- **Phylogenetic Analysis**: Uses phylogenetic markers to classify sequences and estimate taxonomic composition.
- **Taxonomic Profiling**: Provides taxonomic profiles at multiple levels (phylum, class, order, family, genus, species).
- **Input/Output**: Accepts FASTA-formatted sequences; outputs taxonomic abundance estimates.
- **Reference Database**: Uses a comprehensive database of phylogenetic marker genes for classification.

## Pitfalls

- **Database Completeness**: Profiling accuracy depends on reference database completeness.
- **Sequence Quality**: Poor quality sequences may affect classification accuracy.
- **Low Abundance Detection**: May miss organisms present at very low abundance.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **False Positives**: May produce false positive identifications with closely related species.

## Examples

### Analyze metagenomic sequences
**Args:** `metaphyler -i sequences.fasta -o profile.txt`
**Explanation:** Estimates bacterial composition from input sequences.

### With custom database
**Args:** `metaphyler -i sequences.fasta -d custom_db/ -o profile.txt`
**Explanation:** Uses a custom reference database for classification.

### Specify output format
**Args:** `metaphyler -i sequences.fasta -o profile.txt -f csv`
**Explanation:** Outputs results in CSV format.

### Detailed taxonomic breakdown
**Args:** `metaphyler -i sequences.fasta -o profile.txt -v`
**Explanation:** Generates detailed taxonomic breakdown with verbose output.

### Batch processing
**Args:** `metaphyler -i fasta/ -o results/`
**Explanation:** Processes multiple FASTA files in batch mode.