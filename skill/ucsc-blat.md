---
name: ucsc-blat
category: alignment
description: UCSC BLAT - Tool for rapid sequence alignment.
tags: [ucsc-blat, ucsc, sequence-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC BLAT - A tool for rapid DNA/protein sequence alignment.
- **Core Function**: Performs fast sequence alignment against large databases.
- **Input**: Query sequence, target database.
- **Output**: Alignment results in various formats.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence alignment, gene finding, homology search.

## Pitfalls

- **Memory**: May require significant memory for large databases.
- **Sensitivity**: May miss distant homologs.

## Examples

### Align sequence
**Args:** `blat target.fa query.fa output.psl`
**Explanation:** Align query sequence against target database.

### Protein alignment
**Args:** `blat -prot target.pep query.pep output.psl`
**Explanation:** Perform protein-protein alignment.
