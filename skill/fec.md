---
name: fec
category: utility
description: "An error correction tool"
tags: [fec, utility, error-correction, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/zhangjuncsu/Fec"
---

## Concepts

- **Tool Overview**: fec is an error correction tool for sequencing data, designed to identify and correct sequencing errors in reads.
- **Core Function**: Corrects errors in sequencing reads to improve downstream analysis quality.
- **Input/Output**: Input: Sequencing reads (FASTQ). Output: Corrected reads (FASTQ).
- **Algorithm**: Uses k-mer based approach for error detection and correction.
- **Key Features**: Fast error correction, k-mer based, multiple sequencing platforms, paired-end support, quality improvement.
- **Installation**: `conda install -c bioconda fec`

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **K-mer Size**: K-mer size selection affects correction accuracy.
- **Data Quality**: Correction quality depends on input data quality.
- **Sequencing Depth**: Requires sufficient coverage for accurate correction.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic error correction
**Args:** `fec -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects errors in sequencing reads.

### Paired-end correction
**Args:** `fec -1 reads_1.fastq -2 reads_2.fastq -o corrected_`
**Explanation:** Corrects paired-end reads.

### K-mer size
**Args:** `fec -i reads.fastq -o corrected.fastq -k 31`
**Explanation:** Uses 31-mers for correction.

### Quality threshold
**Args:** `fec -i reads.fastq -o corrected.fastq -q 20`
**Explanation:** Sets minimum quality threshold.

### Statistics output
**Args:** `fec -i reads.fastq -o corrected.fastq -s stats.txt`
**Explanation:** Generates correction statistics.