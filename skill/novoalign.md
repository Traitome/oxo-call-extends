---
name: novoalign
category: alignment
description: NovoAlign is a powerful short read aligner for mapping reads to reference genomes from Illumina, Ion Torrent, and 454 platforms.
tags: [novoalign, alignment, short-read, mapping]
author: oxo-call-community
source_url: "http://www.novocraft.com/products/novoalign/"
---

## Concepts

- **Tool Overview**: NovoAlign maps short sequencing reads to reference genomes with high accuracy.
- **Core Function**: Aligns reads using optimized seed-and-extend algorithm.
- **Algorithm**: Implements efficient read mapping with support for multiple platforms.
- **Input Format**: Accepts FASTQ reads and FASTA reference genome.
- **Output**: Produces SAM/BAM alignment files.
- **Use Case**: Read mapping, variant calling, and genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **License**: Commercial license required for full functionality.
- **Memory Usage**: Large genomes require memory.
- **Index Building**: Requires pre-built index.
- **Platform Specific**: Optimized for specific sequencing platforms.
- **Performance**: Slower than some other aligners.

## Examples

### Display help
**Args:** `novoalign --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `novoindex reference.ndx reference.fasta`
**Explanation:** Builds index for reference genome.

### Align reads
**Args:** `novoalign -d reference.ndx -f reads.fastq -o SAM > alignment.sam`
**Explanation:** Aligns reads to reference genome.

### Paired-end alignment
**Args:** `novoalign -d reference.ndx -f reads_1.fastq reads_2.fastq -o SAM > alignment.sam`
**Explanation:** Aligns paired-end reads.

### Output BAM
**Args:** `novoalign -d reference.ndx -f reads.fastq -o BAM > alignment.bam`
**Explanation:** Outputs BAM format directly.

### Threads
**Args:** `novoalign -d reference.ndx -f reads.fastq -o SAM -c 8 > alignment.sam`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `novoalign -d reference.ndx -f reads.fastq -q 30 -o SAM > alignment.sam`
**Explanation:** Filters by minimum quality score.

### Verbose mode
**Args:** `novoalign -d reference.ndx -f reads.fastq -o SAM -v > alignment.sam`
**Explanation:** Runs with verbose output.