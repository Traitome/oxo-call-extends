---
name: any2fasta
category: formatting
description: Convert various sequence formats to FASTA format
tags: [any2fasta, formatting, FASTA, sequence-conversion, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/tseemann/any2fasta"
---

## Concepts

- **Tool Overview**: any2fasta (v0.8.1) - A Perl-based tool for converting various biological sequence formats to FASTA format.
- **Core Function**: Converts multiple sequence formats to standardized FASTA format while preserving sequence IDs and avoiding common mangling issues.
- **Supported Input Formats**:
  - GenBank (.gb, .gbk, .gbff)
  - EMBL (.embl)
  - GFF (with embedded FASTA sequences)
  - FASTA (.fa, .fasta, .fna, .faa)
  - FASTQ (.fq, .fastq)
  - CLUSTAL alignment
  - MUSCLE alignment
  - STOCKHOLM alignment
  - GFA assembly graph
  - PDB protein structure
- **Key Features**:
  - Handles compressed files (.gz, .bz2, .zip) automatically
  - Supports stdin/stdout piping
  - Processes multiple input files in different formats
  - Preserves sequence order in alignment formats
- **Installation**: `conda install -c bioconda any2fasta`

## Pitfalls

- **GFF Limitation**: Only extracts sequences embedded within GFF files (##FASTA section)
- **Ambiguous Characters**: Use `-n` flag carefully as it replaces ambiguous nucleotides with 'N', potentially losing information
- **Header Truncation**: `-t` flag removes description after first whitespace in headers
- **Format Detection**: Relies on file content detection; unusual formats may not be recognized

## Examples

### Basic conversion
**Args:** `any2fasta input.gbk > output.fasta`
**Explanation:** Converts GenBank file to FASTA format, writing to stdout.

### Convert multiple files
**Args:** `any2fasta file1.gbk file2.embl.gz file3.fastq > combined.fasta`
**Explanation:** Processes multiple files in different formats and combines output into single FASTA.

### Standardize FASTA output
**Args:** `any2fasta -u -n -t input.fasta > standardized.fasta`
**Explanation:** Converts to uppercase (-u), replaces ambiguous chars with N (-n), truncates headers at whitespace (-t).

### Handle compressed input
**Args:** `any2fasta genes.gff.gz > genes.fasta`
**Explanation:** Automatically decompresses and converts gzip-compressed GFF file.

### Read from stdin
**Args:** `cat input.gb | any2fasta - > output.fasta`
**Explanation:** Reads from stdin (using `-` as filename) and writes to stdout.

### Include GenBank version suffix
**Args:** `any2fasta -g input.gbk > output.fasta`
**Explanation:** Preserves the version suffix from GenBank LOCUS line in sequence ID.

### Strip description from headers
**Args:** `any2fasta -s input.fasta > output.fasta`
**Explanation:** Removes description portion from FASTA headers (>id desc becomes >id).

### Keep processing on errors
**Args:** `any2fasta -k file1.gbk file2.invalid file3.embl > output.fasta`
**Explanation:** Continues processing remaining files even if some inputs fail.