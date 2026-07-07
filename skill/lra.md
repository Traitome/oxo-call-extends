---
name: lra
category: alignment
description: LRA - Long read aligner for sequences and contigs
tags: [lra, alignment, long-reads, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ChaissonLab/LRA"
---

## Concepts

- **Sequence Alignment**: Aligning sequences to reference genome
- **Long-read Data**: Handling long-read sequencing data
- **Contig Alignment**: Aligning contigs to reference
- **High Sensitivity**: High sensitivity alignment
- **Structural Variants**: Detection of structural variations
- **Genome Comparison**: Comparative genome analysis

## Pitfalls

- **Read Quality**: Poor quality reads affect alignment
- **Memory Usage**: Memory-intensive for large genomes
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Alignments**: May produce false alignments
- **Reference Genome**: Requires good quality reference genome

## Examples

### Align reads
**Args:** `lra align -i reads.fastq -r reference.fasta -o alignment.bam`
**Explanation:** Aligns long reads to reference genome.

### Index reference
**Args:** `lra index reference.fasta`
**Explanation:** Creates index for reference genome.

### Threads
**Args:** `lra align -i reads.fastq -r reference.fasta -o alignment.bam -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output SAM
**Args:** `lra align -i reads.fastq -r reference.fasta -o alignment.sam -f sam`
**Explanation:** Outputs in SAM format.

### Structural variants
**Args:** `lra align -i reads.fastq -r reference.fasta -o alignment.bam --sv`
**Explanation:** Enables structural variant detection.

### Verbose output
**Args:** `lra align -i reads.fastq -r reference.fasta -o alignment.bam -v`
**Explanation:** Provides detailed output.