---
name: ffgc
category: annotation
description: Family Free Genome Comparison (FFGC) workflow
tags: [ffgc, annotation]
author: oxo-call-community
source_url: "https://gitlab.ub.uni-bielefeld.de/gi/FFGC"
---

## Concepts
- **Tool Overview**: Family Free Genome Comparison (FFGC) is a self-contained workflow system that provides functionality for all steps of a family-free gene order analysis starting from annotated genome sequences.  Family-free methods for gene order analyses do not require prior knowledge of evolutionary relationships between the genes across the studied genomes. This tool features a complete workflow for genome comparison, requiring nothing but annotated genome sequences as input.  Surprisingly, the continuous development of family-free methods recently lead to an integrated method for inferring gene families across several species. FFGC now includes a subworkflow for inferring gene families simultaneously based on gene similarities and family-free genome rearrangements (OrthoFFGCʜ and OrthoFFGCʜ≈ extensions).  FFGC is available for download at our git repository (https://gitlab.ub.uni-bielefeld.de/gi/FFGC) or as a Conda package at Bioconda (https://anaconda.org/bioconda/ffgc).  In general, three major steps are performed: (1) the computation of local sequence alignment scores between genes of two or more gene order sequences using BLAST+ or Diamond; (2) the establishment of gene relationships; and (3) the actual family-free gene order analysis.
- **Core Function**: Family Free Genome Comparison (FFGC) workflow
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda ffgc`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
