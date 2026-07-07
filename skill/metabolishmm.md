---
name: metabolishmm
category: annotation
description: Constructs phylogenies and performs functional annotations using HMM markers.
tags: [metabolishmm, phylogenomics, annotation]
author: oxo-call-community
source_url: "https://github.com/elizabethmcd/metabolisHMM"
---

## Concepts

- **Tool Overview**: metabolisHMM uses HMM markers for phylogenomics.
- **Core Function**: Phylogeny construction and annotation.
- **HMM Markers**: Uses hidden Markov models.
- **Phylogenetic Analysis**: Builds phylogenetic trees.
- **Functional Annotation**: Annotates gene functions.
- **Installation**: `conda install -c bioconda metabolishmm`

## Pitfalls

- **Memory Requirements**: High memory for large datasets.
- **Computation Time**: Slow for complex analyses.
- **HMM Database**: Requires HMM profiles.
- **Parameter Tuning**: Requires careful configuration.
- **Sequence Quality**: Depends on input sequence quality.
- **Result Interpretation**: Complex output requires expertise.

## Examples

### Run analysis
**Args:** `metabolishmm -i sequences.fasta -o results/`
**Explanation:** Runs phylogenomics analysis.

### With custom HMMs
**Args:** `metabolishmm -i sequences.fasta -m custom.hmm -o results/`
**Explanation:** Uses custom HMM profiles.

### Build phylogeny
**Args:** `metabolishmm -i sequences.fasta --tree -o tree.nwk`
**Explanation:** Constructs phylogenetic tree.

### Functional annotation
**Args:** `metabolishmm -i sequences.fasta --annotate -o annotations.txt`
**Explanation:** Performs functional annotation.

### Help documentation
**Args:** `metabolishmm --help`
**Explanation:** Displays available options.
