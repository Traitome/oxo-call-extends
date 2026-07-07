---
name: fast2q
category: expression
description: "A Python3 program that counts sequence occurrences in FASTQ files."
tags: [fast2q, expression, FASTQ, sequence-counting, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/afombravo/2FAST2Q"
---

## Concepts

- **Tool Overview**: fast2q is a Python3 program for counting sequence occurrences in FASTQ files, commonly used for small RNA sequencing analysis.
- **Core Function**: Counts and quantifies sequence reads in FASTQ files, providing expression levels for each unique sequence.
- **Input/Output**: Input: FASTQ file. Output: Sequence counts (CSV/TSV), abundance statistics.
- **Algorithm**: Parses FASTQ files and counts occurrences of each unique sequence.
- **Key Features**: FASTQ parsing, sequence counting, abundance quantification, batch processing, quality filtering.
- **Installation**: `conda install -c bioconda fast2q`

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **Sequence Quality**: Poor quality sequences may affect counting accuracy.
- **Format Compatibility**: Requires standard FASTQ format.
- **Duplicate Reads**: May count duplicate reads multiple times.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic sequence counting
**Args:** `fast2q -i reads.fastq -o counts.csv`
**Explanation:** Counts sequence occurrences in FASTQ file.

### With quality filtering
**Args:** `fast2q -i reads.fastq -o counts.csv -q 20`
**Explanation:** Filters reads by quality score before counting.

### Minimum count threshold
**Args:** `fast2q -i reads.fastq -o counts.csv -m 10`
**Explanation:** Only reports sequences with at least 10 occurrences.

### Paired-end reads
**Args:** `fast2q -1 reads_1.fastq -2 reads_2.fastq -o counts.csv`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `fast2q -i fastq_files/ -o results/ --batch`
**Explanation:** Processes multiple FASTQ files in batch mode.