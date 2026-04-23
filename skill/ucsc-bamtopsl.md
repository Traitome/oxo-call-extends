---
name: ucsc-bamtopsl
category: formatting
description: Convert a bam file to a psl and optionally also a fasta file that contains the reads.
tags: [ucsc-bamtopsl, formatting, bam]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-bamtopsl (v482) - Convert a bam file to a psl and optionally also a fasta file that contains the reads.
- **Core Function**: Convert a bam file to a psl and optionally also a fasta file that contains the reads.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-bamtopsl`

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
