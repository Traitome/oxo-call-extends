---
name: ucsc-twobittofa
category: utility
description: UCSC twoBitToFa - Tool for converting twoBit to FASTA.
tags: [ucsc-twobittofa, ucsc, twobit, fasta, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC twoBitToFa - A tool for converting twoBit to FASTA format.
- **Core Function**: Extracts sequences from twoBit files to FASTA.
- **Input**: TwoBit file, optionally with region specification.
- **Output**: FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, sequence extraction, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Region Specification**: Requires correct region format.

## Examples

### Convert twoBit to FASTA
**Args:** `twoBitToFa input.2bit output.fa`
**Explanation:** Convert entire twoBit to FASTA.

### Extract specific region
**Args:** `twoBitToFa input.2bit stdout -seq=chr1:1-1000`
**Explanation:** Extract specific region.
