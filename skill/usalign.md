---
name: usalign
category: alignment
description: Universal structure alignment of monomeric, complex proteins and nucleic acids
tags: [usalign, alignment]
author: oxo-call-community
source_url: "https://zhanggroup.org/US-align/help"
---

## Concepts

- **Tool Overview**: usalign (v20241201) - US-align (Universal Structural alignment) is a unified protocol to compare 3D structures of different macromolecules (proteins, RNAs and DNAs) in different forms (monomers, oligomers and heterocomplexes) for both pairwise and multiple structure alignments. The core alogrithm of US-align is extended from TM-align and generates optimal structural alignments by maximizing TM-score of compared strucures through heuristic dynamic programming iterations. Large-scale benchmark tests showed that US-align can generate more accurate structural alignments with significantly reduced CPU time, compared to the state-of-the-art methods developed for specific structural alignment tasks. TM-score has values in (0,1] with 1 indicating an identical structure match, where a TM-score ≥0.5 (or 0.45) means the structures share the same global topology for proteins (or RNAs).
- **Core Function**: Universal structure alignment of monomeric, complex proteins and nucleic acids
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda usalign`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
