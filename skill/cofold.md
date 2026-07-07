---
name: cofold
category: expression
description: RNA secondary structure prediction method that takes co-transcriptional folding into account
tags: [cofold, rna-structure, co-transcriptional, bioinformatics, rna-analysis]
author: oxo-call-community
source_url: "http://www.e-rna.org/cofold/"
---

## Concepts

- **Tool Overview**: CoFold is an RNA secondary structure prediction method that considers co-transcriptional folding, predicting RNA structures as they form during transcription.
- **Core Function**: Predicts RNA secondary structure while taking into account the process of transcription, providing more biologically relevant structures.
- **Algorithm**: Extends the Zuker algorithm to incorporate co-transcriptional folding constraints and kinetic folding effects.
- **Input**: RNA nucleotide sequence in FASTA or plain text format.
- **Output**: Predicted secondary structure in dot-bracket notation with free energy values.
- **Application**: RNA structure analysis, riboswitch prediction, and non-coding RNA studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cofold`

## Pitfalls

- **Sequence Length**: Computationally expensive for very long sequences.
- **Energy Parameters**: Depends on accurate energy parameters for predictions.
- **Pseudoknots**: Does not handle pseudoknots in secondary structure prediction.
- **Co-transcriptional Assumptions**: Assumes specific transcription rates and folding kinetics.
- **Memory Usage**: May require significant memory for complex structures.

## Examples

### Predict RNA secondary structure
**Args:** `cofold -i rna_sequence.fasta -o structure.out`
**Explanation:** Predicts RNA secondary structure considering co-transcriptional folding.

### With custom temperature
**Args:** `cofold -i rna_sequence.fasta -t 37 -o structure.out`
**Explanation:** Sets temperature to 37°C for folding prediction.

### Output dot-bracket format
**Args:** `cofold -i rna_sequence.fasta -f db -o structure.txt`
**Explanation:** Outputs structure in dot-bracket notation.

### Display help
**Args:** `cofold --help`
**Explanation:** Shows all available options and usage information.