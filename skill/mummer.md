---
name: mummer
category: alignment
description: MUMmer is a system for rapidly aligning entire genomes
tags: [mummer, alignment]
author: oxo-call-community
source_url: "http://mummer.sourceforge.net/"
---

## Concepts

- **Tool Overview**: mummer v3.23 - MUMmer is a system for rapidly aligning entire genomes.
- **Core Function**: MUMmer is a system for rapidly aligning entire genomes
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mummer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Align genomes
**Args:** `nucmer --prefix=output reference.fasta query.fasta`
**Explanation:** Aligns query to reference genome.

