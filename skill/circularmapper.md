---
name: circularmapper
category: alignment
description: A method to improve mappings on circular genomes, using the BWA mapper.
tags: [circularmapper, alignment]
author: oxo-call-community
source_url: "https://github.com/apeltzer/CircularMapper"
---

## Concepts

- **Tool Overview**: circularmapper (v1.93.5) - A method to improve mappings on circular genomes, using the BWA mapper.
- **Core Function**: A method to improve mappings on circular genomes, using the BWA mapper.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda circularmapper`

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
