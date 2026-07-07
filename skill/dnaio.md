---
name: dnaio
category: utility
description: dnaio - Fast FASTA/FASTQ file I/O library.
tags: [dnaio, utility, fasta, fastq, io, sequence]
author: oxo-call-community
source_url: "https://github.com/marcelm/dnaio"
---

## Concepts

- **Tool Overview**: dnaio is a fast library for reading and writing FASTA/FASTQ files.
- **Core Function**: Provides efficient I/O operations for sequence files with minimal overhead.
- **Input/Output**: Input: FASTA/FASTQ files. Output: Processed sequences, filtered data.
- **Algorithm**: Uses optimized parsing for fast sequence file I/O.
- **Key Features**: Fast parsing, memory efficient, paired-end support, quality filtering, batch processing.
- **Installation**: `conda install -c bioconda dnaio`

## Pitfalls

- **Input Requirements**: Requires valid FASTA or FASTQ format.
- **Quality Scores**: FASTQ files must have valid quality score encoding.
- **File Size**: Very large files may require streaming approach.
- **Encoding Issues**: Must handle different quality score encodings correctly.
- **Memory Usage**: Loading entire files into memory may require significant RAM.

## Examples

### Process sequence files
**Args:** `dnaio --input reads.fq --output processed.fq`
**Explanation:** Processes FASTA/FASTQ files efficiently.

### Filter by quality
**Args:** `dnaio --input reads.fq --output filtered.fq --min-quality 20`
**Explanation:** Filter reads by minimum quality score.

### Paired-end processing
**Args:** `dnaio --input R1.fq R2.fq --output processed_R1.fq processed_R2.fq --paired`
**Explanation:** Process paired-end read files.

### Convert format
**Args:** `dnaio --input sequences.fa --output sequences.fq --convert fastq`
**Explanation:** Convert FASTA to FASTQ format.

### Batch processing
**Args:** `dnaio --input-dir fastq_files/ --output-dir processed/`
**Explanation:** Process multiple sequence files in batch.