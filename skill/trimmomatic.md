---
name: trimmomatic
category: qc
description: A flexible read trimming tool for Illumina NGS data.
tags: [trimmomatic, qc]
author: oxo-call-community
source_url: "https://www.plabipd.de/trimmomatic_main.html"
---

## Concepts

- **Tool Overview**: trimmomatic (v0.40) - A flexible read trimming tool for Illumina NGS data.
- **Core Function**: A flexible read trimming tool for Illumina NGS data.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda trimmomatic`

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
