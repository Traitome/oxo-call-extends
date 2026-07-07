---
name: scallop-lr
category: expression
description: Scallop-LR - reference-based transcript assembler for long-read RNA-seq
tags: ["scallop-lr", "expression", "RNA-seq", "long-read", "transcript-assembly"]
author: oxo-call-community
source_url: "https://github.com/Kingsford-Group/lrassemblyanalysis"
---

## Concepts

- **Tool Overview**: Scallop-LR (v0.9.2) is a reference-based transcriptome assembler specifically designed for long-read RNA-seq data from PacBio or Oxford Nanopore platforms.
- **Core Function**: Assembles full-length transcripts from long-read RNA-seq alignments.
- **Algorithm**: Optimized for long reads with higher error rates compared to short reads.
- **Input/Output**: Accepts BAM files with long-read alignments and produces transcript GTF annotations.
- **Long-Read Optimization**: Handles high error rates and variable read lengths characteristic of long-read sequencing.
- **Applications**: Full-length transcript reconstruction, isoform discovery, and alternative splicing analysis.

## Pitfalls

- **Long-Read Specific**: Designed for long reads, may not work well with short-read data.
- **Error Rate**: Sensitive to high error rates in raw long-read data.
- **Computational Resources**: High memory requirements for processing long reads.
- **Alignment Quality**: Results depend on proper alignment of long reads.
- **Reference Genome**: Requires well-annotated reference genome for best results.
- **Runtime**: Processing time can be significant for large datasets.

## Examples

### Basic long-read assembly
**Args:** `scallop-lr -i alignments.bam -o transcripts.gtf`
**Explanation:** `-i` input BAM with long-read alignments; `-o` output GTF.

### With reference genome
**Args:** `scallop-lr -i alignments.bam -r reference.fasta -o transcripts.gtf`
**Explanation:** `-r` reference genome for improved assembly.

### PacBio data
**Args:** `scallop-lr -i pb_alignments.bam -o transcripts.gtf --platform pacbio`
**Explanation:** `--platform pacbio` optimizes for PacBio sequencing data.

### Nanopore data
**Args:** `scallop-lr -i ont_alignments.bam -o transcripts.gtf --platform nanopore`
**Explanation:** `--platform nanopore` optimizes for Oxford Nanopore data.

### Minimum read length
**Args:** `scallop-lr -i alignments.bam -o transcripts.gtf -min-length 1000`
**Explanation:** `-min-length 1000` filters reads shorter than 1000 bp.

### Verbose logging
**Args:** `scallop-lr -i alignments.bam -o transcripts.gtf -v`
**Explanation:** `-v` enables verbose output for debugging.

### Output FASTA
**Args:** `scallop-lr -i alignments.bam -o transcripts.gtf --fasta transcripts.fasta`
**Explanation:** `--fasta` outputs transcript sequences in FASTA format.