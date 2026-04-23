---
name: sequnwinder
category: annotation
description: SeqUnwinder is a framework for characterizing class-discriminative motifs in a collection of genomic loci that have several (overlapping) annotation labels.
tags: [sequnwinder, annotation]
author: oxo-call-community
source_url: "http://mahonylab.org/software/sequnwinder/"
---

## Concepts

- **Tool Overview**: sequnwinder (v0.1.4) - SeqUnwinder is a framework for characterizing class-discriminative motifs in a collection of genomic loci that have several (overlapping) annotation labels.
- **Core Function**: SeqUnwinder is a framework for characterizing class-discriminative motifs in a collection of genomic loci that have several (overlapping) annotation labels.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sequnwinder`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sequnwinder -i <input.fasta> -o <output.gff>`
**Explanation:** Run sequnwinder with typical input and output options.
