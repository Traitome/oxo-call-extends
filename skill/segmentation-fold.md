---
name: segmentation-fold
category: rna-analysis
description: segmentation-fold - RNA folding with predefined segments including K-turns and loop-E motifs
tags: ["segmentation-fold", "rna-analysis", "RNA-folding", "structure-prediction"]
author: oxo-call-community
source_url: "https://github.com/yhoogstrate/segmentation-fold"
---

## Concepts

- **Tool Overview**: segmentation-fold (v1.7.0) performs RNA folding with predefined segments including K-turns and loop-E motifs.
- **Core Function**: Predicts RNA secondary structure with specific structural motifs.
- **Algorithm**: Uses dynamic programming with predefined structural segment patterns.
- **Input/Output**: Accepts RNA sequences and produces structure predictions.
- **Motif Support**: Specifically handles K-turns and loop-E motifs.
- **Applications**: RNA structure prediction, riboswitch analysis, and ncRNA research.

## Pitfalls

- **Memory Usage**: High memory requirements for long sequences.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Sequence Length**: May have limitations on sequence length.
- **Motif Library**: Requires up-to-date motif library.
- **Documentation**: Some features have limited documentation.

## Examples

### Basic folding
**Args:** `segmentation-fold -i rna.fasta -o structure.dot`
**Explanation:** `-i` input FASTA; `-o` output dot-bracket notation.

### With motif library
**Args:** `segmentation-fold -i rna.fasta -m motifs.txt -o structure.dot`
**Explanation:** `-m` specifies custom motif library.

### Verbose logging
**Args:** `segmentation-fold -i rna.fasta -v -o structure.dot`
**Explanation:** `-v` enables verbose output for debugging.

### Output formats
**Args:** `segmentation-fold -i rna.fasta -f ct -o structure.ct`
**Explanation:** `-f ct` outputs in CT format.

### Help command
**Args:** `segmentation-fold --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `segmentation-fold --version`
**Explanation:** Shows current version.

### Energy calculation
**Args:** `segmentation-fold -i rna.fasta -e -o energy.txt`
**Explanation:** `-e` calculates folding energy.