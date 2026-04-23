---
name: balrog
category: annotation
description: Balrog - Universal protein model for prokaryotic gene prediction
tags: [gene-prediction, prokaryotes, protein-model, annotation]
author: oxo-call-community
source_url: "https://github.com/salzberg-lab/BalrogCPP"
---

## Concepts

- **Tool Overview**: Balrog is a prokaryotic gene prediction tool using a universal protein model, designed for accurate gene calling in bacterial and archaeal genomes.

- **Universal Model**: Uses a single trained model applicable across diverse prokaryotic species, avoiding species-specific training requirements.

- **Protein-Based**: Incorporates protein-level information for improved gene boundary prediction.

- **Speed**: Optimized C++ implementation for fast gene prediction on large genomes.

## Pitfalls

- **Prokaryotic Only**: Designed for bacteria and archaea. Not suitable for eukaryotic gene prediction.

- **Training Data**: Model trained on specific dataset. Novel organisms may have reduced accuracy.

- **Partial Genes**: May have difficulty with partial genes at contig boundaries.

## Examples

### Basic gene prediction
**Args:** `balrog --genome genome.fasta --output genes.gff`
**Explanation:** Predicts protein-coding genes in prokaryotic genome.

### Specify output format
**Args:** `balrog --genome genome.fasta --format gff3 --output genes.gff`
**Explanation:** Outputs gene predictions in GFF3 format.

### Predict with sequence output
**Args:** `balrog --genome genome.fasta --output genes.gff --sequences proteins.faa`
**Explanation:** Outputs both GFF annotation and predicted protein sequences.
