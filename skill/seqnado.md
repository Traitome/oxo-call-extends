---
name: seqnado
category: epigenomics
description: A unified and user-friendly collection of pipelines for: ATAC-seq, ChIP-seq, CUT&RUN/TAG, RNA-seq, WGS, Methylation (Bisulphite/TAPS), CRISPR screens and Micro-Capture-C.
tags: [seqnado, epigenomics]
author: oxo-call-community
source_url: "https://github.com/Milne-Group/SeqNado"
---

## Concepts

- **Tool Overview**: seqnado (v1.0.5) - A unified and user-friendly collection of pipelines for: ATAC-seq, ChIP-seq, CUT&RUN/TAG, RNA-seq, WGS, Methylation (Bisulphite/TAPS), CRISPR screens and Micro-Capture-C.
- **Core Function**: A unified and user-friendly collection of pipelines for: ATAC-seq, ChIP-seq, CUT&RUN/TAG, RNA-seq, WGS, Methylation (Bisulphite/TAPS), CRISPR screens and Micro-Capture-C.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqnado`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqnado -i <input.bam> -o <output_dir>`
**Explanation:** Run seqnado with typical input and output options.
