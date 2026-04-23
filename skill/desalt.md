---
name: desalt
category: alignment
description: De Bruijn graph-based Spliced Aligner for Long Transcriptome reads.
tags: [desalt, alignment, long-read, transcriptome, rna]
author: oxo-call-community
source_url: "https://github.com/ydLiu-HIT/deSALT"
---

## Concepts

- **Tool Overview**: deSALT v1.5.6 - De Bruijn graph-based spliced aligner for long transcriptome reads (PacBio/Nanopore).
- **Core Function**: Aligns long RNA-seq reads to a reference genome using splice-aware de Bruijn graph approach.
- **Input/Output**: Expects FASTA/FASTQ long reads and reference genome; outputs SAM/BAM alignment.
- **Installation**: `conda install -c bioconda desalt`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires long reads (PacBio/Nanopore) for optimal performance.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deSALT aln --ref ref.fa --read reads.fq --out aligned.sam`
**Explanation:** Aligns long transcriptome reads to reference genome.
