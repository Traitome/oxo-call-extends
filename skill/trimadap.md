---
name: trimadap
category: utility
description: TrimAdap - Tool for trimming adapter sequences from sequencing reads.
tags: [trimadap, adapter-trimming, sequencing-data, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/trimadap"
---

## Concepts

- **Tool Overview**: TrimAdap - A tool for trimming adapter sequences and low-quality bases from sequencing reads.
- **Core Function**: Removes adapter sequences, trims low-quality ends, and filters reads.
- **Input**: FASTQ files, adapter sequences.
- **Output**: Trimmed FASTQ files, trimming statistics.
- **Installation**: `pip install trimadap` or `conda install -c bioconda trimadap`
- **Use Case**: Sequencing data preprocessing, quality control, read cleaning.

## Pitfalls

- **Adapter Sequences**: Requires accurate adapter sequence information.
- **Over-trimming**: May trim legitimate sequence if parameters are too aggressive.

## Examples

### Trim adapters
**Args:** `trimadap -i reads.fastq -a adapters.fasta -o trimmed.fastq`
**Explanation:** Trim adapter sequences from reads.

### Quality trimming
**Args:** `trimadap -i raw.fastq -q 20 -o clean.fastq`
**Explanation:** Trim low-quality bases from reads.
