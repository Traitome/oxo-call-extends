---
name: csi-ssu
category: expression
description: CSI SSU screening tool for genomic and transcriptomic data
tags: [csi-ssu, expression]
author: oxo-call-community
source_url: "https://github.com/AlexTiceLab/CSI-SSU/blob/main/README.md"
---

## Concepts

- **Tool Overview**: csi-ssu (v1.0.3) - CSI SSU screening tool for genomic and transcriptomic data
- **Core Function**: A command-line tool for screening SSU (Small Subunit ribosomal RNA) sequences in genomic and transcriptomic data. This tool helps identify and classify SSU sequences using phylogenetic placement in SS...
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda csi-ssu`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
