---
name: dragmap
category: alignment
description: DRAGMAP - High-performance DNA sequence aligner optimized for Illumina data.
tags: [dragmap, alignment, dna-sequencing, illumina, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Illumina/DRAGMAP"
---

## Concepts

- **Tool Overview**: DRAGMAP is Illumina's open-source DNA sequence mapper/aligner optimized for speed and accuracy.
- **Core Function**: Aligns sequencing reads to a reference genome using advanced mapping algorithms.
- **Input/Output**: Input: FASTQ reads, FASTA reference genome. Output: BAM alignment file.
- **Algorithm**: Uses a seed-and-extend approach with optimized indexing for rapid read mapping.
- **Key Features**: Ultra-fast alignment, support for paired-end reads, gapped alignment, variant calling integration.
- **Installation**: `conda install -c bioconda dragmap`

## Pitfalls

- **Memory Requirements**: Indexing large genomes requires significant memory resources.
- **Reference Format**: Reference genome must be in FASTA format and properly indexed.
- **Read Length**: Performance optimizations are tailored for typical Illumina read lengths.
- **Paired-End Data**: Requires proper pairing information for accurate fragment alignment.
- **Quality Scores**: Low-quality reads may produce unreliable alignments.
- **Output Size**: BAM files can be very large; consider compression options.

## Examples

### Build genome index
**Args:** `dragmap index --reference ref.fa --output ref.index`
**Explanation:** Creates an index for the reference genome to enable fast alignment.

### Align single-end reads
**Args:** `dragmap align --index ref.index --reads reads.fq --output aligned.bam`
**Explanation:** Aligns single-end sequencing reads to the indexed reference genome.

### Align paired-end reads
**Args:** `dragmap align --index ref.index --reads R1.fq R2.fq --output aligned.bam --paired`
**Explanation:** Aligns paired-end sequencing reads with proper fragment handling.

### With quality filtering
**Args:** `dragmap align --index ref.index --reads reads.fq --output aligned.bam --min-quality 20`
**Explanation:** Filters out low-quality reads before alignment to improve accuracy.

### Output SAM format
**Args:** `dragmap align --index ref.index --reads reads.fq --output aligned.sam --sam`
**Explanation:** Outputs alignments in SAM format instead of BAM.

### Enable variant calling mode
**Args:** `dragmap align --index ref.index --reads reads.fq --output aligned.bam --enable-variant-calling`
**Explanation:** Optimizes alignment for downstream variant calling analysis.