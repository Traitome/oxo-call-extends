---
name: selectfasta
category: sequence-analysis
description: selectfasta - Select sequences from FASTA/FASTQ by header names
tags: ["selectfasta", "sequence-analysis", "FASTA", "FASTQ"]
author: oxo-call-community
source_url: "https://github.com/andvides/selectFasta"
---

## Concepts

- **Tool Overview**: selectfasta (v3.1) selects sequences from FASTA/FASTQ files by header names.
- **Core Function**: Filters sequence files based on header lists.
- **Algorithm**: Uses pattern matching to identify and extract sequences.
- **Input/Output**: Accepts FASTA/FASTQ files and header lists; produces filtered sequences.
- **Sequence Filtering**: Focuses on selective extraction of sequences.
- **Applications**: Sequence analysis, data preprocessing, and subset selection.

## Pitfalls

- **Header Format**: Requires consistent header format in input files.
- **Case Sensitivity**: May be case sensitive depending on implementation.
- **Memory Usage**: High memory requirements for large sequence files.
- **Input Format**: Requires correct FASTA/FASTQ format.
- **Performance**: May be slow for very large files.
- **Duplicate Headers**: May have issues with duplicate headers.

## Examples

### Select sequences
**Args:** `selectfasta -i input.fasta -l headers.txt -o output.fasta`
**Explanation:** `-i` input FASTA; `-l` header list; `-o` output file.

### FASTQ input
**Args:** `selectfasta -i input.fastq -l headers.txt -o output.fastq -f fastq`
**Explanation:** `-f fastq` specifies FASTQ format.

### Inverse selection
**Args:** `selectfasta -i input.fasta -l headers.txt -o output.fasta -v`
**Explanation:** `-v` inverts selection (exclude specified headers).

### Verbose logging
**Args:** `selectfasta -i input.fasta -l headers.txt -v -o output.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `selectfasta --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `selectfasta --version`
**Explanation:** Shows current version.

### Compressed input
**Args:** `selectfasta -i input.fasta.gz -l headers.txt -o output.fasta`
**Explanation:** Handles gzip compressed input.