---
name: leehom
category: qc
description: Maximum-likelihood adapter trimming and removal for sequencing reads
tags: [leehom, qc, adapter-trimming, sequencing, read-processing]
author: oxo-call-community
source_url: "https://github.com/grenaud/leeHom"
---

## Concepts

- **Adapter Trimming**: Removes adapter sequences from reads
- **Maximum Likelihood**: Uses ML approach for trimming
- **Paired-end Support**: Handles paired-end sequencing data
- **Quality Trimming**: Also performs quality trimming
- **Adapter Detection**: Automatically detects adapter sequences
- **Illumina Support**: Designed for Illumina sequencing data

## Pitfalls

- **Adapter Sequences**: Requires known adapter sequences
- **Read Quality**: Poor quality affects adapter detection
- **Over-trimming**: May trim legitimate sequence
- **Under-trimming**: May leave adapter sequences
- **Paired-end Sync**: Requires synchronized paired-end reads
- **Base Quality**: Low quality bases affect trimming decisions

## Examples

### Trim adapters
**Args:** `leeHom -1 reads_1.fastq -2 reads_2.fastq -o trimmed/`
**Explanation:** Trims adapters from paired-end reads.

### Single-end mode
**Args:** `leeHom -f reads.fastq -o trimmed.fastq`
**Explanation:** Processes single-end reads.

### Specify adapter
**Args:** `leeHom -1 reads_1.fastq -2 reads_2.fastq -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -o trimmed/`
**Explanation:** Uses custom adapter sequence.

### Quality trimming
**Args:** `leeHom -1 reads_1.fastq -2 reads_2.fastq -q 20 -o trimmed/`
**Explanation:** Trims low quality bases (Q < 20).

### Minimum length
**Args:** `leeHom -1 reads_1.fastq -2 reads_2.fastq -m 50 -o trimmed/`
**Explanation:** Discards reads shorter than 50bp.

### Batch processing
**Args:** `leeHom batch -d raw_reads/ -o trimmed_reads/`
**Explanation:** Processes multiple sample directories.