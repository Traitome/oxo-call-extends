---
name: mummer4
category: alignment
description: MUMmer is a system for rapidly aligning entire genomes.
tags: [mummer4, alignment]
author: oxo-call-community
source_url: "https://mummer4.github.io"
---

## Concepts

- **Tool Overview**: mummer4 v4.0.1 - MUMmer is a system for rapidly aligning entire genomes..
- **Core Function**: MUMmer is a system for rapidly aligning entire genomes.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mummer4`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Align genomes
**Args:** `nucmer --prefix=output reference.fasta query.fasta`
**Explanation:** Aligns query sequences to reference using nucmer.

### Show alignments
**Args:** `mummer -mum reference.fasta query.fasta`
**Explanation:** Finds maximal unique matches between sequences.

