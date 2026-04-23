---
name: t_coffee
category: alignment
description: A collection of tools for Computing, Evaluating and Manipulating Multiple Alignments of DNA, RNA, Protein Sequences and Structures.
tags: [t_coffee, alignment]
author: oxo-call-community
source_url: "http://www.tcoffee.org/Projects/tcoffee/"
---

## Concepts

- **Tool Overview**: t_coffee (v11.0.8) - A collection of tools for Computing, Evaluating and Manipulating Multiple Alignments of DNA, RNA, Protein Sequences and Structures.
- **Core Function**: A collection of tools for Computing, Evaluating and Manipulating Multiple Alignments of DNA, RNA, Protein Sequences and Structures.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda t_coffee`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `t_coffee -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run t_coffee with typical input and output options.
