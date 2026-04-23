---
name: chisel
category: qc
description: Copy-number Haplotype Inference in Single-cell by Evolutionary Links
tags: [chisel, qc]
author: oxo-call-community
source_url: "https://github.com/raphael-group/chisel"
---

## Concepts

- **Tool Overview**: chisel (v1.1.4) - Copy-number Haplotype Inference in Single-cell by Evolutionary Links
- **Core Function**: CHISEL is an algorithm to infer allele- and haplotype-specififc copy numbers in individual cells from low-coverage single-cell DNA sequencing data. Specifically, the current implementation of CHISEL h...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda chisel`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
