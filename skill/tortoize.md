---
name: tortoize
category: analysis
description: Tortoize - Tool for analyzing tandem repeats and their expansions.
tags: [tortoize, tandem-repeat, repeat-expansion, genomics, microsatellite]
author: oxo-call-community
source_url: "https://github.com/compbio/tortoize"
---

## Concepts

- **Tool Overview**: Tortoize - A tool for detecting and analyzing tandem repeat expansions in genomic sequences.
- **Core Function**: Identifies tandem repeats and characterizes their expansion status.
- **Input**: Genomic sequences (FASTA), repeat annotation files.
- **Output**: Repeat expansions, size estimates, quality metrics.
- **Installation**: `pip install tortoize` or `conda install -c bioconda tortoize`
- **Use Case**: Repeat expansion analysis, disease-associated repeats, population genetics.

## Pitfalls

- **Complex Repeats**: Complex repeat structures may be difficult to resolve.
- **Sequence Quality**: Low-quality sequences affect repeat detection.

## Examples

### Detect repeats
**Args:** `tortoize -i genome.fasta -o repeats/`
**Explanation:** Detect and analyze tandem repeats in genome.

### Expansion analysis
**Args:** `tortoize expand -i repeats.txt -o expansions/`
**Explanation:** Analyze repeat expansions and estimate sizes.
