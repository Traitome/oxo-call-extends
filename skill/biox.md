---
name: biox
category: utility
description: Biological Sequence Compression and Analysis Tool
tags: [compression, sequence-analysis, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/TianMayCry9/BioX"
---

## Concepts
- **Tool Overview**: BioX is an efficient, lossless compression tool for biological sequence data, with additional sequence analysis and phylogenetic tree construction features.
- **Compression**: Lossless compression specifically optimized for biological sequences (DNA, RNA, protein).
- **Analysis Features**: Sequence statistics, phylogenetic tree construction.
- **Applications**: Sequence storage optimization, data transfer, phylogenetic analysis.

## Pitfalls
- **Decompression Required**: Compressed files must be decompressed before use with most tools.

## Examples
### Compress FASTA file
**Args:** `biox compress -i sequences.fa -o sequences.biox`
**Explanation:** Compresses FASTA file using BioX compression.

### Decompress file
**Args:** `biox decompress -i sequences.biox -o sequences.fa`
**Explanation:** Decompresses BioX file back to FASTA format.
