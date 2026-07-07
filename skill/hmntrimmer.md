---
name: hmntrimmer
category: qc
description: HmnTrimmer is a quality trimmer for NGS reads, performing adapter removal and quality-based trimming.
tags: [hmntrimmer, trimming, quality-control, NGS]
author: oxo-call-community
source_url: "https://github.com/guillaume-gricourt/HmnTrimmer"
---

## Concepts

- **Adapter Trimming**: Removes Illumina adapter sequences from read ends using sequence matching algorithms.
- **Quality-Based Trimming**: Trims low-quality bases from read ends using Phred quality score thresholds.
- **Sliding Window Trimming**: Implements sliding window approach to identify and remove low-quality regions within reads.
- **Paired-End Support**: Maintains read pairing information during trimming operations.
- **Multiple Quality Encodings**: Supports both Phred+33 (Illumina 1.8+) and Phred+64 quality score encodings.
- **Flexible Filtering**: Allows filtering based on minimum read length, maximum N content, and quality thresholds.

## Pitfalls

- **Adapter Sequence Database**: Requires up-to-date adapter sequence database; new adapter types may not be recognized.
- **Quality Encoding Detection**: Incorrect quality encoding detection can lead to improper trimming decisions.
- **Over-Trimming Risk**: Aggressive trimming parameters may remove biologically relevant sequence data.
- **Read Pair Synchronization**: Paired-end trimming must maintain read pair synchronization; misaligned pairs cause downstream issues.
- **Compression Handling**: Ensure proper handling of gzip-compressed input/output files.
- **Memory Management**: Processing large FASTQ files requires adequate memory allocation.

## Examples

### Basic paired-end trimming
**Args:** `hmntrimmer -i1 reads_R1.fastq -i2 reads_R2.fastq -o1 trimmed_R1.fastq -o2 trimmed_R2.fastq`
**Explanation:** Trims adapter sequences and low-quality bases from paired-end reads.

### Quality-based trimming with strict thresholds
**Args:** `hmntrimmer -i input.fastq -o trimmed.fastq -q 30 -w 5`
**Explanation:** Trims reads using a sliding window of 5 bases, requiring average quality ≥ Q30.

### Adapter-only trimming
**Args:** `hmntrimmer -i input.fastq -o trimmed.fastq --adapter-only`
**Explanation:** Removes only adapter sequences without quality trimming.

### Filter by minimum length
**Args:** `hmntrimmer -i input.fastq -o trimmed.fastq -l 50`
**Explanation:** Discards reads shorter than 50bp after trimming.

### Remove reads with excessive N content
**Args:** `hmntrimmer -i input.fastq -o filtered.fastq -n 0.1`
**Explanation:** Filters out reads containing more than 10% N bases.

### Process compressed files
**Args:** `hmntrimmer -i input.fastq.gz -o trimmed.fastq.gz`
**Explanation:** Handles gzip-compressed input and produces compressed output.