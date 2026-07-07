---
name: scallop2
category: expression
description: Scallop2 - reference-based transcript assembler optimized for paired-end RNA-seq
tags: ["scallop2", "expression", "RNA-seq", "transcript-assembly"]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/scallop2"
---

## Concepts

- **Tool Overview**: Scallop2 (v1.1.2) is a reference-based transcript assembler optimized for paired-/multiple-end RNA-seq data.
- **Core Function**: Assembles transcripts from RNA-seq reads aligned to a reference genome.
- **Algorithm**: Uses graph-based assembly approach to reconstruct full-length transcripts.
- **Input/Output**: Accepts BAM alignment files and reference genome, produces transcript annotations in GTF format.
- **Paired-End Support**: Specifically optimized for paired-end sequencing data.
- **Applications**: Transcriptome assembly, alternative splicing analysis, and gene expression quantification.

## Pitfalls

- **Reference Dependence**: Requires high-quality reference genome.
- **Alignment Quality**: Results depend on alignment accuracy.
- **Computational Resources**: High memory and CPU requirements for large datasets.
- **Complex Transcripts**: May struggle with highly complex transcript structures.
- **Parameter Tuning**: Requires careful adjustment of assembly parameters.
- **Output Size**: May produce large output files with many isoforms.

## Examples

### Basic transcript assembly
**Args:** `scallop2 -i alignments.bam -o transcripts.gtf`
**Explanation:** `-i` input BAM file; `-o` output GTF with assembled transcripts.

### With reference genome
**Args:** `scallop2 -i alignments.bam -r reference.fasta -o transcripts.gtf`
**Explanation:** `-r` reference genome for improved assembly.

### Strand-specific data
**Args:** `scallop2 -i alignments.bam -o transcripts.gtf --strand-specific`
**Explanation:** `--strand-specific` enables strand-specific assembly.

### Minimum intron length
**Args:** `scallop2 -i alignments.bam -o transcripts.gtf -min-intron 50`
**Explanation:** `-min-intron 50` sets minimum intron length to 50 bp.

### Maximum intron length
**Args:** `scallop2 -i alignments.bam -o transcripts.gtf -max-intron 500000`
**Explanation:** `-max-intron 500000` sets maximum intron length to 500kb.

### Verbose logging
**Args:** `scallop2 -i alignments.bam -o transcripts.gtf -v`
**Explanation:** `-v` enables verbose output for debugging.

### Output FASTA
**Args:** `scallop2 -i alignments.bam -o transcripts.gtf --fasta transcripts.fasta`
**Explanation:** `--fasta` outputs transcript sequences in FASTA format.