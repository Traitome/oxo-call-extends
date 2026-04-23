---
name: strucvis
category: annotation
description: strucVis : Display small RNA depth of coverage on a predicted RNA secondary structure
tags: [strucvis, annotation]
author: oxo-call-community
source_url: "https://github.com/MikeAxtell/strucVis"
---

## Concepts

- **Tool Overview**: strucvis (v0.9) - strucVis : Display small RNA depth of coverage on a predicted RNA secondary structure
- **Core Function**: strucVis : Display small RNA depth of coverage on a predicted RNA secondary structure
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strucvis`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strucvis -i <input.fasta> -o <output.gff>`
**Explanation:** Run strucvis with typical input and output options.
