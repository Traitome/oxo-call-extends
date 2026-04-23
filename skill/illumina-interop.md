---
name: illumina-interop
category: qc
description: The Illumina InterOp libraries are a set of common routines used for reading and writing InterOp metric files. These metric files are binary files produced during a run providing detailed statistics about a run. In a few cases, the metric files are produced after a run during secondary analysis (index metrics) or for faster display of a subset of the original data (collapsed quality scores).
tags: [illumina-interop, qc]
author: oxo-call-community
source_url: "http://illumina.github.io/interop/index.html"
---

## Concepts

- **Tool Overview**: illumina-interop (v1.9.0) - The Illumina InterOp libraries are a set of common routines used for reading and writing InterOp metric files. These metric files are binary files produced during a run providing detailed statistics about a run. In a few cases, the metric files are produced after a run during secondary analysis (index metrics) or for faster display of a subset of the original data (collapsed quality scores).
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda illumina-interop`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
