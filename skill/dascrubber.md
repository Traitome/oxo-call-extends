---
name: dascrubber
category: alignment
description: Alignment-based Scrubbing pipeline
tags: [dascrubber, alignment]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/DASCRUBBER"
---

## Concepts

- **Tool Overview**: dascrubber (v0.0.1a2) - Alignment-based Scrubbing pipeline
- **Core Function**: Alignment-based Scrubbing pipeline
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda dascrubber`

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
