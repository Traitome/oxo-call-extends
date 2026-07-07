---
name: uniqsketch
category: bioinformatics
description: UniqSketch - Sequence sketching tool.
tags: [uniqsketch, sequence-sketching, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/uniqsketch/"
---

## Concepts

- **Tool Overview**: UniqSketch - A tool for sequence sketching and comparison.
- **Core Function**: Creates compact sketches of sequences for comparison.
- **Input**: Sequence files (FASTA/FASTQ).
- **Output**: Sequence sketches.
- **Installation**: Install via pip or conda
- **Use Case**: Sequence comparison, clustering, bioinformatics.

## Pitfalls

- **Sketch Size**: Results depend on sketch size parameter.
- **Memory**: May require significant memory for large datasets.

## Examples

### Create sketch
**Args:** `uniqsketch sketch -i input.fasta -o sketch.txt`
**Explanation:** Create sequence sketch.

### Compare sketches
**Args:** `uniqsketch compare -i1 sketch1.txt -i2 sketch2.txt`
**Explanation:** Compare two sketches.
