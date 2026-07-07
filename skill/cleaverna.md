---
name: cleaverna
category: hpc
description: Machine learning-based tool for scoring DNAzyme cleavage sites in substrate RNA sequences
tags: [cleaverna, dnazyme, rna-cleavage, machine-learning, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/reyhaneh-tavakoli/CleaveRNA/blob/main/README.md"
---

## Concepts

- **Tool Overview**: CleaveRNA is an advanced machine learning-based computational tool for scoring candidate DNAzyme cleavage sites in substrate RNA sequences.
- **Core Function**: Predicts and scores potential DNAzyme cleavage sites using structural and thermodynamic features.
- **Algorithm**: Uses machine learning models trained on structural and thermodynamic features of RNA-DNAzyme interactions.
- **Input**: Substrate RNA sequences (FASTA) and DNAzyme sequences.
- **Output**: Cleavage site predictions with confidence scores.
- **Application**: RNA targeting, DNAzyme design, and functional RNA analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cleaverna`

## Pitfalls

- **Data Quality**: Requires high-quality RNA sequence data.
- **Model Training**: Performance depends on training data quality.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: May require adjustment of prediction parameters.
- **Sequence Length**: May have limitations on sequence length.

## Examples

### Score cleavage sites
**Args:** `cleaverna -i substrate_rna.fasta -d dnazyme.fasta -o predictions.txt`
**Explanation:** Scores candidate DNAzyme cleavage sites in substrate RNA.

### With custom model
**Args:** `cleaverna -i substrate_rna.fasta -d dnazyme.fasta -m custom_model.h5 -o predictions.txt`
**Explanation:** Uses custom-trained model for cleavage site prediction.

### Get top predictions
**Args:** `cleaverna -i substrate_rna.fasta -d dnazyme.fasta -n 10 -o top_predictions.txt`
**Explanation:** Outputs top 10 cleavage site predictions.

### Display help
**Args:** `cleaverna --help`
**Explanation:** Shows all available options and usage information.