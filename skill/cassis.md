---
name: cassis
category: formatting
description: Detection of genomic rearrangement breakpoints
tags: [cassis, formatting, BED]
author: oxo-call-community
source_url: "http://pbil.univ-lyon1.fr/software/Cassis/"
---

## Concepts

- **Tool Overview**: cassis (v0.0.20120106) - Detection of genomic rearrangement breakpoints
- **Core Function**: The package Cassis implements methods for precise detection of genomic rearrangement breakpoints, which were described in Lemaitre et al., 2008.
- **Input/Output**: BED interval input/output
- **Installation**: `conda install -c bioconda cassis`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.gff -o output.gtf`
**Explanation:** Convert between file formats
