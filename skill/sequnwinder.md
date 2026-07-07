---
name: sequnwinder
category: annotation
description: sequnwinder - Characterize class-discriminative motifs in genomic loci
tags: ["sequnwinder", "annotation", "motif", "genomics"]
author: oxo-call-community
source_url: "http://mahonylab.org/software/sequnwinder/"
---

## Concepts

- **Tool Overview**: sequnwinder (v0.1.4) characterizes class-discriminative motifs in genomic loci.
- **Core Function**: Identifies motifs associated with specific annotation labels.
- **Algorithm**: Uses statistical methods for motif discovery and classification.
- **Input/Output**: Accepts genomic loci and produces motif annotations.
- **Motif Discovery**: Focuses on discriminative motif analysis.
- **Applications**: Regulatory genomics, transcription factor binding, and epigenomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on input data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Run analysis
**Args:** `sequnwinder -i peaks.bed -a annotations.txt -o results/`
**Explanation:** `-i` input peaks; `-a` annotations; `-o` output.

### With motifs
**Args:** `sequnwinder -i peaks.bed -a annotations.txt -m motifs.txt -o results/`
**Explanation:** `-m` known motifs file.

### Verbose logging
**Args:** `sequnwinder -v -i peaks.bed -a annotations.txt -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sequnwinder --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sequnwinder --version`
**Explanation:** Shows current version.

### From FASTA
**Args:** `sequnwinder -f sequences.fasta -a annotations.txt -o results/`
**Explanation:** `-f` input FASTA file.