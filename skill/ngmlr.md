---
name: ngmlr
category: alignment
description: NGMLR is a long-read mapper optimized for PacBio and Oxford Nanopore reads.
tags: [ngmlr, alignment, long-reads, pacbio, nanopore]
author: oxo-call-community
source_url: "https://github.com/philres/ngmlr"
---

## Concepts

- **Tool Overview**: NGMLR aligns long sequencing reads to reference genomes.
- **Core Function**: Maps PacBio and Nanopore reads with structural variation detection.
- **Algorithm**: Uses seeded alignment with chaining for long reads.
- **Input Format**: Accepts FASTQ/FASTA reads and FASTA reference genome.
- **Output**: Produces SAM/BAM alignment files.
- **Use Case**: Structural variant calling, genome assembly validation, and long-read analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require significant memory.
- **Computational Cost**: Alignment can be slow for large datasets.
- **Read Quality**: Poor quality reads affect mapping accuracy.
- **Index Building**: Requires indexed reference genome.
- **Output Size**: SAM/BAM files can be large.

## Examples

### Display help
**Args:** `ngmlr --help`
**Explanation:** Shows available options and usage instructions.

### Map reads
**Args:** `ngmlr -r reference.fasta -q reads.fastq -o alignment.sam`
**Explanation:** Maps reads to reference genome.

### BAM output
**Args:** `ngmlr -r reference.fasta -q reads.fastq --bam -o alignment.bam`
**Explanation:** Outputs BAM format directly.

### PacBio mode
**Args:** `ngmlr -r reference.fasta -q reads.fastq -p pacbio -o alignment.sam`
**Explanation:** Optimized for PacBio reads.

### Nanopore mode
**Args:** `ngmlr -r reference.fasta -q reads.fastq -p ont -o alignment.sam`
**Explanation:** Optimized for Oxford Nanopore reads.

### Threads
**Args:** `ngmlr -r reference.fasta -q reads.fastq -t 8 -o alignment.sam`
**Explanation:** Uses 8 threads for parallel processing.

### Output SV candidates
**Args:** `ngmlr -r reference.fasta -q reads.fastq --sv -o alignment.sam`
**Explanation:** Outputs structural variant candidates.