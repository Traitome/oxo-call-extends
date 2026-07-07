---
name: gem2
category: alignment
description: High-performance sequence mapping tool with unique mappability evaluation capabilities.
tags: [gem2, sequence-alignment, mappability, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gemtools/gem2"
---

## Concepts
- **Read Mapping**: High-performance short read alignment to reference genomes.
- **Mappability Evaluation**: Unique tool for assessing read mappability across the genome.
- **Multi-threading**: Supports parallel processing for faster alignment.
- **Multiple Formats**: Supports FASTA, FASTQ, SAM, and BAM formats.
- **Splice-aware Mapping**: Supports RNA-seq read mapping with splice junctions.

## Pitfalls
- **Index Size**: Genome indexes can be large and require significant storage.
- **Memory Usage**: Mapping large datasets requires substantial memory.
- **Parameter Sensitivity**: Mapping parameters affect alignment results.
- **Index Building**: Index creation can be time-consuming for large genomes.
- **Output Format**: SAM/BAM output files can be very large.

## Examples
### Build genome index
**Args:** `gem-indexer -i genome.fasta -o genome.gem`
**Explanation:** Builds a GEM index for the reference genome.

### Map reads
**Args:** `gem-mapper -I genome.gem -i reads.fastq -o alignments.sam`
**Explanation:** Maps reads to the reference genome using the GEM index.

### Evaluate mappability
**Args:** `gem-mappability -I genome.gem -l 100 -o mappability.bw`
**Explanation:** Computes mappability for 100bp reads across the genome.

### RNA-seq mapping
**Args:** `gem-mapper -I genome.gem -i rna_reads.fastq -o rna_alignments.sam --rna`
**Explanation:** Performs splice-aware mapping for RNA-seq reads.

### Parallel mapping
**Args:** `gem-mapper -I genome.gem -i reads.fastq -o alignments.sam -p 16`
**Explanation:** Maps reads using 16 parallel threads.