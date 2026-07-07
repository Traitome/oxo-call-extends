---
name: mfqe
category: utility
description: mfqe is a tool for quickly separating fasta and fastq files.
tags: [mfqe, utility, sequence]
author: oxo-call-community
source_url: "https://github.com/wwood/mfqe"
---

## Concepts

- **Tool Overview**: mfqe v0.5.0 is a fast tool for separating FASTA and FASTQ sequence files.
- **Core Function**: Separates mixed sequence files into FASTA and FASTQ formats.
- **Sequence Separation**: Quickly separates interleaved sequence files.
- **Format Detection**: Automatically detects sequence file formats.
- **Input/Output**: Accepts mixed sequence files; outputs separated FASTA and FASTQ files.
- **Efficient Processing**: Optimized for fast processing of large sequence files.

## Pitfalls

- **Memory Requirements**: Processing large files may require significant memory.
- **Input Format**: Requires correct input format for separation.
- **Parameter Tuning**: May require parameter adjustment for specific use cases.
- **Data Quality**: Separation accuracy depends on input data quality.
- **File Size**: Very large files may take time to process.
- **Format Detection**: May fail with non-standard sequence formats.

## Examples

### Separate sequence files
**Args:** `mfqe -i mixed.fastq -o fasta/`
**Explanation:** Separates mixed sequence file into FASTA and FASTQ.

### With specific output directory
**Args:** `mfqe -i mixed.fastq -f fasta_output.fasta -q fastq_output.fastq`
**Explanation:** Specifies separate output files for FASTA and FASTQ.

### Batch processing
**Args:** `mfqe -i sequences/ -o separated/`
**Explanation:** Processes multiple sequence files in batch mode.

### Force FASTQ output
**Args:** `mfqe -i sequences.fasta -o output.fastq -f fastq`
**Explanation:** Converts FASTA to FASTQ format.

### Force FASTA output
**Args:** `mfqe -i sequences.fastq -o output.fasta -f fasta`
**Explanation:** Converts FASTQ to FASTA format.