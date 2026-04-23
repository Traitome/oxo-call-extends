---
name: viennarna
category: containerization
description: ViennaRNA package -- RNA secondary structure prediction and comparison
tags: [viennarna, containerization]
author: oxo-call-community
source_url: "http://www.tbi.univie.ac.at/RNA/"
---

## Concepts

- **Tool Overview**: viennarna (v2.7.2) - ViennaRNA package -- RNA secondary structure prediction and comparison
- **Core Function**: ViennaRNA package -- RNA secondary structure prediction and comparison
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda viennarna`

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
