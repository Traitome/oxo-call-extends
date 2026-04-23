---
name: shapemapper
category: formatting
description: ShapeMapper converts raw sequencing files into mutational profiles, creates SHAPE reactivity plots, and provides extensive diagnostic information useful for experiment analysis and troubleshooting.
tags: [shapemapper, formatting]
author: oxo-call-community
source_url: "http://www.chem.unc.edu/rna/software.html"
---

## Concepts

- **Tool Overview**: shapemapper (v1.2) - ShapeMapper converts raw sequencing files into mutational profiles, creates SHAPE reactivity plots, and provides extensive diagnostic information useful for experiment analysis and troubleshooting.
- **Core Function**: ShapeMapper converts raw sequencing files into mutational profiles, creates SHAPE reactivity plots, and provides extensive diagnostic information useful for experiment analysis and troubleshooting.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shapemapper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shapemapper -i <input_file> -o <output_file>`
**Explanation:** Run shapemapper with typical input and output options.
