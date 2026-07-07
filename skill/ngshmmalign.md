---
name: ngshmmalign
category: alignment
description: ngshmmalign is a profile HMM aligner optimized for small genomes and NGS reads.
tags: [ngshmmalign, alignment, hmm, small-genomes]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/ngshmmalign"
---

## Concepts

- **Tool Overview**: ngshmmalign aligns NGS reads using profile Hidden Markov Models.
- **Core Function**: Maps reads to reference sequences with HMM-based alignment.
- **Algorithm**: Uses profile HMM for sensitive alignment.
- **Input Format**: Accepts FASTQ reads and FASTA reference.
- **Output**: Produces SAM/BAM alignment files.
- **Use Case**: Viral genome analysis, small genome alignment, and sensitive mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Size**: Optimized for small genomes.
- **Memory Usage**: Large references may require memory.
- **Computational Cost**: HMM alignment can be slow.
- **Index Building**: Requires HMM profile generation.
- **Accuracy vs Speed**: Trade-off between sensitivity and speed.

## Examples

### Display help
**Args:** `ngshmmalign --help`
**Explanation:** Shows available options and usage instructions.

### Build profile
**Args:** `ngshmmalign build -r reference.fasta -o profile.hmm`
**Explanation:** Builds HMM profile from reference.

### Align reads
**Args:** `ngshmmalign align -p profile.hmm -q reads.fastq -o alignment.sam`
**Explanation:** Aligns reads using HMM profile.

### BAM output
**Args:** `ngshmmalign align -p profile.hmm -q reads.fastq --bam -o alignment.bam`
**Explanation:** Outputs BAM format directly.

### Paired-end reads
**Args:** `ngshmmalign align -p profile.hmm -q1 reads_1.fastq -q2 reads_2.fastq -o alignment.sam`
**Explanation:** Aligns paired-end reads.

### Threads
**Args:** `ngshmmalign align -p profile.hmm -q reads.fastq -t 8 -o alignment.sam`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `ngshmmalign align -p profile.hmm -q reads.fastq -v -o alignment.sam`
**Explanation:** Runs with verbose output.