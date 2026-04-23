---
name: tncomp_finder
category: utility
description: Composite transposon finder for bacterial and archaeal genomes
tags: [tncomp_finder, utility]
author: oxo-call-community
source_url: "https://github.com/danillo-alvarenga/tncomp_finder"
---

## Concepts

- **Tool Overview**: tncomp_finder (v1.0.0) - TnComp_finder is a program for the prediction of putative composite transposons in bacterial and archaeal genomes based on insertion sequence replicas in a relatively short span. It works by comparing nucleotide sequences from bacterial and archaeal genomes to a custom transposon database.
- **Core Function**: Composite transposon finder for bacterial and archaeal genomes
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda tncomp_finder`

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
