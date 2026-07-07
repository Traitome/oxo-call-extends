---
name: genomethreader
category: gene-prediction
description: GenomeThreader - Gene structure prediction using spliced alignments of cDNA/EST and protein sequences.
tags: [genomethreader, gene-prediction, spliced-alignment, bioinformatics]
author: oxo-call-community
source_url: "http://genomethreader.org/"
---

## Concepts
- **Gene Structure Prediction**: Predicts gene structures in genomes.
- **Spliced Alignment**: Aligns sequences with splice site awareness.
- **Similarity-Based Prediction**: Uses similarity to known sequences for prediction.
- **cDNA/EST Mapping**: Maps cDNA and EST sequences to genome.
- **Protein Alignment**: Aligns protein sequences to genome.

## Pitfalls
- **Alignment Quality**: Depends on accurate sequence alignment.
- **Intron Prediction**: May incorrectly predict intron boundaries.
- **Alternative Splicing**: May miss alternative splicing events.
- **Gene Coverage**: May miss genes with no homology.
- **Parameter Sensitivity**: Results sensitive to parameters.

## Examples
### Predict gene structures
**Args:** `gt -genome genome.fasta -cdna cdnas.fasta -o predictions.gff`
**Explanation:** Predicts gene structures from cDNA sequences.

### With protein sequences
**Args:** `gt -genome genome.fasta -protein proteins.fasta -o predictions.gff`
**Explanation:** Uses protein sequences for gene prediction.

### Combined prediction
**Args:** `gt -genome genome.fasta -cdna cdnas.fasta -protein proteins.fasta -o predictions.gff`
**Explanation:** Uses both cDNA and protein sequences.

### Generate report
**Args:** `gt -genome genome.fasta -cdna cdnas.fasta -r -o report.txt`
**Explanation:** Generates prediction report.

### Batch processing
**Args:** `gt -genome genome.fasta -cdna ./cdnas/ -o predictions.gff`
**Explanation:** Processes multiple cDNA files.