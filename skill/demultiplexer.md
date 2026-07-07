---
name: demultiplexer
category: utility
description: demultiplexer - Python tool for demultiplexing Illumina reads with LeeseLab tagging scheme.
tags: [demultiplexer, utility, demultiplexing, illumina]
author: oxo-call-community
source_url: "https://github.com/DominikBuchner/demultiplexer"
---

## Concepts

- **Tool Overview**: demultiplexer (v1.2.1+) is a Python tool for demultiplexing Illumina reads using the LeeseLab tagging scheme. It handles the specific barcode structure used in LeeseLab protocols.
- **Core Function**: Separates multiplexed Illumina reads based on the LeeseLab tagging barcodes, enabling processing of multiple samples in a single sequencing run.
- **Input/Output**: Input: FASTQ files (paired-end), optional barcode file. Output: Demultiplexed FASTQ files per sample.
- **Algorithm**: Uses pattern matching to identify and extract barcodes according to the LeeseLab tagging scheme.
- **Key Features**: LeeseLab tagging scheme support, paired-end processing, quality trimming, batch processing, statistics generation.
- **Installation**: `conda install -c bioconda demultiplexer`

## Pitfalls

- **Input Requirements**: Requires Illumina FASTQ files with LeeseLab tagging scheme.
- **Tagging Scheme**: Only works with specific tagging scheme.
- **Read Quality**: Poor quality reads may affect barcode identification.
- **Barcode Design**: Results depend on barcode design and diversity.
- **Read Pair Consistency**: Requires matching barcodes for paired-end reads.

## Examples

### Demultiplex paired-end reads
**Args:** `demultiplexer --input R1.fq R2.fq --output output_dir/`
**Explanation:** Demultiplexes paired-end Illumina reads using LeeseLab scheme.

### With custom barcodes
**Args:** `demultiplexer --input R1.fq R2.fq --barcodes barcodes.txt --output output_dir/`
**Explanation:** Use custom barcode file for demultiplexing.

### With quality filtering
**Args:** `demultiplexer --input R1.fq R2.fq --output output_dir/ --quality 20`
**Explanation:** Apply quality filtering with Phred score threshold.