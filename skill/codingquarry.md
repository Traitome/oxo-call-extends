---
name: codingquarry
category: expression
description: Highly accurate hidden Markov model gene prediction in fungal genomes using RNA-seq transcripts
tags: [codingquarry, gene-prediction, hidden-markov-model, fungal-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://sourceforge.net/p/codingquarry/"
---

## Concepts

- **Tool Overview**: CodingQuarry is a gene prediction tool specifically designed for fungal genomes, using hidden Markov models (HMMs) and integrating RNA-seq transcript data for improved accuracy.
- **Core Function**: Predicts gene structures in fungal genomes by combining ab initio prediction with RNA-seq evidence.
- **Algorithm**: Uses hidden Markov models to model gene structure, incorporating RNA-seq data to improve splice site prediction.
- **Input**: Fungal genome sequence in FASTA format, optional RNA-seq data.
- **Output**: Predicted gene structures in GFF or GenBank format.
- **Application**: Fungal genome annotation, comparative genomics, and transcriptomics.
- **Installation**: Install via bioconda: `conda install -c bioconda codingquarry`

## Pitfalls

- **Species Specificity**: Optimized for fungal genomes, may not perform well on other organisms.
- **RNA-seq Quality**: Depends on high-quality RNA-seq data for optimal results.
- **Genome Complexity**: May struggle with highly fragmented genomes.
- **Parameter Tuning**: May require adjustment for specific fungal species.
- **Memory Usage**: May require significant memory for large genomes.

## Examples

### Predict genes in fungal genome
**Args:** `CodingQuarry -g genome.fasta -o predictions.gff`
**Explanation:** Predicts genes in fungal genome using ab initio HMM-based approach.

### With RNA-seq evidence
**Args:** `CodingQuarry -g genome.fasta -r rnaseq.bam -o predictions.gff`
**Explanation:** Integrates RNA-seq data for improved gene prediction accuracy.

### With multiple RNA-seq samples
**Args:** `CodingQuarry -g genome.fasta -r sample1.bam -r sample2.bam -o predictions.gff`
**Explanation:** Uses multiple RNA-seq samples for better evidence support.

### Display help
**Args:** `CodingQuarry --help`
**Explanation:** Shows all available options and usage information.