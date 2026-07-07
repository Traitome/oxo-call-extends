---
name: scallop-umi
category: expression
description: Scallop-UMI - reference-based transcript assembler for linked-reads RNA-seq
tags: ["scallop-umi", "expression", "RNA-seq", "UMI", "linked-reads"]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/scallop-umi"
---

## Concepts

- **Tool Overview**: Scallop-UMI (v1.1.0) is a reference-based transcript assembler specifically designed for linked-reads RNA-seq data with Unique Molecular Identifiers (UMIs).
- **Core Function**: Assembles transcripts from RNA-seq reads while leveraging UMI information to improve accuracy.
- **Algorithm**: Combines graph-based assembly with UMI deduplication for more accurate transcript reconstruction.
- **Input/Output**: Accepts BAM files with UMI-tagged reads and produces transcript GTF annotations.
- **UMI Support**: Handles Unique Molecular Identifiers for error correction and duplicate removal.
- **Applications**: Transcriptome assembly with improved accuracy using linked-read technology.

## Pitfalls

- **UMI Requirement**: Requires UMI-tagged reads for full functionality.
- **Reference Dependence**: Requires high-quality reference genome.
- **Alignment Quality**: Results depend on proper read alignment.
- **Computational Resources**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment of assembly parameters.
- **Complex Transcripts**: May struggle with highly complex gene loci.

## Examples

### Basic assembly with UMI
**Args:** `scallop-umi -i alignments.bam -o transcripts.gtf`
**Explanation:** `-i` input BAM with UMI-tagged reads; `-o` output GTF.

### Specify UMI tag
**Args:** `scallop-umi -i alignments.bam -o transcripts.gtf --umi-tag UB`
**Explanation:** `--umi-tag UB` specifies UMI tag in BAM file.

### With reference genome
**Args:** `scallop-umi -i alignments.bam -r reference.fasta -o transcripts.gtf`
**Explanation:** `-r` reference genome for improved assembly.

### Strand-specific data
**Args:** `scallop-umi -i alignments.bam -o transcripts.gtf -s`
**Explanation:** `-s` enables strand-specific assembly.

### Minimum UMI count
**Args:** `scallop-umi -i alignments.bam -o transcripts.gtf -min-umi 2`
**Explanation:** `-min-umi 2` requires minimum 2 UMIs per transcript.

### Verbose logging
**Args:** `scallop-umi -i alignments.bam -o transcripts.gtf -v`
**Explanation:** `-v` enables verbose output for debugging.

### Output FASTA
**Args:** `scallop-umi -i alignments.bam -o transcripts.gtf --fasta transcripts.fasta`
**Explanation:** `--fasta` outputs transcript sequences.