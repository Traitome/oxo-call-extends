---
name: erne
category: alignment
description: "ERNE - Extended Randomized Numerical alignEr"
tags: [erne, alignment, sequence-alignment, RNA-seq, short-reads]
author: oxo-call-community
source_url: "http://erne.sourceforge.net"
---

## Concepts

- **Tool Overview**: ERNE (Extended Randomized Numerical alignEr) is a fast and memory-efficient sequence aligner designed for mapping short reads to reference genomes, particularly optimized for RNA-seq data.
- **Core Function**: Maps short sequencing reads to reference sequences with high speed and accuracy, supporting both DNA and RNA sequencing data.
- **Input/Output**: Input: Short reads (FASTQ), reference genome (FASTA). Output: Aligned reads (SAM/BAM), mapping statistics.
- **Algorithm**: Uses randomized numerical hashing for fast seed finding and dynamic programming for optimal alignment.
- **Key Features**: Ultra-fast mapping, low memory usage, support for paired-end reads, splice-aware alignment for RNA-seq, quality filtering.
- **Installation**: `conda install -c bioconda erne`

## Pitfalls

- **Reference Index**: Requires building an index for the reference genome.
- **Read Length**: Optimized for short reads; may not perform well with long reads.
- **Memory Management**: Large genomes require sufficient memory for indexing.
- **Parameter Tuning**: Default parameters may need adjustment for specific datasets.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Build reference index
**Args:** `erne-build -i ref.fasta -o ref_index`
**Explanation:** Builds index for reference genome.

### Map single-end reads
**Args:** `erne-mapper -i reads.fastq -r ref_index -o aligned.sam`
**Explanation:** Maps single-end reads to reference genome.

### Map paired-end reads
**Args:** `erne-mapper -1 reads_1.fastq -2 reads_2.fastq -r ref_index -o aligned.sam`
**Explanation:** Maps paired-end reads to reference genome.

### RNA-seq splice-aware mapping
**Args:** `erne-mapper -i reads.fastq -r ref_index -o aligned.sam --rna`
**Explanation:** Performs splice-aware mapping for RNA-seq data.

### Output BAM format
**Args:** `erne-mapper -i reads.fastq -r ref_index -o aligned.bam --bam`
**Explanation:** Outputs aligned reads in BAM format.