---
name: unmerge
category: bioinformatics
description: UnMerge - Tool for splitting merged sequences.
tags: [unmerge, sequence-splitting, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/unmerge/"
---

## Concepts

- **Tool Overview**: UnMerge - A tool for splitting merged sequences.
- **Core Function**: Separates merged sequences into individual components.
- **Input**: Merged sequence file.
- **Output**: Individual sequence files.
- **Installation**: Install via pip or conda
- **Use Case**: Sequence processing, data cleaning, bioinformatics.

## Pitfalls

- **Overlapping Sequences**: May struggle with complex overlaps.
- **Memory**: May require significant memory for large files.

## Examples

### Split merged sequences
**Args:** `unmerge -i merged.fasta -o split/`
**Explanation:** Split merged sequences.

### With options
**Args:** `unmerge -i merged.fasta -o split/ -m 10`
**Explanation:** Maximum overlap allowed.
