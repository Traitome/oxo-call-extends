---
name: bwa-mem2
category: alignment
description: Next version of BWA-MEM with improved speed and identical outputs
tags: [bwa-mem2, alignment, short-read, mapping, dna-seq]
author: oxo-call-community
source_url: "https://github.com/bwa-mem2/bwa-mem2"
---

## Concepts

- **Tool Overview**: BWA-MEM2 is the next generation of BWA-MEM with ~1.5-2x speedup and identical outputs.
- **Core Function**: Maps DNA sequences to reference genomes using an improved algorithm.
- **Compatibility**: Produces identical output to BWA-MEM for reproducibility.
- **Index Format**: Uses different index format from BWA; must rebuild indexes.
- **SSE Support**: Utilizes SSE4.2 instructions for faster alignment.
- **Installation**: Install via bioconda: `conda install -c bioconda bwa-mem2`

## Pitfalls

- **Index Incompatibility**: BWA-MEM2 indexes are NOT compatible with BWA indexes.
- **Rebuild Required**: Must rebuild indexes when switching from BWA to BWA-MEM2.
- **CPU Requirement**: Requires SSE4.2-capable CPU for full speedup.
- **Memory Usage**: Uses more memory than BWA-MEM during alignment.

## Examples

### Build genome index
**Args:** `bwa-mem2 index reference.fa`
**Explanation:** Creates BWA-MEM2 index files from reference genome.

### Align paired-end reads
**Args:** `bwa-mem2 mem -t 8 reference.fa R1.fq R2.fq > aligned.sam`
**Explanation:** Aligns paired-end reads using BWA-MEM2 with 8 threads.

### Align single-end reads
**Args:** `bwa-mem2 mem -t 8 reference.fa reads.fq > aligned.sam`
**Explanation:** Aligns single-end reads to the indexed reference genome.

### With read groups
**Args:** `bwa-mem2 mem -t 8 -R '@RG\tID:sample1\tSM:sample1' reference.fa R1.fq R2.fq | samtools sort -o aligned.bam`
**Explanation:** Aligns with read groups and pipes to sorted BAM.

### Output all alignments
**Args:** `bwa-mem2 mem -a -t 8 reference.fa reads.fq > aligned.sam`
**Explanation:** Outputs all alignments including secondary hits.

### Check version
**Args:** `bwa-mem2 version`
**Explanation:** Displays installed BWA-MEM2 version.
