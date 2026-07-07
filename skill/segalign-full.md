---
name: segalign-full
category: alignment
description: SegAlign - Scalable GPU-based whole genome aligner
tags: ["segalign-full", "alignment", "GPU", "whole-genome"]
author: oxo-call-community
source_url: "https://github.com/galaxyproject/SegAlign"
---

## Concepts

- **Tool Overview**: SegAlign (v0.1.2.7) is a scalable GPU-based whole genome aligner.
- **Core Function**: Aligns sequencing reads to reference genomes using GPU acceleration.
- **Algorithm**: Uses parallel computing on GPU for fast alignment.
- **Input/Output**: Accepts FASTQ reads and produces SAM/BAM alignments.
- **GPU Acceleration**: Leverages GPU for high-performance alignment.
- **Applications**: Whole-genome sequencing alignment, variant calling, and genome analysis.

## Pitfalls

- **GPU Requirements**: Requires compatible GPU hardware.
- **Memory Usage**: High memory requirements for large genomes.
- **Software Dependencies**: Requires GPU drivers and CUDA toolkit.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Index**: Requires pre-built index for reference genome.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Basic alignment
**Args:** `segalign-full -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** `-i` input FASTQ; `-r` reference genome; `-o` output SAM.

### BAM output
**Args:** `segalign-full -i reads.fastq -r reference.fasta -o alignments.bam --bam`
**Explanation:** Outputs BAM format instead of SAM.

### GPU selection
**Args:** `segalign-full -i reads.fastq -r reference.fasta -g 0 -o alignments.sam`
**Explanation:** `-g 0` uses GPU device 0.

### Verbose logging
**Args:** `segalign-full -i reads.fastq -r reference.fasta -v -o alignments.sam`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `segalign-full -i reads.fastq -r reference.fasta -t 8 -o alignments.sam`
**Explanation:** `-t 8` uses 8 CPU threads.

### Quality filtering
**Args:** `segalign-full -i reads.fastq -r reference.fasta -q 20 -o alignments.sam`
**Explanation:** `-q 20` filters reads with quality below 20.

### Help command
**Args:** `segalign-full --help`
**Explanation:** Shows available commands and options.