---
name: desalt
category: alignment
description: deSALT - De Bruijn graph-based spliced aligner for long transcriptome reads.
tags: [desalt, alignment, long-read, transcriptome, rna]
author: oxo-call-community
source_url: "https://github.com/ydLiu-HIT/deSALT"
---

## Concepts

- **Tool Overview**: desalt (v1.5.6+) is a De Bruijn graph-based spliced aligner specifically designed for long transcriptome reads from PacBio or Oxford Nanopore sequencing.
- **Core Function**: Aligns long RNA-seq reads to a reference genome using a splice-aware De Bruijn graph approach, handling long reads and complex splicing patterns.
- **Input/Output**: Input: FASTA/FASTQ long reads, reference genome. Output: SAM/BAM alignment files, splicing junctions.
- **Algorithm**: Constructs De Bruijn graphs from reads and reference to identify splice junctions and perform accurate alignment.
- **Key Features**: Long-read alignment, splice-aware, De Bruijn graph-based, handles complex transcripts, supports PacBio/Nanopore data.
- **Installation**: `conda install -c bioconda desalt`

## Pitfalls

- **Input Requirements**: Optimized for long reads (PacBio/Nanopore), may not perform well on short reads.
- **Memory Usage**: May require significant memory for large genomes.
- **Index Building**: Requires time to build genome index.
- **Computational Time**: May be slow for very large datasets.
- **Reference Genome**: Must use appropriate reference genome with annotation.

## Examples

### Align long transcriptome reads
**Args:** `deSALT aln --ref ref.fa --read reads.fq --out aligned.sam`
**Explanation:** Aligns long transcriptome reads to reference genome.

### With annotation-guided alignment
**Args:** `deSALT aln --ref ref.fa --read reads.fq --out aligned.sam --gtf annotation.gtf`
**Explanation:** Use gene annotation to guide splice junction detection.

### Direct RNA-seq mode
**Args:** `deSALT aln --ref ref.fa --read reads.fq --out aligned.sam --direct-rna`
**Explanation:** Optimize for direct RNA sequencing data.