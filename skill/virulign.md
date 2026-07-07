---
name: virulign
category: bioinformatics
description: Virulign - Viral sequence alignment.
tags: [virulign, viral-genomics, sequence-alignment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rega-cev/virulign"
---

## Concepts

- **Tool Overview**: Virulign - Aligns viral sequences to reference.
- **Core Function**: Performs multiple sequence alignment of viral sequences.
- **Input**: Viral sequences.
- **Output**: Aligned sequences.
- **Installation**: Install via pip or conda
- **Use Case**: Viral genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Reference**: Requires reference sequence.

## Examples

### Align sequences
**Args:** `virulign -i sequences.fasta -o alignment.fasta`
**Explanation:** Align viral sequences.

### With options
**Args:** `virulign -i sequences.fasta -o alignment.fasta -r ref.fasta`
**Explanation:** Use reference sequence.
