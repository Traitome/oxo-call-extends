---
name: wgd
category: bioinformatics
description: WGD - Whole-genome duplication analysis.
tags: [wgd, comparative-genomics, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/wgd/"
---

## Concepts

- **Tool Overview**: WGD - Whole-genome duplication analysis tool.
- **Core Function**: Analyzes ancient whole-genome duplications.
- **Input**: Genome sequences.
- **Output**: WGD analysis results.
- **Installation**: Install via pip or conda
- **Use Case**: Comparative genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Detect WGD
**Args:** `wgd detect -i genome.fasta -o wgd.txt`
**Explanation:** Detect WGD events.

### With options
**Args:** `wgd dating -i wgd.txt -o dating.txt`
**Explanation:** Date WGD events.
