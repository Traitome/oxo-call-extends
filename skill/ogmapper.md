---
name: ogmapper
category: alignment
description: OGMapper is a fast and lightweight genomic mapper for short sequencing reads.
tags: [ogmapper, alignment, short-reads, mapping]
author: oxo-call-community
source_url: "https://github.com/vtrevino/ogmapper"
---

## Concepts

- **Tool Overview**: OGMapper provides fast read mapping to reference genomes.
- **Core Function**: Aligns short sequencing reads to reference sequences.
- **Algorithm**: Uses seed-and-extend approach for efficient mapping.
- **Input Format**: Accepts FASTQ reads and FASTA reference sequences.
- **Output**: Produces SAM/BAM alignment files.
- **Use Case**: Read mapping, variant calling, and genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Length**: Optimized for short reads, may not handle long reads well.
- **Memory Usage**: Large references require memory.
- **Computational Cost**: Mapping can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Validation**: Results should be validated with other mappers.

## Examples

### Display help
**Args:** `ogmapper --help`
**Explanation:** Shows available options and usage instructions.

### Map reads
**Args:** `ogmapper -r reference.fasta -q reads.fastq -o alignments.sam`
**Explanation:** Maps reads to reference genome.

### Output BAM
**Args:** `ogmapper -r reference.fasta -q reads.fastq -o alignments.bam --bam`
**Explanation:** Outputs alignment in BAM format.

### Paired-end mapping
**Args:** `ogmapper -r reference.fasta -q reads_1.fastq -q2 reads_2.fastq -o alignments.sam`
**Explanation:** Maps paired-end reads.

### Threads
**Args:** `ogmapper -r reference.fasta -q reads.fastq -t 8 -o alignments.sam`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `ogmapper -r reference.fasta -q reads.fastq -q 30 -o alignments.sam`
**Explanation:** Filters by minimum quality score.

### Verbose mode
**Args:** `ogmapper -r reference.fasta -q reads.fastq -v -o alignments.sam`
**Explanation:** Runs with verbose output.

### Create index
**Args:** `ogmapper index -r reference.fasta -o index`
**Explanation:** Creates index for reference genome.