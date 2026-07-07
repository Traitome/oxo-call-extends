---
name: mrsfast
category: alignment
description: mrsFAST - micro-read substitution-only Fast Alignment Search Tool.
tags: [mrsfast, alignment, sequencing]
author: oxo-call-community
source_url: "https://github.com/sfu-compbio/mrsfast"
---

## Concepts

- **Tool Overview**: mrsFAST v3.4.2 is a fast read alignment tool for short sequencing reads.
- **Core Function**: Aligns micro-reads to reference genome with substitution support.
- **Fast Alignment**: Optimized for speed with substitution-only mapping.
- **Short Reads**: Specialized for short sequencing read alignment.
- **Index-based**: Uses index for rapid search.
- **Input/Output**: Accepts FASTQ reads; outputs SAM/BAM alignments.

## Pitfalls

- **Short Reads Only**: Designed for short sequencing reads.
- **Memory Requirements**: Index building requires significant memory.
- **Parameter Tuning**: May require parameter adjustment for mapping.
- **Data Quality**: Results depend on read quality.
- **Substitution Only**: Does not support indels by default.
- **Index Size**: Reference index can be large.

## Examples

### Align reads to reference
**Args:** `mrsfast --search reference.fasta --seq reads.fastq --out alignments.sam`
**Explanation:** Aligns reads to reference genome.

### Build index
**Args:** `mrsfast --index reference.fasta`
**Explanation:** Builds index for reference genome.

### With maximum mismatches
**Args:** `mrsfast --search reference.fasta --seq reads.fastq -m 2 --out alignments.sam`
**Explanation:** Allows up to 2 mismatches.

### Paired-end alignment
**Args:** `mrsfast --search reference.fasta --seq reads_1.fastq --seq2 reads_2.fastq --out alignments.sam`
**Explanation:** Aligns paired-end reads.

### Output in BAM format
**Args:** `mrsfast --search reference.fasta --seq reads.fastq --out alignments.bam`
**Explanation:** Outputs alignments in BAM format.