---
name: cnasim
category: formatting
description: Improved simulation of single-cell copy number profiles and DNA-seq data from tumors
tags: [cnasim, formatting, SAM]
author: oxo-call-community
source_url: "https://github.com/samsonweiner/CNAsim"
---

## Concepts

- **Tool Overview**: cnasim (v1.3.5) - Improved simulation of single-cell copy number profiles and DNA-seq data from tumors
- **Core Function**: CNAsim is a software package for improved simulation of single-cell copy number alteration (CNA) data from tumors. See our paper with the same name published in Bioinformatics.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda cnasim`

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
