---
name: nucleosome_prediction
category: epigenetics
description: Predicts nucleosome positions on genomic sequences using computational models.
tags: [nucleosome_prediction, epigenetics, chromatin, dna-packaging]
author: oxo-call-community
source_url: "https://genie.weizmann.ac.il/software/nucleo_prediction.html"
---

## Concepts

- **Tool Overview**: Predicts nucleosome positions on genomic DNA sequences.
- **Core Function**: Identifies likely nucleosome binding sites.
- **Algorithm**: Uses sequence-based features and machine learning models.
- **Input Format**: Accepts FASTA genomic sequences.
- **Output**: Produces predicted nucleosome positions and scores.
- **Use Case**: Epigenetics research, chromatin structure analysis, and gene regulation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Model Accuracy**: Predictions are probabilistic and may not be exact.
- **Sequence Context**: Results depend on local sequence context.
- **Species Specific**: Models may be species-specific.
- **Validation**: Results should be experimentally validated.
- **Computational Cost**: Large sequences can be computationally intensive.

## Examples

### Display help
**Args:** `nucleosome_prediction --help`
**Explanation:** Shows available options and usage instructions.

### Predict nucleosomes
**Args:** `nucleosome_prediction -i genome.fasta -o positions.txt`
**Explanation:** Predicts nucleosome positions on input sequence.

### Output BED
**Args:** `nucleosome_prediction -i genome.fasta -o positions.bed --bed`
**Explanation:** Outputs positions in BED format.

### Score threshold
**Args:** `nucleosome_prediction -i genome.fasta -t 0.8 -o positions.txt`
**Explanation:** Filters by prediction confidence threshold.

### Window size
**Args:** `nucleosome_prediction -i genome.fasta -w 147 -o positions.txt`
**Explanation:** Sets nucleosome window size to 147bp.

### Species model
**Args:** `nucleosome_prediction -i genome.fasta -s human -o positions.txt`
**Explanation:** Uses human-specific prediction model.

### Verbose mode
**Args:** `nucleosome_prediction -i genome.fasta -v -o positions.txt`
**Explanation:** Runs with verbose output.