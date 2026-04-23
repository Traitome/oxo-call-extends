---
name: whokaryote
category: assembly
description: Classify metagenomic contigs as eukaryotic or prokaryotic
tags: [whokaryote, assembly]
author: oxo-call-community
source_url: "https://github.com/LottePronk/whokaryote"
---

## Concepts

- **Tool Overview**: whokaryote (v1.1.2) - Whokaryote uses a random forest classifier that uses gene-structure based features and optionally Tiara predictions to predict whether a contig is from a eukaryote or from a prokaryote. You can use Whokaryote to determine which contigs need eukaryotic gene prediction and which need prokaryotic gene prediction.
- **Core Function**: Classify metagenomic contigs as eukaryotic or prokaryotic
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda whokaryote`

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
