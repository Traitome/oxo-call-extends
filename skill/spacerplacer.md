---
name: spacerplacer
category: genome-editing
description: SpacerPlacer is a powerful software for reconstructing ancestral CRISPR spacer arrays.
tags: [spacerplacer, genome-editing]
author: oxo-call-community
source_url: "https://github.com/fbaumdicker/SpacerPlacer"
---

## Concepts

- **Tool Overview**: spacerplacer (v1.0.1) - SpacerPlacer is a powerful software for reconstructing ancestral CRISPR spacer arrays.
- **Core Function**: SpacerPlacer is a powerful software for reconstructing ancestral CRISPR spacer arrays.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spacerplacer`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spacerplacer -i <input.fasta> -g <guide.fa> -o <output_dir>`
**Explanation:** Run spacerplacer with typical input and output options.
