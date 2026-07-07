---
name: ngs-smap
category: alignment
description: SMAP is a stack-based NGS read mapping tool for accurate alignment.
tags: [ngs-smap, alignment, mapping, stack-based]
author: oxo-call-community
source_url: "https://gitlab.com/truttink/smap"
---

## Concepts

- **Tool Overview**: SMAP provides stack-based mapping for next-generation sequencing reads.
- **Core Function**: Maps sequencing reads to reference genome with high accuracy.
- **Algorithm**: Uses stack-based approach for sensitive read mapping.
- **Input Format**: Accepts FASTQ reads and FASTA reference genome.
- **Output**: Produces SAM/BAM alignment files.
- **Use Case**: Read mapping, variant calling, and genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Genome**: Requires indexed reference genome.
- **Memory Usage**: Large genomes require memory.
- **Computational Cost**: Mapping can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Output Size**: Alignment files can be large.

## Examples

### Display help
**Args:** `smap --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `smap index -r reference.fasta -o index/`
**Explanation:** Builds index for reference genome.

### Map reads
**Args:** `smap map -i reads.fastq -r reference.fasta -o alignment.sam`
**Explanation:** Maps reads to reference genome.

### BAM output
**Args:** `smap map -i reads.fastq -r reference.fasta --bam -o alignment.bam`
**Explanation:** Outputs BAM format directly.

### Paired-end reads
**Args:** `smap map -i reads_1.fastq -i2 reads_2.fastq -r reference.fasta -o alignment.sam`
**Explanation:** Maps paired-end reads.

### Threads
**Args:** `smap map -i reads.fastq -r reference.fasta -t 8 -o alignment.sam`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `smap map -i reads.fastq -r reference.fasta -q 20 -o alignment.sam`
**Explanation:** Filters reads by quality score.