---
name: b2btools
category: annotation
description: B2BTools - Bio2Byte software suite for predicting protein biophysical properties
tags: [protein-prediction, dynamics, disorder, aggregation, phase-separation]
author: oxo-call-community
source_url: "https://bitbucket.org/bio2byte/b2btools_releases"
---

## Concepts

- **Tool Overview**: B2BTools predicts protein biophysical properties from sequence, including backbone dynamics, disorder, early folding, aggregation propensity, and phase separation.

- **Multiple Predictors**: Includes Dynamine (backbone dynamics), Disomine (disorder), EfoldMine (early folding), AgMata (aggregation), PSPer (phase separation), and ShiftCrypt (chemical shift encoding).

- **Sequence-Based**: All predictions use only amino acid sequence as input, no structural data required.

- **Biophysical Focus**: Predicts properties related to protein behavior rather than structure, complementing structure prediction tools.

## Pitfalls

- **Prediction Limits**: Predictions are probabilistic, not deterministic. Experimental validation recommended.

- **Sequence Length**: Very long or very short sequences may have reduced prediction accuracy.

- **Post-Translational Modifications**: Does not account for PTMs that may affect biophysical properties.

- **Training Data**: Predictions based on available training data. Novel protein types may have lower accuracy.

## Examples

### Predict backbone dynamics
**Args:** `dynamine prediction --input proteins.fasta --output dynamics.tsv`
**Explanation:** Predicts protein backbone dynamics (flexibility) from amino acid sequences.

### Predict protein disorder
**Args:** `disomine prediction --input proteins.fasta --output disorder.tsv`
**Explanation:** Predicts intrinsically disordered regions using dynamics and secondary structure features.

### Predict aggregation propensity
**Args:** `agmata prediction --input proteins.fasta --output aggregation.tsv`
**Explanation:** Predicts beta-aggregation prone regions in protein sequences.

### Predict phase separation
**Args:** `psper prediction --input proteins.fasta --output phase_separation.tsv`
**Explanation:** Predicts proteins likely to undergo liquid-liquid phase separation.

### Run all predictors
**Args:** `b2btools predict --input proteins.fasta --output results/ --all`
**Explanation:** Runs all available predictors on input protein sequences.
