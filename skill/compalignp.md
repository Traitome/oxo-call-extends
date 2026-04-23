---
name: compalignp
category: alignment
description: Compute fractional "identity" between trusted alignment and test alignment.
tags: [compalignp, alignment]
author: oxo-call-community
source_url: "http://www.biophys.uni-duesseldorf.de/bralibase/"
---

## Concepts

- **Tool Overview**: compalignp (v1.0) - Compute fractional "identity" between trusted alignment and test alignment.
- **Core Function**: Compute fractional "identity" between trusted alignment and test alignment.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda compalignp`

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
