---
name: glean-gene
category: alignment
description: GLEAN is an unsupervised learning system to integrate disparate sources of gene structure evidence (gene model predictions, EST/protein genomic sequence alignments, SAGE/peptide tags, etc) to produce a consensus gene prediction, without prior training.
tags: [glean-gene, alignment]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/glean-gene/"
---

## Concepts

- **Tool Overview**: glean-gene (v1.0.1) - GLEAN is an unsupervised learning system to integrate disparate sources of gene structure evidence (gene model predictions, EST/protein genomic sequence alignments, SAGE/peptide tags, etc) to produce a consensus gene prediction, without prior training.
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda glean-gene`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
