---
name: bamaligncleaner
category: alignment
description: Removes unaligned references in BAM alignment file.
tags: [bamaligncleaner, alignment, BAM]
author: oxo-call-community
source_url: "https://github.com/maxibor/bamAlignCleaner"
---

## Concepts

- **Tool Overview**: bamaligncleaner (v0.3) - Removes unaligned references in BAM alignment file.
- **Core Function**: Removes unaligned references in BAM alignment file.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda bamaligncleaner`

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
