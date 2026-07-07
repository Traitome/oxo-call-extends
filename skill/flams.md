---
name: flams
category: utility
description: "FLAMS is a machine learning tool for predicting lysine acylation sites and other post-translational modification sites in protein sequences."
tags: [flams, utility, bioinformatics, proteomics, lysine-acylation, prediction, machine-learning, post-translational-modification]
author: oxo-call-community
source_url: "https://github.com/hannelorelongin/FLAMS"
---

## Concepts
- **Tool Overview**: FLAMS (Find Lysine Acylation & other Modification Sites) is a machine learning-based predictor for lysine acylation sites and other post-translational modifications in proteins.
- **Core Function**: Predicts potential modification sites using sequence-based features and trained classifiers for various acylation types.
- **Supported Modifications**: Acetylation, succinylation, malonylation, crotonylation, butyrylation, and other lysine acylations.
- **Feature Engineering**: Extracts sequence context features, physicochemical properties, and structural information for prediction.
- **ML Framework**: Uses Random Forest classifiers trained on experimentally validated modification sites from public databases.
- **Confidence Scores**: Provides probability scores for each predicted site to assess prediction reliability.
- **Installation**: `conda install -c bioconda flams` or clone from GitHub. Requires Python 3.x, scikit-learn, biopython.

## Pitfalls
- **Training Data Bias**: Models trained on limited datasets may have bias towards well-studied proteins and organisms.
- **False Positives**: High prediction scores do not guarantee biological relevance. Experimental validation recommended.
- **Species Specificity**: Models trained on human data may not perform well on other species. Use species-specific models when available.
- **Sequence Context**: Prediction accuracy depends on sequence window size. Default window may miss important contextual information.
- **Modification Crosstalk**: Multiple modifications on the same lysine residue are not considered. Sites may have multiple potential modifications.
- **Structural Information**: Predictions are sequence-based only and do not incorporate 3D structural information which may affect modification likelihood.

## Examples
### Predict lysine acetylation sites
**Args:** `flams --input protein.fasta --modification acetylation --output predictions.csv`
**Explanation:** Predicts acetylation sites on protein sequences in FASTA file using pre-trained model.

### Predict multiple modification types
**Args:** `flams --input protein.fasta --modification acetylation,succinylation,malonylation --output predictions.csv`
**Explanation:** Predicts multiple modification types simultaneously and outputs combined results.

### Filter by confidence score
**Args:** `flams --input protein.fasta --modification acetylation --threshold 0.8 --output predictions.csv`
**Explanation:** Filters predictions to only include sites with confidence score >= 0.8 for higher precision.

### Batch processing with FASTA directory
**Args:** `flams --input-dir fasta_files/ --modification acetylation --output-dir results/`
**Explanation:** Processes all FASTA files in input directory and saves results to output directory.

### Generate visualization
**Args:** `flams --input protein.fasta --modification acetylation --plot --output plot.png`
**Explanation:** Generates visualization showing predicted modification sites mapped to protein sequences.
