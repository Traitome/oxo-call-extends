---
name: telseq
category: analysis
description: Telseq - Telomere Length Estimation from short-read sequencing data.
tags: [telseq, telomere, telomere-length, short-read, wgs, ngs]
author: oxo-call-community
source_url: "https://github.com/zd1/telseq"
---

## Concepts

- **Tool Overview**: Telseq - A tool for estimating average telomere length from whole genome sequencing (WGS) data.
- **Core Function**: Calculates telomere length based on the ratio of telomeric reads to single-copy gene reads using short-read sequencing data.
- **Input**: Whole genome sequencing reads (FASTQ) or pre-aligned BAM files.
- **Output**: Telomere length estimate in kilobases, quality metrics, and per-sample comparison.
- **Installation**: `pip install telseq` or `conda install -c bioconda telseq`
- **Use Case**: Population studies of telomere length, cancer research, aging biomarkers.

## Pitfalls

- **Short Reads**: Works with short reads but may be less accurate than long-read methods.
- **Coverage**: Requires sufficient WGS coverage (typically >10x) for reliable estimates.
- **Library Preparation**: Some library prep methods may bias telomere representation.

## Examples

### Estimate telomere length
**Args:** `telseq -i WGS_reads.fastq.gz -o telomere_length.txt`
**Explanation:** Calculate telomere length from WGS data.

### From BAM file
**Args:** `telseq -b aligned.bam -o telomere_results.txt`
**Explanation:** Use pre-aligned BAM file for telomere length estimation.
