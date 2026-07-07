---
name: typing
category: analysis
description: Typing - Tool for sequence typing and classification.
tags: [typing, sequence-typing, classification, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/compbio/typing"
---

## Concepts

- **Tool Overview**: Typing - A tool for sequence typing and classification of biological sequences.
- **Core Function**: Classifies sequences into predefined types or categories.
- **Input**: Sequence files (FASTA), typing database.
- **Output**: Sequence types, confidence scores, classification results.
- **Installation**: `pip install typing` or `conda install -c bioconda typing`
- **Use Case**: Sequence classification, strain typing, microbial identification.

## Pitfalls

- **Database Quality**: Results depend on typing database completeness.
- **Sequence Quality**: Requires good quality sequences.

## Examples

### Type sequences
**Args:** `typing -i sequences.fasta -d typing_database.fasta -o types.txt`
**Explanation:** Classify sequences into types.

### With confidence
**Args:** `typing -i reads.fastq -d database/ -c -o results/`
**Explanation:** Type sequences with confidence scores.
