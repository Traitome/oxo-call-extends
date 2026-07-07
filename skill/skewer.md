---
name: skewer
category: qc
description: A fast and accurate adapter trimmer for paired-end reads
tags: [skewer, qc, adapter-trimming, preprocessing]
author: oxo-call-community
source_url: "https://github.com/relipmoc/skewer"
---

## Concepts

- **Tool Overview**: skewer (v0.2.2) - A fast adapter trimmer using bit-masked k-difference matching algorithm
- **Core Function**: Detects and removes adapter sequences from NGS reads with high accuracy
- **Input/Output**: Accepts FASTQ files (single-end or paired-end); outputs trimmed FASTQ files
- **Algorithm**: Implements bit-masked k-difference matching for efficient adapter detection
- **Installation**: `conda install -c bioconda skewer` or compile from source
- **Key Features**: Supports paired-end, mate-pair, and amplicon modes; handles quality-based trimming

## Pitfalls

- **Adapter Sequence**: Incorrect adapter sequence leads to failed trimming; use `-x` to specify
- **Quality Format**: Ensure correct quality format (Sanger/Solexa); use `-f auto` for auto-detection
- **Read Length**: Minimum read length after trimming defaults to 18; adjust with `-l`
- **Error Rate**: Default error rate (0.1) may need adjustment for low-quality data
- **Input Order**: For paired-end data, ensure correct order of input files
- **Compression**: Input files must be decompressed or use appropriate flags

## Examples

### Display help
**Args:** `skewer --help`
**Explanation:** Shows available options and usage information.

### Single-end trimming
**Args:** `skewer -x AGATCGGAAGAGC -q 3 sample.fastq -o trimmed`
**Explanation:** Trim single-end reads with specified adapter sequence.

### Paired-end trimming
**Args:** `skewer -x AGATCGGAAGAGC -y AGATCGGAAGAGCGTCGTGT sample_R1.fastq sample_R2.fastq -o trimmed`
**Explanation:** Trim paired-end reads with separate adapters for R1 and R2.

### With quality trimming
**Args:** `skewer -Q 9 -q 3 -t 4 sample_R1.fastq sample_R2.fastq -o trimmed`
**Explanation:** Apply quality trimming with mean quality threshold 9 and end quality 3, using 4 threads.

### Mate-pair mode
**Args:** `skewer -m mp -j CTGTCTCTTATACACATCTAGATGTGTATAAGAGACAG lmp_R1.fastq lmp_R2.fastq -o trimmed`
**Explanation:** Process mate-pair reads with junction adapter.

### Amplicon mode with barcodes
**Args:** `skewer -m ap --cut 0,6 --qiime -x forward.fa -y reverse.fa mix_R1.fastq mix_R2.fastq -o trimmed`
**Explanation:** Process amplicon data with barcode trimming for QIIME.

### Compressed output
**Args:** `skewer -z -x AGATCGGAAGAGC sample.fastq -o trimmed`
**Explanation:** Output trimmed reads in gzip compressed format.