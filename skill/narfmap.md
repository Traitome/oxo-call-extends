---
name: narfmap
category: alignment
description: NARFMAP is a fork of the Dragen mapper/aligner optimized for high-performance read mapping.
tags: [narfmap, alignment, dragen, mapping, long-reads]
author: oxo-call-community
source_url: "https://github.com/bioinformaticsorphanage/NARFMAP"
---

## Concepts

- **Tool Overview**: NARFMAP v1.4.2 is a high-performance read mapper and aligner, forked from the Illumina Dragen aligner.
- **Core Function**: Aligns sequencing reads to reference genomes with high speed and accuracy.
- **Algorithm**: Implements seed-and-extend mapping with advanced heuristics for optimal performance.
- **Input Format**: Accepts FASTQ reads (paired-end or single-end) and FASTA reference sequences.
- **Output**: Produces sorted and indexed BAM files with alignment information.
- **Use Case**: High-throughput read mapping for whole-genome sequencing, exome sequencing, and targeted sequencing.

## Pitfalls

- **Reference Requirements**: Requires indexed reference genome in FASTA format.
- **Memory Usage**: Can require significant memory for large genomes.
- **Version Compatibility**: Options may vary between different versions.
- **Input Format**: Requires properly formatted FASTQ files.
- **Output Size**: BAM files can be very large and require sufficient storage.
- **Indexing**: Output BAM needs separate indexing step for downstream analysis.

## Examples

### Display help
**Args:** `narfmap --help`
**Explanation:** Shows available options and usage instructions.

### Basic alignment
**Args:** `narfmap -r reference.fasta -1 reads_R1.fastq -2 reads_R2.fastq -o aligned.bam`
**Explanation:** Aligns paired-end reads to reference genome.

### Single-end alignment
**Args:** `narfmap -r reference.fasta -1 reads.fastq -o aligned.bam`
**Explanation:** Aligns single-end reads to reference genome.

### Gzipped input
**Args:** `narfmap -r ref.fasta -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -o aligned.bam`
**Explanation:** Processes gzipped FASTQ files directly.

### Threads
**Args:** `narfmap -r ref.fasta -1 R1.fastq -2 R2.fastq -t 16 -o aligned.bam`
**Explanation:** Uses 16 threads for parallel alignment.

### Output SAM format
**Args:** `narfmap -r ref.fasta -1 R1.fastq -2 R2.fastq --sam -o aligned.sam`
**Explanation:** Outputs alignment in SAM format instead of BAM.