---
name: csblast
category: alignment
description: Context-specific extension of BLAST that significantly improves sensitivity and alignment quality.
tags: [csblast, alignment]
author: oxo-call-community
source_url: "http://wwwuser.gwdg.de/~compbiol/data/csblast/"
---

## Concepts

- **Tool Overview**: csblast (v2.2.3) - Context-specific extension of BLAST that significantly improves sensitivity and alignment quality.
- **Core Function**: Context-specific extension of BLAST that significantly improves sensitivity and alignment quality.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda csblast`

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
