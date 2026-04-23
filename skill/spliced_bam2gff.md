---
name: spliced_bam2gff
category: alignment
description: A tool to convert spliced BAM alignments into GFF2 format
tags: [spliced_bam2gff, alignment, bam, gff]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/spliced_bam2gff"
---

## Concepts

- **Tool Overview**: spliced_bam2gff (v1.3) - A tool to convert spliced BAM alignments into GFF2 format
- **Core Function**: A tool to convert spliced BAM alignments into GFF2 format
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spliced_bam2gff`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spliced_bam2gff -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run spliced_bam2gff with typical input and output options.
