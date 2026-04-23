---
name: trace-crispr
category: alignment
description: TRACE: Triple-aligner Read Analysis for CRISPR Editing
tags: [trace-crispr, alignment]
author: oxo-call-community
source_url: "https://trace-crispr.readthedocs.io"
---

## Concepts

- **Tool Overview**: trace-crispr (v0.6.3) - TRACE provides robust quantification of CRISPR editing outcomes including HDR, NHEJ, and large deletions using a triple-aligner consensus approach (BWA-MEM, BBMap, minimap2).
- **Core Function**: TRACE: Triple-aligner Read Analysis for CRISPR Editing
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda trace-crispr`

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
