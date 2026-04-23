---
name: rscape
category: alignment
description: R-scape (RNA Structural Covariation Above Phylogenetic Expectation) looks for evidence of a conserved RNA secondary structure by measuring pairwise covariations observed in an input multiple sequence alignment.
tags: ["rscape", "alignment"]
author: oxo-call-community
source_url: "http://eddylab.org/R-scape/"
---

## Concepts

- **Tool Overview**: R-scape (RNA Structural Covariation Above Phylogenetic Expectation) looks for evidence of a conserved RNA secondary structure by measuring pairwise covariations observed in an input multiple sequence alignment. (version 2.0.4.a)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rscape`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

