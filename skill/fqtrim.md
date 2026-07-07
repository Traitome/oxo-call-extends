---
name: fqtrim
category: qc
description: fqtrim is a versatile stand-alone utility that can be used to trim adapters, poly-A tails, terminal unknown bases (Ns) and low quality 3' regions in reads from high-throughput next-generation sequencing machines.
tags: [fqtrim, trimming, quality control, adapters]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/fqtrim/"
---

## Concepts
- **Adapter Trimming**: Removes sequencing adapters from read ends.
- **Poly-A Tail Trimming**: Trims poly-A tails from RNA-seq reads.
- **Quality Trimming**: Removes low-quality bases from 3' ends.
- **N Base Removal**: Trims terminal unknown bases (Ns).
- **Paired-End Support**: Handles paired-end sequencing data.

## Pitfalls
- **Adapter Sequence**: Requires correct adapter sequence specification.
- **Over-Trimming**: May remove valid sequence if parameters are too aggressive.
- **Quality Threshold**: Default quality thresholds may not suit all data.
- **Memory Usage**: Processing large files requires sufficient memory.
- **Output Format**: Limited output format options.

## Examples
### Basic adapter trimming
**Args:** `fqtrim -a AGATCGGAAGAGC -i reads.fastq -o trimmed.fastq`
**Explanation:** Trims the specified adapter sequence from reads.

### Trim poly-A tails
**Args:** `fqtrim -A -i reads.fastq -o trimmed.fastq`
**Explanation:** Trims poly-A tails from the 3' ends of reads.

### Quality trimming
**Args:** `fqtrim -q 20 -i reads.fastq -o trimmed.fastq`
**Explanation:** Trims bases with quality score below 20 from 3' ends.

### Paired-end trimming
**Args:** `fqtrim -a AGATCGGAAGAGC -1 reads_R1.fastq -2 reads_R2.fastq -o trimmed_`
**Explanation:** Trims adapters from paired-end reads.

### Trim N bases
**Args:** `fqtrim -N -i reads.fastq -o trimmed.fastq`
**Explanation:** Removes terminal unknown bases (Ns) from reads.