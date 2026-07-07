---
name: scramble
category: alignment
description: scramble - Soft Clipped Read Alignment Mapper
tags: ["scramble", "alignment", "RNA-seq", "splicing"]
author: oxo-call-community
source_url: "https://github.com/GeneDx/scramble"
---

## Concepts

- **Tool Overview**: scramble (v1.0.2) is a Soft Clipped Read Alignment Mapper.
- **Core Function**: Aligns soft-clipped reads to reference genome for splice junction detection.
- **Algorithm**: Uses dynamic programming for optimal alignment of soft-clipped reads.
- **Input/Output**: Accepts FASTA/FASTQ files and produces SAM/BAM alignments.
- **Splice Junction**: Specifically designed for detecting splice junctions from RNA-seq data.
- **Applications**: RNA-seq analysis, alternative splicing detection, and transcriptomics.

## Pitfalls

- **Data Quality**: Results depend on input sequence quality.
- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Genome**: Requires compatible reference genome.
- **False Positives**: May report false splice junctions.

## Examples

### Basic alignment
**Args:** `scramble -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** `-i` input reads; `-r` reference; `-o` output SAM.

### BAM output
**Args:** `scramble -i reads.fastq -r reference.fasta -o alignments.bam --bam`
**Explanation:** Outputs BAM format instead of SAM.

### Splice junction detection
**Args:** `scramble -i reads.fastq -r reference.fasta -o junctions.bed --junctions`
**Explanation:** `--junctions` outputs splice junctions in BED format.

### Paired-end reads
**Args:** `scramble -i reads_1.fastq -i2 reads_2.fastq -r reference.fasta -o alignments.sam`
**Explanation:** `-i2` specifies second read pair.

### Verbose logging
**Args:** `scramble -i reads.fastq -r reference.fasta -v -o alignments.sam`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `scramble -i reads.fastq -r reference.fasta -t 8 -o alignments.sam`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Quality filtering
**Args:** `scramble -i reads.fastq -r reference.fasta -q 20 -o alignments.sam`
**Explanation:** `-q 20` filters reads with quality below 20.