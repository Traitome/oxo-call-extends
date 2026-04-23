---
name: clame
category: alignment
description: CLAME is a binning software for metagenomic reads. It immplements a fm-index search algorithm for nucleotide sequence alignment. Then it uses strongly connected component strategy to bin sequences with similar DNA composition.
tags: [clame, alignment]
author: oxo-call-community
source_url: "https://github.com/andvides/CLAME"
---

## Concepts

- **Tool Overview**: clame (v1.0) - CLAME is a binning software for metagenomic reads. It immplements a fm-index search algorithm for nucleotide sequence alignment. Then it uses strongly connected component strategy to bin sequences with similar DNA composition.
- **Core Function**: CLAME is a binning software for metagenomic reads. It immplements a fm-index search algorithm for nucleotide sequence alignment. Then it uses strongly connected component strategy to bin sequences with similar DNA composition.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda clame`

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
