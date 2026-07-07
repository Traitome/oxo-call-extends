---
name: crispr_studio
category: genome-editing
description: CRISPRStudio visualizes CRISPR arrays by clustering spacer sequences and generating publication-ready vector graphics for microbial strain comparison
tags: [crispr_studio, CRISPR, array-visualization, spacer, microbial-typing, phylogeny]
author: oxo-call-community
source_url: "https://github.com/moineaulab/CRISPRStudio"
---

## Concepts

- **Tool Overview**: CRISPRStudio (v1.0) is a command-line tool for rapid visualization of CRISPR arrays in microbial genomes.
- **Core Function**: Compares spacer sequences across a dataset, clusters similar spacers based on sequence homology, assigns two-color codes to each cluster, and generates scalable SVG output for publication-quality figures.
- **Algorithm**: (1) Extract spacer sequences from CRISPRDetect GFF output. (2) Align spacers using FASTA36 and compute pairwise similarity. (3) Cluster spacers by mismatch cutoff (default=2). (4) Assign color codes to clusters. (5) Generate SVG visualization of arrays.
- **Input/Output**: Requires CRISPRDetect GFF format input; outputs SVG vector graphics
- **Installation**: `git clone https://github.com/moineaulab/CRISPRStudio.git && cd CRISPRStudio && ./Install.sh`
- **Dependencies**: Python 3.6.x or older, FASTA36, scipy, numpy, pandas, scikit-bio

## Pitfalls

- **Python Version**: scikit-bio has compatibility issues with Python 3.7+. Install on Python 3.6.x for best results.
- **CRISPRDetect Dependency**: CRISPRStudio requires CRISPRDetect to first predict CRISPR arrays in genomes. CRISPRDetect output (GFF format) is the input to CRISPRStudio.
- **Spacer Clustering**: The mismatch cutoff (-m flag) determines color assignment. Default is 2 mismatches allowed for same-color spacers. Set to 0 for identical-only matching.

## Examples

### Basic CRISPR array visualization
**Args:** `-g crisdetect_output.gff -f genome.fasta -o output.svg`
**Explanation:** Standard workflow: provide CRISPRDetect GFF file and genome FASTA to generate array visualization.

### Automatic sorting of CRISPR loci
**Args:** `-g crisdetect_output.gff -f genome.fasta -s -o output.svg`
**Explanation:** The `-s` flag enables automatic sorting of CRISPR loci for easier comparison across strains.

### Highlight shared spacers across strains
**Args:** `-g crisdetect_output.gff -f genome.fasta -c -o output.svg`
**Explanation:** Use `-c` flag to highlight spacers that are shared between multiple strains in the dataset with distinct colors.

### Custom mismatch cutoff for spacer clustering
**Args:** `-g crisdetect_output.gff -f genome.fasta -m 3 -o output.svg`
**Explanation:** Set `-m` to control spacer clustering stringency. Higher values (e.g., 3) group more divergent spacers as similar.

### Gray out unique spacers
**Args:** `-g crisdetect_output.gff -f genome.fasta -gU -o output.svg`
**Explanation:** Use `-gU` to gray out spacers appearing only once, leaving only spacers shared at least twice colored.
