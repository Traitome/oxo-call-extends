---
name: jronn
category: formatting
description: JRONN is a Java implementation of the RONN algorithm for RNA secondary structure prediction.
tags: [jronn, formatting, RNA, secondary-structure, prediction]
author: oxo-call-community
source_url: "https://biojava.org/"
---

## Concepts

- **Tool Overview**: jronn (v7.1.0) - Java implementation of the RONN algorithm for RNA secondary structure prediction.
- **RNA Structure Prediction**: Predicts RNA secondary structure from sequence.
- **RONN Algorithm**: Uses the RONN (RNA Ortholog Nucleotide Neural Network) algorithm.
- **Java Implementation**: Provides Java API for integration with bioinformatics pipelines.
- **Multiple Sequences**: Supports batch processing of multiple RNA sequences.
- **Structure Output**: Outputs predicted structures in various formats.

## Pitfalls

- **Sequence Length**: Performance degrades with very long sequences.
- **Prediction Accuracy**: Accuracy varies by RNA type and length.
- **Memory Usage**: Large datasets require significant memory.
- **Java Version**: Requires specific Java version.
- **Training Data**: Model trained on specific RNA types may not generalize.
- **Output Format**: Different output formats have different information content.

## Examples

### Predict RNA secondary structure
**Args:** `jronn -i rna.fasta -o structure.dot`
**Explanation:** Predicts secondary structure and outputs in dot-bracket format.

### Batch processing
**Args:** `jronn -i sequences.fasta -o structures/`
**Explanation:** Processes multiple sequences from FASTA file.

### Output in BED format
**Args:** `jronn -i rna.fasta -o structure.bed --format bed`
**Explanation:** Outputs structure in BED format.

### Include confidence scores
**Args:** `jronn -i rna.fasta -o structure.dot --confidence`
**Explanation:** Includes confidence scores in output.

### Set prediction threshold
**Args:** `jronn -i rna.fasta -o structure.dot -t 0.5`
**Explanation:** Sets prediction probability threshold to 0.5.

### Show help
**Args:** `jronn --help`
**Explanation:** Displays available options and usage information.