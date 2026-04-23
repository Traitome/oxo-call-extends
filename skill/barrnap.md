---
name: barrnap
category: annotation
description: Barrnap - Rapid ribosomal RNA prediction for bacteria, archaea, and eukaryotes
tags: [rrna-prediction, ribosomal-rna, annotation, bacteria, archaea]
author: oxo-call-community
source_url: "https://github.com/tseemann/barrnap"
---

## Concepts

- **Tool Overview**: Barrnap (BAcerial Ribosomal RNA Predictor) rapidly predicts ribosomal RNA genes (5S, 16S, 23S) in bacterial, archaeal, and eukaryotic genomes.

- **HMM-Based**: Uses HMMER hidden Markov models for accurate rRNA gene detection.

- **Multiple Kingdoms**: Supports bacterial, archaeal, and eukaryotic rRNA prediction with kingdom-specific models.

- **Speed**: Optimized for fast rRNA prediction, suitable for large-scale genome annotation.

## Pitfalls

- **Partial Genes**: May miss partial rRNA genes at contig boundaries.

- **Pseudogenes**: Does not distinguish functional rRNAs from pseudogenes.

- **Strand Prediction**: Always reports rRNAs on forward strand. Check actual strand in genome.

## Examples

### Basic rRNA prediction
**Args:** `barrnap --kingdom bac genome.fasta > rrna.gff`
**Explanation:** Predicts bacterial rRNA genes from genome assembly.

### Archaeal rRNA prediction
**Args:** `barrnap --kingdom arc genome.fasta > rrna.gff`
**Explanation:** Predicts archaeal rRNA genes using archaea-specific models.

### Eukaryotic rRNA prediction
**Args:** `barrnap --kingdom euk genome.fasta > rrna.gff`
**Explanation:** Predicts eukaryotic rRNA genes including 18S, 5.8S, 28S, and 5S.

### Reject short contigs
**Args:** `barrnap --kingdom bac --reject 0.5 genome.fasta > rrna.gff`
**Explanation:** Rejects rRNA predictions shorter than 50% of expected length.

### Multi-threaded processing
**Args:** `barrnap --kingdom bac --threads 8 genome.fasta > rrna.gff`
**Explanation:** Uses 8 threads for faster rRNA prediction on large genomes.
