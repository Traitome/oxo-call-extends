---
name: dinopy
category: utility
description: dinopy - Python library for FASTA/FASTQ I/O with dinucleotide analysis.
tags: [dinopy, utility, fasta, fastq, dinucleotide]
author: oxo-call-community
source_url: "https://github.com/bioinformatics-pt/dinopy"
---

## Concepts

- **Tool Overview**: dinopy is a Python library for reading and writing FASTA/FASTQ files with dinucleotide analysis capabilities.
- **Core Function**: Provides efficient file I/O for sequence data with additional dinucleotide frequency analysis.
- **Input/Output**: Input: FASTA/FASTQ files. Output: Processed sequences, dinucleotide statistics, quality reports.
- **Algorithm**: Parses sequence files efficiently and calculates dinucleotide frequencies.
- **Key Features**: Fast sequence parsing, dinucleotide analysis, quality score handling, batch processing, format conversion.
- **Installation**: `conda install -c bioconda dinopy`

## Pitfalls

- **Input Requirements**: Requires valid FASTA or FASTQ format with proper headers.
- **File Size**: May require significant memory for very large sequence files.
- **Quality Scores**: FASTQ files must have valid quality score encoding.
- **Ambiguous Bases**: May need special handling for ambiguous nucleotide codes.
- **Encoding Issues**: Must handle different quality score encodings correctly.

## Examples

### Analyze dinucleotide frequencies
**Args:** `dinopy --input reads.fq --output stats.tsv`
**Explanation:** Analyzes dinucleotide frequencies in FASTQ file.

### Convert FASTA to FASTQ
**Args:** `dinopy convert --input sequences.fa --output sequences.fq`
**Explanation:** Convert FASTA file to FASTQ format.

### Filter by sequence length
**Args:** `dinopy filter --input reads.fq --output filtered.fq --min-length 50`
**Explanation:** Filter sequences by minimum length.

### Generate quality report
**Args:** `dinopy quality --input reads.fq --output report.html`
**Explanation:** Generate quality control report for sequencing data.

### Batch processing
**Args:** `dinopy batch --input-dir fastq_files/ --output-dir results/`
**Explanation:** Process multiple sequence files in batch.