---
name: shorttracks
category: alignment
description: ShortTracks : Useful length- and strand-based coverage files (bigwig) from small RNA-seq alignments (BAM)
tags: [shorttracks, alignment, bam]
author: oxo-call-community
source_url: "https://github.com/MikeAxtell/ShortTracks"
---

## Concepts

- **Tool Overview**: shorttracks (v1.3) - ShortTracks : Useful length- and strand-based coverage files (bigwig) from small RNA-seq alignments (BAM)
- **Core Function**: ShortTracks : Useful length- and strand-based coverage files (bigwig) from small RNA-seq alignments (BAM)
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shorttracks`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shorttracks -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run shorttracks with typical input and output options.
