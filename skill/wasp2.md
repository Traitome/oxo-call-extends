---
name: wasp2
category: alignment
description: Allele-specific analysis of next-generation sequencing data with Rust acceleration
tags: [wasp2, alignment, bam]
author: oxo-call-community
source_url: "https://mcvickerlab.github.io/WASP2/"
---

## Concepts

- **Tool Overview**: wasp2 (v1.4.0) - WASP2 is a high-performance tool for allele-specific analysis of NGS data. It provides functionality for variant counting, read remapping for bias correction, and statistical analysis of allelic imbalance. The package includes a Rust extension for accelerated BAM processing.
- **Core Function**: Allele-specific analysis of next-generation sequencing data with Rust acceleration
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda wasp2`

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
