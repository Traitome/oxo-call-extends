---
name: bwa-aln-interactive
category: alignment
description: Interactive version of BWA aln read mapper for real-time alignment
tags: [bwa, alignment, interactive, real-time]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/bwa-aln-interactive"
---

## Concepts

- **Tool Overview**: bwa-aln-interactive is a modified BWA aln for interactive/real-time alignment.
- **Core Function**: Aligns reads in real-time as they arrive, useful for streaming applications.
- **Input**: Streaming FASTQ reads and pre-built BWA index.
- **Output**: SAM format alignments.
- **Application**: Real-time sequencing analysis and streaming pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda bwa-aln-interactive`

## Pitfalls

- **Interactive Mode**: Designed for streaming input; not for batch processing.
- **Index Required**: Must build BWA index before starting interactive session.
- **Latency**: Alignment latency depends on read length and index size.

## Examples

### Start interactive alignment
**Args:** `bwa-aln-interactive reference.fa`
**Explanation:** Starts interactive alignment session against indexed reference.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
