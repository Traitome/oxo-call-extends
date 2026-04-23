---
name: tirank
category: expression
description: A comprehensive analysis tool for prioritizing phenotypic niches in tumor microenvironment.
tags: [tirank, expression]
author: oxo-call-community
source_url: "https://tirank.readthedocs.io/"
---

## Concepts

- **Tool Overview**: tirank (v1.0.2) - TiRank integrates deep learning and statistical analysis to infer phenotype transfer from bulk transcriptomic data to single-cell or spatial transcriptomic data. GPU-accelerated modules rely on PyTorch (>=2.1) and torchvision (>=0.16), which should be installed manually according to the user's CUDA environment.
- **Core Function**: A comprehensive analysis tool for prioritizing phenotypic niches in tumor microenvironment.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda tirank`

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
