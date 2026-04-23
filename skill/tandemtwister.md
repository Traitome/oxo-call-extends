---
name: tandemtwister
category: annotation
description: Detection of interleaved and embedded tandem repeats from long reads
tags: [tandemtwister, annotation, bed]
author: oxo-call-community
source_url: "https://github.com/Lionward/tandemtwister"
---

## Concepts

- **Tool Overview**: tandemtwister (v0.2.0) - Detection of interleaved and embedded tandem repeats from long reads
- **Core Function**: Detection of interleaved and embedded tandem repeats from long reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tandemtwister`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tandemtwister -i <input.fasta> -o <output.gff>`
**Explanation:** Run tandemtwister with typical input and output options.
