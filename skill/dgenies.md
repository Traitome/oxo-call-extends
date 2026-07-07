---
name: dgenies
category: utility
description: D-Genies - Interactive dot plot visualization for genome comparisons.
tags: [dgenies, utility, dotplot, visualization, genome-comparison]
author: oxo-call-community
source_url: "http://dgenies.toulouse.inrae.fr"
---

## Concepts

- **Tool Overview**: dgenies (v1.5.0+) is an interactive tool for generating dot plots of large genome alignments. It provides visualization of synteny and structural variations.
- **Core Function**: Creates interactive dot plots for visualizing genome-to-genome alignments, highlighting syntenic regions and rearrangements.
- **Input/Output**: Input: Genome FASTA files or pre-computed alignment files (BLAST, MUMmer). Output: Interactive HTML dot plot visualization.
- **Algorithm**: Uses sequence alignment results to generate dot plots with configurable parameters for filtering and visualization.
- **Key Features**: Interactive visualization, supports large genomes, multiple alignment formats, synteny detection, structural variation highlighting.
- **Installation**: `conda install -c bioconda dgenies`

## Pitfalls

- **Input Requirements**: Requires genome sequences or pre-computed alignments.
- **Memory Usage**: May require significant memory for large genome comparisons.
- **Alignment Quality**: Dot plot quality depends on input alignment quality.
- **Visualization Complexity**: Very large genomes may produce cluttered dot plots.
- **Browser Requirements**: Interactive features require modern web browser.

## Examples

### Generate dot plot from genomes
**Args:** `dgenies --target genome1.fa --query genome2.fa --output dotplot/`
**Explanation:** Generates interactive dot plot comparing two genomes using MUMmer alignment.

### With pre-computed alignment
**Args:** `dgenies --target genome1.fa --query genome2.fa --output dotplot/ --nucmer nucmer.out`
**Explanation:** Use pre-computed MUMmer alignment for faster visualization.

### Protein-level comparison
**Args:** `dgenies --target proteins1.fa --query proteins2.fa --output dotplot/ --blast blast.out`
**Explanation:** Compare protein sequences using BLAST alignment.

### Filter by alignment length
**Args:** `dgenies --target genome1.fa --query genome2.fa --output dotplot/ --min-length 1000`
**Explanation:** Filter short alignments, only show matches >= 1000 bp.

### Generate static image
**Args:** `dgenies --target genome1.fa --query genome2.fa --output dotplot/ --png plot.png`
**Explanation:** Generate static PNG image in addition to interactive HTML.