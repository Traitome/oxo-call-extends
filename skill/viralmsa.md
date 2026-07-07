---
name: viralmsa
category: bioinformatics
description: viralMSA - Viral multiple sequence alignment.
tags: [viralmsa, viral-genomics, msa, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/viralmsa/"
---

## Concepts

- **Tool Overview**: viralMSA - Multiple sequence alignment for viruses.
- **Core Function**: Aligns multiple viral sequences.
- **Input**: Viral sequences.
- **Output**: Alignment.
- **Installation**: Install via pip or conda
- **Use Case**: Viral genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Time**: May be slow for many sequences.

## Examples

### Align sequences
**Args:** `viralmsa -i sequences.fasta -o alignment.fasta`
**Explanation:** Align viral sequences.

### With options
**Args:** `viralmsa -i sequences.fasta -o alignment.fasta -t 8`
**Explanation:** Use 8 threads.
