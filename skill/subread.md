---
name: subread
category: alignment
description: High-performance read alignment, quantification, and mutation discovery.
tags: [subread, read-alignment, quantification, rnaseq]
author: oxo-call-community
source_url: "https://subread.sourceforge.net/SubreadUsersGuide.pdf"
---

## Concepts

- **Tool Overview**: subread (v2.1.1) is a high-performance tool for read alignment, quantification, and mutation discovery.
- **Core Function**: Aligns sequencing reads to reference genomes with high accuracy and speed.
- **Algorithm**: Uses seed-and-vote strategy for sensitive and accurate alignment.
- **Input/Output**: Input: FASTQ reads, reference genome; Output: SAM/BAM alignment, expression counts.
- **Applications**: RNA-seq analysis, ChIP-seq, DNA-seq, gene expression quantification.
- **Installation**: `conda install -c bioconda subread` or download from SourceForge.

## Pitfalls

- **Read Quality**: Low-quality reads affect alignment accuracy.
- **Memory Requirements**: Large reference genomes require significant memory.
- **Index Building**: Requires index building before alignment.
- **Parameter Tuning**: Incorrect parameters affect alignment quality.
- **Read Length**: Optimal for specific read lengths.
- **Computational Time**: Alignment of large datasets can be slow.

## Examples

### Display help
**Args:** `subread-align --help`
**Explanation:** Shows available options for read alignment.

### Basic read alignment
**Args:** `subread-align -i reference.index -r reads.fastq -o alignment.sam`
**Explanation:** Align reads to indexed reference genome.

### Build index
**Args:** `subread-buildindex -o reference.index reference.fasta`
**Explanation:** Build index for reference genome.

### Paired-end alignment
**Args:** `subread-align -i reference.index -r read1.fastq -R read2.fastq -o alignment.sam`
**Explanation:** Align paired-end reads.

### Quantification
**Args:** `featureCounts -a annotation.gtf -o counts.txt alignment.bam`
**Explanation:** Count reads per gene.

### Verbose mode
**Args:** `subread-align -i reference.index -r reads.fastq -o alignment.sam -v`
**Explanation:** Run with detailed logging.

### Output BAM
**Args:** `subread-align -i reference.index -r reads.fastq -o alignment.bam -b`
**Explanation:** Output alignment in BAM format.

### Batch processing
**Args:** `subread-align -i reference.index -r batch/ -o results/`
**Explanation:** Process multiple read files together.

### Generate report
**Args:** `subread-align -i reference.index -r reads.fastq -o alignment.sam --report`
**Explanation:** Generate comprehensive HTML report.
