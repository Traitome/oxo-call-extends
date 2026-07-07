---
name: vadr
category: bioinformatics
description: VADR - Viral Annotation and Diagnostics Resource.
tags: [vadr, viral-annotation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/ncbi/vadr"
---

## Concepts

- **Tool Overview**: VADR - A tool for viral genome annotation and diagnostics.
- **Core Function**: Annotates and validates viral genome sequences.
- **Input**: Viral genome sequences (FASTA).
- **Output**: Annotation results.
- **Installation**: Install via conda or source
- **Use Case**: Viral genomics, diagnostics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Database Requirements**: Requires viral reference database.

## Examples

### Annotate viral genome
**Args:** `vadr -i viral_genome.fasta -o annotation/`
**Explanation:** Annotate viral genome.

### With options
**Args:** `vadr -i viral_genome.fasta -o annotation/ -s strict`
**Explanation:** Use strict validation mode.
