---
name: ucsc-liftup
category: utility
description: UCSC liftUp - Tool for lifting coordinates.
tags: [ucsc-liftup, ucsc, coordinate-conversion, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC liftUp - A tool for lifting coordinates using chain files.
- **Core Function**: Lifts coordinates from one assembly to another.
- **Input**: Coordinate file, chain file.
- **Output**: Lifted coordinates.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome assembly conversion, coordinate mapping.

## Pitfalls

- **Chain File**: Requires appropriate chain file.
- **Memory**: May require significant memory for large files.

## Examples

### Lift up coordinates
**Args:** `liftUp input.bed hg19ToHg38.over.chain output.bed`
**Explanation:** Lift coordinates to target assembly.

### With options
**Args:** `liftUp -verbose input.bed chain.chain output.bed`
**Explanation:** Lift with verbose output.
