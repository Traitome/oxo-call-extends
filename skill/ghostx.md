---
name: ghostx
category: formatting
description: GHOSTX is a homology search tool which can detect remote homologues like BLAST and is about 100 times more efficient than BLAST by using suffix arrays. GHOSTX outputs search results in the format similar to BLAST-tabular format.
tags: [ghostx, formatting]
author: oxo-call-community
source_url: "http://www.bi.cs.titech.ac.jp/ghostx/"
---

## Concepts

- **Tool Overview**: ghostx (v1.3.7) - GHOSTX is a homology search tool which can detect remote homologues like BLAST and is about 100 times more efficient than BLAST by using suffix arrays. GHOSTX outputs search results in the format similar to BLAST-tabular format.
- **Core Function**: Provides functionality for formatting tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda ghostx`

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
