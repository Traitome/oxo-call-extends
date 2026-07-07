---
name: mreps
category: variant-calling
description: Flexible and efficient software for identifying tandem repeats in DNA sequences.
tags: [mreps, variant-calling, repeats]
author: oxo-call-community
source_url: "http://mreps.univ-mlv.fr"
---

## Concepts

- **Tool Overview**: mreps v2.6.01 identifies tandem repeats in DNA sequences.
- **Core Function**: Detects serial/tandem repeats in genomic sequences.
- **Repeat Detection**: Specialized for tandem repeat identification.
- **Flexible Algorithm**: Supports various repeat patterns.
- **Efficient Search**: Optimized for speed and sensitivity.
- **Input/Output**: Accepts FASTA sequences; outputs repeat coordinates.

## Pitfalls

- **Memory Requirements**: Memory usage depends on sequence length.
- **Parameter Tuning**: May require parameter adjustment for detection.
- **Repeat Complexity**: Complex repeats may be missed.
- **Data Quality**: Results depend on sequence quality.
- **Computational Resources**: Large sequences may require significant resources.
- **False Positives**: May produce false positive predictions.

## Examples

### Find tandem repeats
**Args:** `mreps sequence.fasta -o repeats.txt`
**Explanation:** Identifies tandem repeats in sequence.

### With minimum repeat length
**Args:** `mreps sequence.fasta -min 10 -o repeats.txt`
**Explanation:** Sets minimum repeat unit length to 10.

### With maximum repeat length
**Args:** `mreps sequence.fasta -max 100 -o repeats.txt`
**Explanation:** Sets maximum repeat unit length to 100.

### Verbose output
**Args:** `mreps sequence.fasta -v -o repeats.txt`
**Explanation:** Shows detailed repeat information.

### Batch processing
**Args:** `mreps -i fasta/ -o results/`
**Explanation:** Processes multiple sequence files.