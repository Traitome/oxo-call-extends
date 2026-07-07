---
name: sfold
category: utility
description: sfold - Statistical Folding of Nucleic Acids
tags: ["sfold", "utility", "RNA-structure", "folding"]
author: oxo-call-community
source_url: "https://github.com/Ding-RNA-Lab/Sfold"
---

## Concepts

- **Tool Overview**: sfold (v2.2) provides statistical folding of nucleic acids.
- **Core Function**: Predicts RNA secondary structure using statistical methods.
- **Algorithm**: Uses partition function and base pairing probabilities.
- **Input/Output**: Accepts FASTA sequences and produces structure predictions.
- **RNA Folding**: Focuses on RNA secondary structure prediction.
- **Applications**: RNA structure analysis, functional RNA research, and bioinformatics.

## Pitfalls

- **Memory Usage**: High memory requirements for long sequences.
- **Performance**: May be slow for extremely long sequences.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Fold RNA
**Args:** `sfold -i rna.fasta -o structure.txt`
**Explanation:** `-i` input sequence; `-o` output structure.

### With constraints
**Args:** `sfold -i rna.fasta -c constraints.txt -o structure.txt`
**Explanation:** `-c` constraint file.

### Probability mode
**Args:** `sfold -i rna.fasta -p -o probabilities.txt`
**Explanation:** `-p` output base pairing probabilities.

### Verbose logging
**Args:** `sfold -v -i rna.fasta -o structure.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sfold --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sfold --version`
**Explanation:** Shows current version.

### Multiple sequences
**Args:** `sfold -i sequences.fasta -o structures/`
**Explanation:** Processes multiple sequences.