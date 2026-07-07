---
name: seqfold
category: structure-prediction
description: seqfold - Predict nucleic acid secondary structure and minimum free energy
tags: ["seqfold", "structure-prediction", "RNA", "DNA"]
author: oxo-call-community
source_url: "https://github.com/Lattice-Automation/seqfold"
---

## Concepts

- **Tool Overview**: seqfold (v0.9.0) predicts minimum free energy and structure of nucleic acids.
- **Core Function**: Predicts RNA/DNA secondary structure using energy minimization.
- **Algorithm**: Implements nearest neighbor thermodynamic model for folding.
- **Input/Output**: Accepts FASTA/sequence files and produces structure predictions.
- **Structure Prediction**: Focuses on nucleic acid secondary structure prediction.
- **Applications**: RNA structure analysis, primer design, and nucleic acid research.

## Pitfalls

- **Sequence Length**: Limited accuracy for very long sequences.
- **Memory Usage**: High memory requirements for complex structures.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on input sequence quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Predict structure
**Args:** `seqfold -i sequence.fasta -o structure.txt`
**Explanation:** `-i` input FASTA; `-o` output structure file.

### RNA folding
**Args:** `seqfold -i rna.fasta -t rna -o structure.txt`
**Explanation:** `-t rna` specifies RNA folding.

### DNA folding
**Args:** `seqfold -i dna.fasta -t dna -o structure.txt`
**Explanation:** `-t dna` specifies DNA folding.

### Verbose logging
**Args:** `seqfold -i sequence.fasta -v -o structure.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqfold --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqfold --version`
**Explanation:** Shows current version.

### Output dot-bracket
**Args:** `seqfold -i sequence.fasta -f dotbracket -o structure.txt`
**Explanation:** `-f dotbracket` outputs in dot-bracket notation.