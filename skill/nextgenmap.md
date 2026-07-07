---
name: nextgenmap
category: alignment
description: NextGenMap is a flexible, highly sensitive short read mapping tool optimized for high mismatch rates.
tags: [nextgenmap, alignment, short-reads, mapping, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Cibiv/NextGenMap"
---

## Concepts

- **Tool Overview**: NextGenMap is a fast and sensitive short read aligner for DNA sequencing data.
- **Core Function**: Maps short reads to reference genomes with high mismatch tolerance.
- **Algorithm**: Uses seed-and-extend approach with optimized indexing for speed.
- **Input Format**: Accepts FASTQ files and FASTA reference genome.
- **Output**: Produces SAM/BAM alignment files.
- **Use Case**: RNA-seq, ChIP-seq, and whole-genome sequencing alignment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Index Building**: Requires indexed reference genome.
- **Memory Usage**: Large genomes require memory.
- **Mapping Quality**: High mismatch rates may affect mapping quality.
- **Output Size**: SAM/BAM files can be large.
- **Paired-End Data**: Requires proper handling of paired reads.

## Examples

### Display help
**Args:** `nextgenmap --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `nextgenmap build -r reference.fasta -o index/`
**Explanation:** Builds index for reference genome.

### Map reads
**Args:** `nextgenmap map -r reference.fasta -q reads.fastq -o alignment.sam`
**Explanation:** Maps reads to reference genome.

### Paired-end mapping
**Args:** `nextgenmap map -r reference.fasta -q1 reads_1.fastq -q2 reads_2.fastq -o alignment.sam`
**Explanation:** Maps paired-end reads.

### BAM output
**Args:** `nextgenmap map -r reference.fasta -q reads.fastq --bam -o alignment.bam`
**Explanation:** Outputs BAM format directly.

### Quality filtering
**Args:** `nextgenmap map -r reference.fasta -q reads.fastq -q 30 -o alignment.sam`
**Explanation:** Filters reads by quality score.

### Threads
**Args:** `nextgenmap map -r reference.fasta -q reads.fastq -t 8 -o alignment.sam`
**Explanation:** Uses 8 threads for parallel processing.