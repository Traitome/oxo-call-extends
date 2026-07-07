---
name: verticall
category: bioinformatics
description: Verticall - Vertical inheritance analysis.
tags: [verticall, phylogenetic-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/katholt/verticall"
---

## Concepts

- **Tool Overview**: Verticall - Vertical inheritance analysis tool.
- **Core Function**: Analyzes vertical transmission of genetic material.
- **Input**: Genome sequences.
- **Output**: Inheritance patterns.
- **Installation**: Install via pip or conda
- **Use Case**: Phylogenetic analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Analyze inheritance
**Args:** `verticall --ref ref.fasta --query query.fasta -o results/`
**Explanation:** Analyze vertical inheritance.

### With options
**Args:** `verticall --ref ref.fasta --query query.fasta -o results/ --threads 8`
**Explanation:** Use 8 threads.
