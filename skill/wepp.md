---
name: wepp
category: alignment
description: Wastewater-Based Epidemiology using Phylogenetic Placements
tags: [wepp, alignment]
author: oxo-call-community
source_url: "https://turakhia.ucsd.edu/WEPP"
---

## Concepts

- **Tool Overview**: wepp (v0.1.5.4) - WEPP (Wastewater-Based Epidemiology using Phylogenetic Placements) is a pathogen-agnostic pipeline that enhances wastewater surveillance by leveraging the pathogen's full phylogeny. It reports haplotype and lineage abundances, maps reads parsimoniously to selected haplotypes, and flags Unaccounted Alleles — those observed in the sample but unexplained by selected haplotypes, potentially indicating novel variants. WEPP performs parsimonious read placement on the mutation-annotated tree (MAT) to select a subset of haplotypes and adds their neighbors to form an initial candidate pool, which is passed to a deconvolution algorithm to estimate their relative abundances. An interactive dashboard enables visualization of haplotypes in the global phylogenetic tree and read-level analysis.
- **Core Function**: Wastewater-Based Epidemiology using Phylogenetic Placements
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda wepp`

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
