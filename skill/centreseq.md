---
name: centreseq
category: assembly
description: Fast generation of core genome from bacterial strains
tags: [centreseq, assembly]
author: oxo-call-community
source_url: "https://github.com/bfssi-forest-dussault/centreseq"
---

## Concepts

- **Tool Overview**: centreseq (v0.3.8) - Fast generation of core genome from bacterial strains
- **Core Function**: Fast generation of core genome from bacterial strains
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda centreseq`

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
