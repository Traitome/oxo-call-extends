---
name: tetyper
category: annotation
description: TETyper - Transposable Element typing and subfamily classification tool.
tags: [tetyper, transposable-element, classification, subfamily, te-annotation, typing]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/tetyper"
---

## Concepts

- **Tool Overview**: TETyper - A tool for typing and classifying transposable elements into subfamilies based on sequence similarity and characteristic mutations.
- **Core Function**: Classifies TE sequences at the subfamily level, identifying lineage-specific insertions and age-related mutations.
- **Input**: TE sequences in FASTA format, reference subfamily sequences.
- **Output**: Subfamily classification for each TE, mutation profiles, insertion age estimates.
- **Installation**: `pip install tetyper` or `conda install -c bioconda tetyper`
- **Use Case**: TE evolution studies, distinguishing polymorphic insertions, dating TE insertions.

## Pitfalls

- **Reference Quality**: Subfamily classification depends on quality of reference subfamily sequences.
- **Mutation Accumulation**: Age estimation assumes uniform mutation rates.

## Examples

### Type TEs
**Args:** `tetyper -i te_sequences.fasta -o subfamily_classification.tsv`
**Explanation:** Classify TE sequences into subfamilies.

### With age estimation
**Args:** `tetyper -i te.fasta --estimate-age -o results/`
**Explanation:** Classify TEs and estimate their insertion age.
