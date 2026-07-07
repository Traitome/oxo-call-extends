---
name: metagene_annotator
category: utility
description: MetaGeneAnnotator is a gene-finding program for prokaryote and phage
tags: [metagene_annotator, utility, gene-prediction, prokaryote]
author: oxo-call-community
source_url: "http://metagene.nig.ac.jp/"
---

## Concepts

- **Tool Overview**: MetaGeneAnnotator v1.0 is a gene-finding program specifically designed for prokaryotes and phages.
- **Core Function**: Identifies protein-coding genes in prokaryotic and phage genomes.
- **Prokaryotic Focus**: Optimized for prokaryotic gene structures including operons and Shine-Dalgarno sequences.
- **Phage Support**: Capable of identifying genes in phage genomes with high accuracy.
- **Input/Output**: Accepts FASTA-formatted genome sequences; outputs gene predictions in various formats.
- **High Accuracy**: Designed for high-precision gene prediction in microbial genomes.

## Pitfalls

- **Eukaryotic Limitations**: Not suitable for eukaryotic gene prediction.
- **Sequence Quality**: Poor quality sequences may affect prediction accuracy.
- **Gene Density**: May miss genes in regions with unusual gene density.
- **Overlapping Genes**: May have difficulty with overlapping genes.
- **Parameter Sensitivity**: Results may vary with different parameter settings.
- **Annotation Updates**: Does not automatically update annotations as new data becomes available.

## Examples

### Predict genes in genome
**Args:** `mgap -i genome.fasta -o genes.gff`
**Explanation:** Predicts genes from prokaryotic genome sequence.

### Output in GenBank format
**Args:** `mgap -i genome.fasta -o genes.gbk -f genbank`
**Explanation:** Outputs gene predictions in GenBank format.

### With custom parameters
**Args:** `mgap -i genome.fasta -o genes.gff -p params.txt`
**Explanation:** Uses custom parameters for gene prediction.

### Phage gene prediction
**Args:** `mgap -i phage.fasta -o phage_genes.gff -phage`
**Explanation:** Optimizes gene prediction for phage genomes.

### Batch processing
**Args:** `mgap -i genomes/ -o predictions/`
**Explanation:** Processes multiple genome files in batch.