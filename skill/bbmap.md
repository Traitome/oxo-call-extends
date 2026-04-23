---
name: bbmap
category: alignment
description: BBMap - Short read aligner and comprehensive bioinformatic toolsuite
tags: [alignment, short-reads, variant-calling, quality-control, toolsuite]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/bbmap"
---

## Concepts

- **Tool Overview**: BBMap is a short read aligner plus a comprehensive suite of bioinformatics tools including BBTools (quality trimming, adapter removal, error correction, etc.).

- **Alignment**: High-performance short read aligner supporting both DNA and RNA-seq data.

- **BBTools Suite**: Includes numerous utilities: BBDuk (quality filtering), BBMerge (read merging), BBNorm (coverage normalization), Reformat (format conversion), etc.

- **Memory Efficiency**: Designed for memory-efficient processing of large datasets.

- **Variant Calling**: Includes variant calling capabilities with sensitive SNP/indel detection.

## Pitfalls

- **Java Requirement**: Requires Java runtime. Ensure adequate Java heap memory with -Xmx flag.

- **Memory Settings**: Default memory may be insufficient for large genomes. Adjust -Xmx parameter.

- **Index Size**: Reference indexing creates large files. Ensure sufficient disk space.

## Examples

### Basic alignment
**Args:** `bbmap.sh ref=reference.fasta in=reads.fastq out=aligned.sam`
**Explanation:** Aligns reads to reference genome, outputs SAM format.

### Align with quality filtering
**Args:** `bbmap.sh ref=reference.fasta in=reads.fastq out=aligned.sam qtrim=rl trimq=20 minlen=50`
**Explanation:** Aligns reads with quality trimming (Q20) and minimum length filtering.

### BBDuk adapter trimming
**Args:** `bbduk.sh in=reads.fastq out=trimmed.fastq ref=adapters.fa ktrim=r k=23 hdist=1`
**Explanation:** Removes adapter sequences from reads using BBDuk tool.

### BBMerge read merging
**Args:** `bbmerge.sh in1=R1.fastq in2=R2.fastq out=merged.fastq out1=unmerged_R1.fastq out2=unmerged_R2.fastq`
**Explanation:** Merges overlapping paired-end reads.

### BBNorm coverage normalization
**Args:** `bbnorm.sh in=reads.fastq out=normalized.fastq target=100`
**Explanation:** Normalizes read coverage to target depth (100x).

### Variant calling
**Args:** `callvariants.sh ref=reference.fasta in=aligned.sam out=variants.vcf`
**Explanation:** Calls variants from aligned reads.
