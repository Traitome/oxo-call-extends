---
name: cloudspades
category: assembly
description: A module of the SPAdes assembler aimed at genome assembly from linked read technologies (10x, Tellseq, Haplotagging).
tags: [cloudspades, assembly]
author: oxo-call-community
source_url: "https://github.com/ablab/spades/tree/cloudspades-ismb"
---

## Concepts

- **Tool Overview**: cloudspades (v3.16.0) - A module of the SPAdes assembler aimed at genome assembly from linked read technologies (10x, Tellseq, Haplotagging).
- **Core Function**: A module of the SPAdes assembler aimed at genome assembly from linked read technologies (10x, Tellseq, Haplotagging).
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cloudspades`

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
