---
name: fxtract
category: utility
description: Extract sequences from a fastx file given a subsequence or identifier.
tags: [fxtract, sequence extraction, FASTX, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ctSkennerton/fxtract"
---

## Concepts
- **Sequence Extraction**: Extracts sequences from FASTX files.
- **Pattern Matching**: Matches sequences by subsequence or identifier.
- **FASTX Support**: Works with both FASTQ and FASTA formats.
- **Flexible Search**: Supports various search criteria.
- **Efficient Processing**: Optimized for large sequence files.

## Pitfalls
- **Memory Usage**: Large files require significant memory.
- **Pattern Complexity**: Complex patterns may slow down search.
- **Output Format**: Limited output format options.
- **Case Sensitivity**: May be case-sensitive depending on options.
- **Wildcard Support**: Limited wildcard support in patterns.

## Examples
### Extract by identifier
**Args:** `fxtract -i reads.fastq -n seq123 -o extracted.fastq`
**Explanation:** Extracts sequence with identifier seq123.

### Extract by subsequence
**Args:** `fxtract -i reads.fastq -s ATGCGT -o extracted.fastq`
**Explanation:** Extracts sequences containing ATGCGT.

### Extract multiple identifiers
**Args:** `fxtract -i reads.fastq -l ids.txt -o extracted.fastq`
**Explanation:** Extracts sequences listed in ids.txt.

### Case-insensitive search
**Args:** `fxtract -i reads.fastq -s atgcgt -i -o extracted.fastq`
**Explanation:** Performs case-insensitive subsequence search.

### Output FASTA format
**Args:** `fxtract -i reads.fastq -n seq123 -f fasta -o extracted.fasta`
**Explanation:** Outputs in FASTA format.