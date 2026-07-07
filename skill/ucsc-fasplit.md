---
name: ucsc-fasplit
category: utility
description: UCSC faSplit - Tool for splitting FASTA files.
tags: [ucsc-fasplit, ucsc, fasta, sequence-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faSplit - A tool for splitting FASTA files into smaller files.
- **Core Function**: Splits multi-record FASTA into individual files or chunks.
- **Input**: FASTA file.
- **Output**: Multiple FASTA files.
- **Installation**: Part of UCSC utilities
- **Use Case**: File splitting, parallel processing, data organization.

## Pitfalls

- **Output Directory**: Requires existing output directory.
- **Memory**: May require significant memory for large files.

## Examples

### Split by sequence
**Args:** `faSplit byName genome.fa output_dir/`
**Explanation:** Split into individual sequence files.

### Split by size
**Args:** `faSplit about genome.fa 10000000 output_dir/`
**Explanation:** Split into ~10MB chunks.
