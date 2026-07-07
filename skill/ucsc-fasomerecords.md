---
name: ucsc-fasomerecords
category: utility
description: UCSC faSomeRecords - Tool for extracting multiple FASTA records.
tags: [ucsc-fasomerecords, ucsc, fasta, sequence-extraction, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faSomeRecords - A tool for extracting multiple records from FASTA.
- **Core Function**: Extracts sequences by name from multi-record FASTA.
- **Input**: FASTA file, list of sequence names.
- **Output**: Selected FASTA records.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence extraction, subset selection, data preparation.

## Pitfalls

- **Sequence Names**: Requires exact name matches.
- **Memory**: May require significant memory for large files.

## Examples

### Extract records
**Args:** `faSomeRecords genome.fa names.txt > subset.fa`
**Explanation:** Extract specified sequences.

### From stdin
**Args:** `cat names.txt | faSomeRecords genome.fa stdin > subset.fa`
**Explanation:** Extract from piped names.
