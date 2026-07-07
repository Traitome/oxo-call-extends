---
name: ucsc-randomlines
category: utility
description: UCSC randomLines - Tool for selecting random lines.
tags: [ucsc-randomlines, ucsc, random, sampling, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC randomLines - A tool for selecting random lines from files.
- **Core Function**: Randomly selects lines from input files.
- **Input**: Input file.
- **Output**: Randomly selected lines.
- **Installation**: Part of UCSC utilities
- **Use Case**: Random sampling, data analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Random Seed**: Results may vary without fixed seed.

## Examples

### Select random lines
**Args:** `randomLines -count=100 input.txt > random.txt`
**Explanation:** Select 100 random lines.

### With options
**Args:** `randomLines -count=100 -seed=42 input.txt > random.txt`
**Explanation:** Select with fixed seed.
