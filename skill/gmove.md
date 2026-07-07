---
name: gmove
category: gene-prediction
description: gmove - Gene prediction tool for eukaryotic genomes.
tags: [gmove, gene-prediction, eukaryotic, annotation]
author: oxo-call-community
source_url: "https://github.com/institut-de-genomique/Gmove/blob/v1.3/README.md"
---

## Concepts
- **Gene Prediction**: Predicts protein-coding genes.
- **Eukaryotic Genomes**: Specialized for eukaryotic genomes.
- **Evidence Integration**: Integrates multiple evidence types.
- **Annotation**: Produces genome annotations.
- **Splice Prediction**: Predicts splice sites.

## Pitfalls
- **Species Specificity**: Best for trained species.
- **Evidence Quality**: Depends on evidence quality.
- **Complex Genes**: May miss complex gene structures.
- **Memory Usage**: Large genomes require memory.
- **Result Validation**: Results should be validated.

## Examples
### Predict genes
**Args:** `gmove -i genome.fasta -o predictions.gff3`
**Explanation:** Predicts genes in genome.

### With evidence
**Args:** `gmove -i genome.fasta -e evidence.bam -o predictions.gff3`
**Explanation:** Uses evidence for prediction.

### Train model
**Args:** `gmove -i genome.fasta -t training.txt -o predictions.gff3`
**Explanation:** Uses trained model.

### Generate report
**Args:** `gmove -i genome.fasta -o predictions.gff3 -r`
**Explanation:** Generates prediction report.

### Batch processing
**Args:** `gmove -l genomes.txt -o ./predictions/`
**Explanation:** Processes multiple genomes.