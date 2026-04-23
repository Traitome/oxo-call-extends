---
name: ymp
category: containerization
description: Create entire NGS pipelines with one command
tags: [ymp, containerization]
author: oxo-call-community
source_url: "https://ymp.readthedocs.io"
---

## Concepts

- **Tool Overview**: ymp (v0.3.2) - YMP allows composing complex NGS data analysis workflows from conceptual building blocks ("stages") using a single command line statement. Pre-tested conda environments are installed on-the fly, reference databases downloaded as needed and requested workflows executed using Snakemake.  With YMP, developing new pipelines or testing alternative approaches using differnt tools or optimizing parameters becomes easy. Results from previous results are reused where possible. The collection of stages included with YMP is can be extended with project specific YMP stage definitions or simple Snakefiles.
- **Core Function**: Create entire NGS pipelines with one command
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ymp`

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
