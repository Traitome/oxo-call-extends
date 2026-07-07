---
name: stopfree
category: rna-analysis
description: Rust implementation of the stopFree coding potential tool for identifying non-coding RNAs.
tags: [stopfree, coding-potential, non-coding-rna, bioinformatics]
author: oxo-call-community
source_url: "https://pypi.org/project/stopfree/"
---

## Concepts

- **Tool Overview**: stopfree (v0.2.4) is a fast tool for assessing the coding potential of RNA sequences.
- **Core Function**: Predicts whether RNA sequences are coding or non-coding based on stop codon frequency analysis.
- **Algorithm**: Analyzes stop codon patterns and sequence features to determine coding potential.
- **Input/Output**: Input: FASTA sequences; Output: Coding potential scores for each sequence.
- **Applications**: Identifying non-coding RNAs, filtering coding sequences from transcriptome data.
- **Installation**: `conda install -c bioconda stopfree` or `pip install stopfree`.

## Pitfalls

- **Sequence Quality**: Low-quality sequences affect prediction accuracy.
- **Sequence Length**: Very short sequences produce unreliable predictions.
- **Training Data**: Model trained on specific organisms may not generalize.
- **Threshold Selection**: Incorrect thresholds affect classification.
- **Frame Detection**: Incorrect reading frame assignment affects results.
- **Strand Orientation**: Strand information affects prediction accuracy.

## Examples

### Display help
**Args:** `stopfree --help`
**Explanation:** Shows available options and usage information.

### Basic coding potential analysis
**Args:** `stopfree -i sequences.fasta -o results.txt`
**Explanation:** Predict coding potential for input sequences.

### With strand information
**Args:** `stopfree -i sequences.fasta -o results.txt -s +`
**Explanation:** Specify strand orientation for analysis.

### Verbose mode
**Args:** `stopfree -i sequences.fasta -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output probabilities
**Args:** `stopfree -i sequences.fasta -o results.txt --probabilities`
**Explanation:** Output probability scores for each sequence.

### Filter by threshold
**Args:** `stopfree -i sequences.fasta -o results.txt -c 0.5`
**Explanation:** Filter sequences with coding potential below 0.5.

### Batch processing
**Args:** `stopfree -i batch/ -o results/`
**Explanation:** Process multiple FASTA files together.

### Custom model
**Args:** `stopfree -i sequences.fasta -o results.txt -m custom_model`
**Explanation:** Use custom-trained model for prediction.

### Generate report
**Args:** `stopfree -i sequences.fasta -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
