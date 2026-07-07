---
name: transdecoder
category: annotation
description: TransDecoder - Tool for identifying coding regions in transcript sequences.
tags: [transdecoder, coding-region, orf-prediction, transcriptome, annotation]
author: oxo-call-community
source_url: "https://github.com/TransDecoder/TransDecoder"
---

## Concepts

- **Tool Overview**: TransDecoder - A tool for predicting coding regions (ORFs) in transcript sequences.
- **Core Function**: Identifies likely protein-coding regions in RNA-seq assembled transcripts.
- **Input**: Transcript sequences (FASTA), optional protein homology evidence.
- **Output**: Predicted ORFs, peptide sequences, coding potential scores.
- **Installation**: `conda install -c bioconda transdecoder`
- **Use Case**: Transcriptome annotation, gene prediction, proteomics.

## Pitfalls

- **Short Transcripts**: May miss short ORFs or require minimum length threshold adjustment.
- **Non-coding RNAs**: May incorrectly predict ORFs in non-coding transcripts.

## Examples

### Predict ORFs
**Args:** `TransDecoder.LongOrfs -t transcripts.fasta`
**Explanation:** Identify long open reading frames in transcripts.

### Predict coding regions
**Args:** `TransDecoder.Predict -t transcripts.fasta`
**Explanation:** Predict coding regions with comprehensive analysis.
