---
name: complexcgr
category: qc
description: Chaos Game Representation encoders for DNA/RNA sequences
tags: [complexcgr, cgr, sequence-visualization, dna-rna, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/AlgoLab/complexCGR"
---

## Concepts

- **Tool Overview**: complexCGR is a tool for generating Chaos Game Representation (CGR) encoders and image representations of DNA/RNA sequences, providing visual patterns for sequence analysis.
- **Core Function**: Converts nucleotide sequences into 2D fractal-like visual representations using iterative mapping algorithms.
- **Algorithm**: Uses Chaos Game Representation algorithm to map sequences into square or multi-dimensional spaces based on nucleotide composition.
- **Input**: DNA or RNA sequences in FASTA format.
- **Output**: CGR images, coordinate files, and numerical encodings for machine learning applications.
- **Application**: Sequence visualization, pattern recognition, and sequence-based machine learning features.
- **Installation**: Install via bioconda: `conda install -c bioconda complexcgr`

## Pitfalls

- **Sequence Length**: Very long sequences may produce dense images with limited detail.
- **Resolution**: Image resolution affects pattern visibility and computational requirements.
- **Normalization**: Different sequence lengths may require normalization for comparison.
- **Interpretation**: CGR patterns require training to interpret biologically.
- **Memory**: High-resolution CGRs for large sequences require significant memory.

## Examples

### Generate CGR image
**Args:** `complexcgr -i sequence.fasta -o cgr_image.png`
**Explanation:** Generates Chaos Game Representation image from DNA sequence.

### With custom resolution
**Args:** `complexcgr -i sequence.fasta -r 1024 -o cgr_image.png`
**Explanation:** Creates 1024x1024 resolution CGR image.

### Generate numerical encoding
**Args:** `complexcgr -i sequence.fasta -e -o encoding.txt`
**Explanation:** Outputs numerical CGR coordinates for machine learning.

### Display help
**Args:** `complexcgr --help`
**Explanation:** Shows all available options and usage information.