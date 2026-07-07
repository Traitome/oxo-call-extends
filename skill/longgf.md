---
name: longgf
category: expression
description: LongGF - Fast gene fusion detection from long-read RNA-seq data
tags: [longgf, expression, gene-fusion, RNA-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/WGLab/LongGF"
---

## Concepts

- **Gene Fusion Detection**: Detection of gene fusion events
- **Long-read RNA-seq**: Analysis of long-read RNA sequencing data
- **Fusion Transcripts**: Identification of fusion transcripts
- **Splice Junction**: Analysis of splice junctions
- **Transcriptomics**: Transcriptome analysis
- **Cancer Genomics**: Application in cancer genomics

## Pitfalls

- **Read Quality**: Poor quality reads affect detection
- **Mapping Quality**: Requires accurate read mapping
- **False Positives**: May produce false positive fusion calls
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization

## Examples

### Detect gene fusions
**Args:** `longgf -i reads.fastq -o fusions.txt`
**Explanation:** Detects gene fusions from long-read RNA-seq data.

### Reference annotation
**Args:** `longgf -i reads.fastq -o fusions.txt -a annotation.gtf`
**Explanation:** Uses gene annotation file.

### Reference genome
**Args:** `longgf -i reads.fastq -o fusions.txt -r reference.fasta`
**Explanation:** Uses reference genome.

### Threads
**Args:** `longgf -i reads.fastq -o fusions.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `longgf -i reads.fastq -o fusions.json -f json`
**Explanation:** Outputs results in JSON format.

### Verbose output
**Args:** `longgf -i reads.fastq -o fusions.txt -v`
**Explanation:** Provides detailed output.