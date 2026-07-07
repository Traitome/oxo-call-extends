---
name: palikiss
category: alignment
description: pAliKiss predicts RNA secondary structures for multiple sequence alignments.
tags: [palikiss, alignment, rna-structure, pseudoknots]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/palikiss"
---

## Concepts

- **Tool Overview**: pAliKiss predicts RNA secondary structures from alignments.
- **Core Function**: Predicts secondary structures including pseudoknots.
- **Algorithm**: Uses comparative sequence analysis and energy minimization.
- **Input Format**: Accepts multiple sequence alignments.
- **Output**: Produces structure predictions in various formats.
- **Use Case**: RNA structure analysis, ncRNA research, and riboswitch prediction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Computational Cost**: Prediction can be computationally intensive.
- **Pseudoknot Complexity**: May miss complex pseudoknots.
- **Alignment Quality**: Results depend on input alignment quality.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `palikiss --help`
**Explanation:** Shows available options and usage instructions.

### Predict structure
**Args:** `palikiss -i alignment.fasta -o structure.txt`
**Explanation:** Predicts RNA secondary structure.

### With pseudoknots
**Args:** `palikiss -p -i alignment.fasta -o structure.txt`
**Explanation:** Enables pseudoknot prediction.

### Output format
**Args:** `palikiss -i alignment.fasta -o structure.dot --dot`
**Explanation:** Outputs in DOT format.

### Verbose mode
**Args:** `palikiss -v -i alignment.fasta -o structure.txt`
**Explanation:** Runs with verbose output.

### Energy threshold
**Args:** `palikiss -e -10 -i alignment.fasta -o structure.txt`
**Explanation:** Sets energy threshold.

### Number of threads
**Args:** `palikiss -t 4 -i alignment.fasta -o structure.txt`
**Explanation:** Uses 4 threads for parallel processing.