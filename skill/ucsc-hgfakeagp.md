---
name: ucsc-hgfakeagp
category: utility
description: UCSC hgFakeAgp - Tool for creating fake AGP files.
tags: [ucsc-hgfakeagp, ucsc, agp, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgFakeAgp - A tool for creating fake AGP files.
- **Core Function**: Generates AGP files from sequence data.
- **Input**: Sequence information.
- **Output**: AGP file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome assembly, scaffolding, data preparation.

## Pitfalls

- **Sequence Names**: Requires matching sequence names.
- **Memory**: May require significant memory for large sequences.

## Examples

### Create fake AGP
**Args:** `hgFakeAgp chrom.sizes > assembly.agp`
**Explanation:** Create AGP from chromosome sizes.

### With options
**Args:** `hgFakeAgp -name=scaffold chrom.sizes > assembly.agp`
**Explanation:** Add scaffold name prefix.
