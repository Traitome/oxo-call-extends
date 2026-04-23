---
name: dart
category: alignment
description: Dart: a fast and accurate RNA-seq mapper
tags: [dart, alignment]
author: oxo-call-community
source_url: "https://github.com/hsinnan75/Dart"
---

## Concepts

- **Tool Overview**: dart (v1.4.6) - Dart: a fast and accurate RNA-seq mapper
- **Core Function**: An efficient short read mapper for RNA-Seq data.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda dart`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
