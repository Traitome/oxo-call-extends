---
name: metaeuk
category: annotation
description: MetaEuk - sensitive, high-throughput gene discovery and annotation for large-scale eukaryotic metagenomics
tags: [metaeuk, annotation, metagenomics, eukaryotic, gene-prediction]
author: oxo-call-community
source_url: "https://github.com/soedinglab/metaeuk"
---

## Concepts

- **Tool Overview**: MetaEuk is a sensitive, high-throughput tool for gene discovery and annotation in large-scale eukaryotic metagenomics datasets.
- **Core Function**: Identifies and annotates protein-coding genes in eukaryotic metagenomic sequences.
- **Sensitive Detection**: Designed for sensitive detection of eukaryotic genes even in complex metagenomic samples.
- **Large-scale Processing**: Optimized for processing large-scale metagenomic datasets efficiently.
- **Input/Output**: Accepts FASTA-formatted sequences; outputs gene predictions with functional annotations.
- **Homology-based Prediction**: Uses homology searches for accurate gene prediction and annotation.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Database Quality**: Annotation accuracy depends on reference database quality.
- **Sequence Quality**: Poor quality sequences may produce incorrect gene predictions.
- **Gene Density**: May miss genes in regions with low sequence coverage.
- **Alternative Splicing**: May not fully capture alternative splicing events.
- **Memory Requirements**: Memory usage can be high for large input datasets.

## Examples

### Predict genes in metagenome
**Args:** `metaeuk easy-predict contigs.fasta db/ genes.fasta annotations.gff`
**Explanation:** Predicts genes from metagenomic contigs using reference database.

### With custom database
**Args:** `metaeuk easy-predict contigs.fasta custom_db/ genes.fasta annotations.gff`
**Explanation:** Uses a custom protein database for gene prediction.

### Specify output format
**Args:** `metaeuk easy-predict contigs.fasta db/ genes.fasta annotations.gff --outfmt gff3`
**Explanation:** Outputs annotations in GFF3 format.

### Run with increased sensitivity
**Args:** `metaeuk easy-predict contigs.fasta db/ genes.fasta annotations.gff --sensitive`
**Explanation:** Runs in sensitive mode for detecting low-abundance genes.

### Parallel processing
**Args:** `metaeuk easy-predict contigs.fasta db/ genes.fasta annotations.gff --threads 16`
**Explanation:** Uses 16 threads for parallel processing.