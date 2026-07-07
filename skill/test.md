---
name: test
category: formatting
description: Test recipe demonstrating bioinformatics tool documentation standards, modeled after seqtk.
tags: [test, formatting, bioinformatics, sequence]
author: oxo-call-community
source_url: "https://github.com/lh3/seqtk"
---

## Concepts

- **Tool Overview**: test is a demonstration recipe for bioinformatics tool documentation, based on the seqtk sequence processing tool.
- **Core Function**: Serves as a template for documenting bioinformatics command-line tools with standard sections.
- **Input/Output**: Accepts FASTA/Q sequence files and produces processed sequence outputs.
- **Installation**: `conda install -c bioconda test` (Note: this is a test package for demonstration)
- **Common Operations**: Sequence subsampling, quality filtering, format conversion, and statistics generation.
- **Documentation Template**: Follows standard bioinformatics tool documentation with Concepts, Pitfalls, and Examples sections.

## Pitfalls

- **Sequence Format**: Ensure input files are valid FASTA or FASTQ format to avoid parsing errors.
- **Quality Scores**: FASTQ files must have valid Phred quality scores (typically ASCII-33 or ASCII-64).
- **Memory Usage**: Processing large sequence files may require sufficient memory; consider subsampling first.
- **Compression**: When using gzip-compressed files, ensure proper decompression or tool support for streaming.
- **Output Redirection**: Use shell redirection (> or >>) to save output to files instead of printing to console.

## Examples

### Display help information
**Args:** `test --help`
**Explanation:** Show available commands and options for the tool.

### Subsample sequences
**Args:** `test sample -s 100 input.fastq output.fastq`
**Explanation:** Randomly subsample 100 reads from input FASTQ file and save to output.

### Convert FASTA to FASTQ
**Args:** `test seq -Q input.fasta output.fastq`
**Explanation:** Convert FASTA sequences to FASTQ format, adding dummy quality scores.

### Extract sequences by name
**Args:** `test subseq input.fasta names.txt output.fasta`
**Explanation:** Extract sequences whose names match those in names.txt from input.fasta.

### Generate sequence statistics
**Args:** `test stat input.fastq`
**Explanation:** Print basic statistics including total reads, bases, and quality metrics.