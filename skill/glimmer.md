---
name: glimmer
category: gene-prediction
description: glimmer - Gene finding system for microbial DNA.
tags: [glimmer, gene-prediction, microbial, gene-finder]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/glimmer/index.shtml"
---

## Concepts
- **Gene Finding**: Identifies genes in microbial DNA.
- **Interpolated Markov Models**: Uses IMMs for gene prediction.
- **Microbial Genomes**: Specialized for microbial genomes.
- **Sequence Analysis**: Analyzes DNA sequences.
- **ORF Detection**: Detects open reading frames.

## Pitfalls
- **Microbial Specificity**: Designed for microbial genomes.
- **Training Data**: May require training for new species.
- **Overlapping Genes**: May miss overlapping genes.
- **Memory Usage**: Large genomes require memory.
- **Result Validation**: Results should be validated.

## Examples
### Predict genes
**Args:** `glimmer3 genome.fasta -o predictions.gff3`
**Explanation:** Predicts genes in genome.

### With options
**Args:** `glimmer3 genome.fasta -l 100 -o predictions.gff3`
**Explanation:** Uses minimum gene length.

### Train model
**Args:** `glimmer3 -t training.fasta genome.fasta -o predictions.gff3`
**Explanation:** Uses trained model.

### Generate report
**Args:** `glimmer3 genome.fasta -r -o report.html`
**Explanation:** Generates prediction report.

### Batch processing
**Args:** `glimmer3 -l genomes.txt -o ./predictions/`
**Explanation:** Processes multiple genomes.