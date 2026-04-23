---
name: cawlign
category: alignment
description: A tool for aligning consensus sequences to reference genomes.
tags: [cawlign, alignment, FASTA]
author: oxo-call-community
source_url: "https://github.com/veg/cawlign"
---

## Concepts

- **Tool Overview**: cawlign (v0.1.16) - A tool for aligning consensus sequences to reference genomes.
- **Core Function**: A standalone C++ port of bealign, a part of the BioExt package. The purpose of this program is to align/map sequences in a FASTA file to a reference sequence and output the alignment as another FASTA ...
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda cawlign`

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
