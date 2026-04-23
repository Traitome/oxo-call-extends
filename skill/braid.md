---
name: braid
category: annotation
description: Block Resolution and Annotation of Integrated DNA
tags: [braid, annotation, dna, integration]
author: oxo-call-community
source_url: "https://github.com/YuefanHuang1998/BRAID"
---

## Concepts

- **Tool Overview**: BRAID performs block resolution and annotation of integrated DNA sequences.
- **Core Function**: Identifies and annotates integrated DNA blocks in genomes.
- **Input**: Genome sequences and integration evidence.
- **Output**: Annotated integration sites and block boundaries.
- **Application**: Analysis of horizontal gene transfer and DNA integration events.
- **Installation**: Install via bioconda: `conda install -c bioconda braid`

## Pitfalls

- **Evidence Required**: Requires evidence of integration events.
- **Reference Genome**: Well-annotated reference improves accuracy.
- **Python Required**: Requires Python runtime environment.

## Examples

### Detect integration blocks
**Args:** `braid -g genome.fa -i evidence.tsv -o integration_results/`
**Explanation:** Identifies and annotates integrated DNA blocks in genome.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
