---
name: assembly-stats
category: assembly
description: Get assembly statistics from FASTA and FASTQ files
tags: [assembly-stats, assembly, FASTA, FASTQ]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/assembly-stats"
---

## Concepts

- **Tool Overview**: assembly-stats (v1.0.1) - Get assembly statistics from FASTA and FASTQ files
- **Core Function**: Get assembly statistics from FASTA and FASTQ files
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda assembly-stats`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
