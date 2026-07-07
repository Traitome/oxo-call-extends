---
name: cherri
category: rna
description: Accurate detection of functional RNA-RNA interaction sites
tags: [cherri, rna-rna-interaction, bioinformatics, rna-structure, prediction]
author: oxo-call-community
source_url: "https://github.com/BackofenLab/Cherri"
---

## Concepts

- **Tool Overview**: Cherri is a computational tool for accurately detecting functional RNA-RNA interaction sites.
- **Core Function**: Predicts RNA-RNA interaction sites using machine learning and structural information.
- **Algorithm**: Combines sequence features, structural information, and machine learning models for prediction.
- **Input**: RNA sequences or structures in various formats.
- **Output**: Predicted interaction sites with confidence scores.
- **Application**: RNA biology research, regulatory RNA analysis, and RNA structure-function studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cherri`

## Pitfalls

- **Sequence Quality**: Requires high-quality RNA sequences.
- **Structural Information**: Performance improves with structural data.
- **Model Training**: Models trained on specific datasets may not generalize.
- **Computational Time**: May be slow for large RNA sequences.
- **False Positives**: May produce false positive predictions.

## Examples

### Predict RNA-RNA interactions
**Args:** `cherri -a rna_a.fasta -b rna_b.fasta -o interactions.txt`
**Explanation:** Predicts interaction sites between two RNA sequences.

### With structure input
**Args:** `cherri -a rna_a.struct -b rna_b.struct -o interactions.txt`
**Explanation:** Uses structural information for improved predictions.

### Output detailed results
**Args:** `cherri -a rna_a.fasta -b rna_b.fasta -o interactions.txt -v`
**Explanation:** Generates detailed output with confidence scores.

### Display help
**Args:** `cherri --help`
**Explanation:** Shows all available options and usage information.