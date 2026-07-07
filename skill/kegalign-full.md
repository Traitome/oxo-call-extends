---
name: kegalign-full
category: alignment
description: KegAlign - A Scalable GPU-Based Whole Genome Aligner.
tags: [kegalign-full, alignment, GPU, whole genome, scalable]
author: oxo-call-community
source_url: "https://github.com/galaxyproject/KegAlign/blob/main/README.md"
---

## Concepts

- **Tool Overview**: kegalign-full (v0.1.2.9) - GPU-accelerated whole genome aligner.
- **GPU Acceleration**: Uses GPU for parallel alignment.
- **Whole Genome**: Designed for whole genome alignment.
- **Scalability**: Scales to large genomes.
- **Speed**: Significantly faster than CPU-based aligners.
- **Memory Efficiency**: Optimized memory usage.

## Pitfalls

- **GPU Requirements**: Requires NVIDIA GPU with CUDA.
- **CUDA Version**: Requires specific CUDA version.
- **Memory Usage**: GPU memory can be limiting.
- **Input Size**: Very large genomes may exceed GPU memory.
- **Installation**: Complex GPU setup required.
- **Platform Specific**: Limited to systems with compatible GPUs.

## Examples

### Align reads to genome
**Args:** `kegalign -i reads.fastq -r genome.fasta -o alignments.bam`
**Explanation:** Aligns reads to reference genome using GPU.

### Use multiple GPUs
**Args:** `kegalign -i reads.fastq -r genome.fasta -o alignments.bam -g 2`
**Explanation:** Uses 2 GPUs for parallel processing.

### Build genome index
**Args:** `kegalign index -i genome.fasta -o genome.idx`
**Explanation:** Builds GPU-optimized genome index.

### Paired-end alignment
**Args:** `kegalign -i reads_1.fastq -j reads_2.fastq -r genome.fasta -o alignments.bam`
**Explanation:** Aligns paired-end reads.

### Output SAM format
**Args:** `kegalign -i reads.fastq -r genome.fasta -o alignments.sam --sam`
**Explanation:** Outputs alignments in SAM format.

### Quality filtering
**Args:** `kegalign -i reads.fastq -r genome.fasta -o alignments.bam -q 30`
**Explanation:** Filters alignments by mapping quality.