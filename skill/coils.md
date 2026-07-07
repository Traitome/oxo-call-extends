---
name: coils
category: qc
description: Prediction of coiled-coil regions in protein sequences
tags: [coils, protein-structure, coiled-coil, bioinformatics, structural-biology]
author: oxo-call-community
source_url: "https://rostlab.org/owiki/index.php/Packages#Package_overview"
---

## Concepts

- **Tool Overview**: COILS is a tool for predicting coiled-coil regions in protein sequences, using a probabilistic approach based on sequence patterns.
- **Core Function**: Identifies potential coiled-coil domains in protein sequences by analyzing heptad repeat patterns.
- **Algorithm**: Uses a sliding window approach with position-specific scoring matrices derived from known coiled-coil sequences.
- **Input**: Protein sequences in FASTA format.
- **Output**: Predicted coiled-coil regions with confidence scores.
- **Application**: Protein structure prediction, domain analysis, and functional annotation.
- **Installation**: Install via bioconda: `conda install -c bioconda coils`

## Pitfalls

- **Window Size**: Default window size may need adjustment for specific applications.
- **False Positives**: May predict coiled-coils in non-coiled-coil regions.
- **Sequence Quality**: Requires high-quality sequence data.
- **Heptad Repeat**: Relies on canonical heptad repeat patterns.
- **Complex Structures**: May miss complex coiled-coil arrangements.

## Examples

### Predict coiled-coil regions
**Args:** `coils -i protein.fasta -o coils_prediction.txt`
**Explanation:** Predicts coiled-coil regions in protein sequence.

### With custom window size
**Args:** `coils -i protein.fasta -w 21 -o coils_prediction.txt`
**Explanation:** Uses 21-residue window for prediction.

### Output probabilities
**Args:** `coils -i protein.fasta -p -o probabilities.txt`
**Explanation:** Outputs prediction probabilities for each position.

### Display help
**Args:** `coils --help`
**Explanation:** Shows all available options and usage information.