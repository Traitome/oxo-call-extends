---
name: zorro
category: alignment
description: Probabilistic masking program for multiple sequence alignments
tags: [zorro, alignment, masking, phylogenetics, confidence-score]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/probmask/"
---

## Concepts

- **Tool Overview**: ZORRO is a probabilistic masking program that assigns confidence scores to each column in a multiple sequence alignment
- **Confidence Scoring**: Uses statistical models to assess alignment reliability
- **Phylogenetic Integration**: Scores can be used to filter unreliable alignment regions before phylogenetic inference
- **Automated Masking**: Removes subjectivity from manual masking by providing quantitative confidence values
- **Output Formats**: Produces confidence scores that can be used with RAxML and other phylogenetic tools
- **Installation**: `conda install -c bioconda zorro`

## Pitfalls

- **Input Requirements**: Requires pre-aligned sequences in FASTA or PHYLIP format
- **Score Interpretation**: Confidence scores are rational numbers; may need conversion for tools requiring integers
- **Alignment Quality**: Results depend on the quality of the input alignment
- **Computational Time**: May be slow for very large multiple sequence alignments

## Examples

### Calculate confidence scores
**Args:** `zorro -i alignment.fasta -o confidence.txt`
**Explanation:** Calculate confidence scores for each column in the alignment.

### Generate masked alignment
**Args:** `zorro -i alignment.fasta -o masked.fasta -c 0.5`
**Explanation:** Generate masked alignment, keeping only columns with confidence >= 0.5.

### Output weights for RAxML
**Args:** `zorro -i alignment.fasta -w weights.txt`
**Explanation:** Output weight file for use with RAxML's -a option.