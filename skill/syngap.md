---
name: syngap
category: annotation
description: SynGAP: Synteny-based Gene structure Annotation Polisher
tags: [syngap, annotation]
author: oxo-call-community
source_url: "https://github.com/yanyew/SynGAP"
---

## Concepts

- **Tool Overview**: syngap (v1.2.5) - SynGAP: Synteny-based Gene structure Annotation Polisher
- **Core Function**: SynGAP: Synteny-based Gene structure Annotation Polisher
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda syngap`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `syngap -i <input.fasta> -o <output.gff>`
**Explanation:** Run syngap with typical input and output options.
