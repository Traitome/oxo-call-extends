---
name: metawepp
category: alignment
description: metaWEPP: Improving resolution of metagenomic analysis using WEPP
tags: [metawepp, alignment, alignment]
author: oxo-call-community
source_url: "https://github.com/TurakhiaLab/metaWEPP"
---

## Concepts

- **Tool Overview**: metawepp v0.1.0 - metaWEPP extends the current species-level resolution of existing metagenomic tools by providing near-haplotype detection and abundance estimation for multi-species samples. It utilizes a standard classifier to first segregate reads by species before applying the Wastewater-Based Epidemiology using Phylogenetic Placements (WEPP) pipeline to each segregated dataset. By performing parsimonious read placement on species-specific mutation-annotated trees (MATs), metaWEPP identifies the haplotypes that best explain the data and flags Unaccounted Alleles—mutations observed in the sample but unexplained by selected haplotypes—potentially indicating the presence of novel variants. The pipeline enables high-resolution surveillance across diverse pathogens and includes an interactive dashboard for visualizing identified haplotypes within their global phylogenies. This allows for detailed, read-level analysis of emerging lineages within complex metagenomic datasets..
- **Core Function**: metaWEPP: Improving resolution of metagenomic analysis using WEPP
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda metawepp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
