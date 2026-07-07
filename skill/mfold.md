---
name: mfold
category: utility
description: Mfold web server for nucleic acid folding and hybridization prediction.
tags: [mfold, utility, nucleic-acid]
author: oxo-call-community
source_url: "http://www.unafold.org/mfold/software/download-mfold.php"
---

## Concepts

- **Tool Overview**: Mfold v3.6 is a tool for nucleic acid folding and hybridization prediction.
- **Core Function**: Predicts secondary structures of nucleic acids.
- **RNA Folding**: Predicts RNA secondary structures based on thermodynamic principles.
- **DNA Folding**: Supports DNA secondary structure prediction.
- **Input/Output**: Accepts nucleic acid sequences; outputs predicted structures.
- **Thermodynamic Modeling**: Uses nearest-neighbor thermodynamic model for predictions.

## Pitfalls

- **Sequence Length**: May have limitations for very long sequences.
- **Computational Resources**: Processing complex structures may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for complex folding predictions.
- **Parameter Tuning**: May require parameter adjustment for optimal predictions.
- **Prediction Accuracy**: Predictions are based on thermodynamic models and may not always match experimental results.
- **Runtime**: Complex folding predictions can be time-consuming.

## Examples

### Predict RNA secondary structure
**Args:** `mfold -i sequence.fasta -o structure.txt`
**Explanation:** Predicts RNA secondary structure from sequence.

### DNA folding prediction
**Args:** `mfold -i dna_sequence.fasta -o structure.txt -d`
**Explanation:** Predicts DNA secondary structure.

### Custom temperature
**Args:** `mfold -i sequence.fasta -o structure.txt -t 37`
**Explanation:** Uses 37°C for folding prediction.

### Generate visualization
**Args:** `mfold -i sequence.fasta -o structure.txt -p plot.png`
**Explanation:** Generates structure visualization.

### Batch processing
**Args:** `mfold -i sequences/ -o structures/`
**Explanation:** Processes multiple sequences in batch mode.