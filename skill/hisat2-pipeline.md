---
name: hisat2-pipeline
category: alignment
description: A pipeline to automatically run an RNA-seq analysis using HISAT2/Stringtie using default settings.
tags: [hisat2-pipeline, alignment]
author: oxo-call-community
source_url: "https://github.com/mcamagna/HISAT2-pipeline"
---

## Concepts

- **Tool Overview**: hisat2-pipeline (v1.1.1) - A pipeline to automatically run an RNA-seq analysis using HISAT2/Stringtie using default settings.
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hisat2-pipeline`

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
