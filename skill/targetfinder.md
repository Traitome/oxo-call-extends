---
name: targetfinder
category: annotation
description: Plant small RNA target prediction tool
tags: [targetfinder, annotation]
author: oxo-call-community
source_url: "https://github.com/carringtonlab/TargetFinder"
---

## Concepts

- **Tool Overview**: targetfinder (v1.7) - Plant small RNA target prediction tool
- **Core Function**: Plant small RNA target prediction tool
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda targetfinder`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `targetfinder -i <input.fasta> -o <output.gff>`
**Explanation:** Run targetfinder with typical input and output options.
