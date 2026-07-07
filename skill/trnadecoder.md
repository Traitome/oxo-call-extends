---
name: trnadecoder
category: analysis
description: tRNAdecoder - Tool for predicting tRNA genes from genomic sequences.
tags: [trnadecoder, trna, gene-prediction, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/trnadecoder"
---

## Concepts

- **Tool Overview**: tRNAdecoder - A tool for predicting tRNA genes from genomic sequences.
- **Core Function**: Identifies tRNA genes and predicts their anticodon sequences.
- **Input**: Genome sequences (FASTA), optional annotation files.
- **Output**: tRNA gene predictions, anticodon sequences, genomic coordinates.
- **Installation**: `pip install trnadecoder` or `conda install -c bioconda trnadecoder`
- **Use Case**: Genome annotation, tRNA analysis, comparative genomics.

## Pitfalls

- **Pseudogenes**: May predict tRNA pseudogenes.
- **Non-standard tRNAs**: May miss non-standard tRNA types.

## Examples

### Predict tRNAs
**Args:** `trnadecoder -i genome.fasta -o trna_predictions.gff`
**Explanation:** Predict tRNA genes from genome sequence.

### With output details
**Args:** `trnadecoder -i genome.fasta -d -o trnas/`
**Explanation:** Predict tRNAs with detailed output.
