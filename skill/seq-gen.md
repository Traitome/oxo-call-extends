---
name: seq-gen
category: population-genomics
description: Seq-Gen is a program that will simulate the evolution of nucleotide or amino acid sequences along a phylogeny, using common models of the substitution process.
tags: [seq-gen, population-genomics]
author: oxo-call-community
source_url: "http://tree.bio.ed.ac.uk/software/Seq-Gen/"
---

## Concepts

- **Tool Overview**: seq-gen (v1.3.5) - Seq-Gen is a program that will simulate the evolution of nucleotide or amino acid sequences along a phylogeny, using common models of the substitution process.
- **Core Function**: Seq-Gen is a program that will simulate the evolution of nucleotide or amino acid sequences along a phylogeny, using common models of the substitution process.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seq-gen`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seq-gen -i <input.vcf> -o <output_dir>`
**Explanation:** Run seq-gen with typical input and output options.
