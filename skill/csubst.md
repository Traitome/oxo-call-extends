---
name: csubst
category: utility
description: Tool for analyzing combinatorial codon substitutions in DNA sequences.
tags: [csubst, utility, codon, substitution, mutation, DNA-sequence]
author: oxo-call-community
source_url: "https://github.com/kfuku52/csubst/blob/v1.11.10/README.md"
---

## Concepts

- **Tool Overview**: csubst (v1.11.10+) is a tool for analyzing combinatorial codon substitutions and their effects on protein sequences.
- **Core Function**: Identifies potential codon substitutions, predicts their impact on protein structure and function, and calculates evolutionary metrics.
- **Input/Output**: Input: FASTA DNA sequences, codon alignment files. Output: Substitution matrices, effect predictions, evolutionary statistics.
- **Genetic Code**: Supports multiple genetic codes (standard, mitochondrial, chloroplast) for different organisms.
- **Key Features**: Codon usage analysis, substitution effect prediction (synonymous/nonsynonymous), evolutionary distance calculation.
- **Installation**: `conda install -c bioconda csubst`

## Pitfalls

- **Frame Shift**: Input sequences must be in-frame; out-of-frame sequences produce incorrect results.
- **Genetic Code**: Ensure correct genetic code is specified for non-standard organisms (e.g., mitochondria).
- **Ambiguous Bases**: N or ambiguous bases may affect substitution calculations; pre-process sequences to remove ambiguities.
- **Large Alignments**: Very large alignments may require significant computational resources.
- **Output Interpretation**: Substitution effects should be validated experimentally; tool provides predictions only.

## Examples

### Analyze codon substitutions
**Args:** `csubst -i input.fasta -o results/ --codon-table standard`
**Explanation:** Analyze codon substitutions in input sequences using the standard genetic code.

### Calculate evolutionary distances
**Args:** `csubst -i alignment.fasta -o distances.txt --mode distance`
**Explanation:** Calculate pairwise evolutionary distances from a codon alignment.

### Predict substitution effects
**Args:** `csubst -i input.fasta -o effects.txt --predict-effect`
**Explanation:** Predict functional effects of potential codon substitutions.
