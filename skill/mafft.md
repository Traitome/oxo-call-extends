---
name: mafft
category: alignment
description: Multiple alignment program for amino acid or nucleotide sequences based on fast Fourier transform
tags: [mafft, alignment]
author: oxo-call-community
source_url: "http://mafft.cbrc.jp/alignment/software/"
---

## Concepts

- **Tool Overview**: mafft v7.525 - Multiple alignment program for amino acid or nucleotide sequences based on fast Fourier transform.
- **Core Function**: Multiple alignment program for amino acid or nucleotide sequences based on fast Fourier transform
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mafft`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Multiple alignment
**Args:** `--auto input.fasta > aligned.fasta`
**Explanation:** Performs multiple sequence alignment with automatic strategy selection.

