---
name: cerberus-x
category: metagenomics
description: Functional ontology assignments via HMM searching for environmental shotgun omics data
tags: [cerberus-x, hmm, functional-annotation, metagenomics, ontology]
author: oxo-call-community
source_url: "https://github.com/raw-lab/cerberus/blob/v1.5.0/README.md"
---

## Concepts

- **Tool Overview**: cerberus-x performs functional ontology assignments using Hidden Markov Model (HMM) searching for environmental shotgun omics data.
- **Core Function**: Assigns functional annotations to sequences using HMM-based searches against functional databases.
- **Algorithm**: Uses HMM profiles to identify functional domains and assign ontology terms.
- **Input**: FASTA sequence files from metagenomic or metatranscriptomic data.
- **Output**: Functional annotation results with ontology terms and confidence scores.
- **Application**: Functional analysis of environmental metagenomics data.
- **Installation**: Install via bioconda: `conda install -c bioconda cerberus-x`

## Pitfalls

- **Database Requirement**: Requires pre-built HMM databases for annotation.
- **Computational Time**: HMM searches can be computationally intensive.
- **Memory Usage**: Large databases may require significant memory.
- **Annotation Quality**: Depends on database completeness and quality.

## Examples

### Run functional annotation
**Args:** `cerberus-x -i sequences.fasta -o annotations.tsv`
**Explanation:** Performs functional annotation using default HMM databases.

### Specify custom database
**Args:** `cerberus-x -i sequences.fasta -d custom_hmm_db -o results.tsv`
**Explanation:** Uses custom HMM database for annotation.

### Parallel processing
**Args:** `cerberus-x -i sequences.fasta -o annotations.tsv -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### Display help
**Args:** `cerberus-x --help`
**Explanation:** Shows all available options and usage information.