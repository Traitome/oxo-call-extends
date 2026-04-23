---
name: bugseq-porechop
category: qc
description: Adapter removal and demultiplexing of Oxford Nanopore reads
tags: [porechop, nanopore, adapter-trimming, demultiplexing, qc]
author: oxo-call-community
source_url: "https://gitlab.com/bugseq/porechop"
---

## Concepts

- **Tool Overview**: bugseq-porechop removes adapters and demultiplexes Oxford Nanopore reads.
- **Core Function**: Trims adapter sequences and separates barcoded reads from Nanopore data.
- **Input**: FASTQ files from Nanopore sequencing.
- **Output**: Trimmed and optionally demultiplexed FASTQ files.
- **Fork**: Fork of artic-network/Porechop with bugseq improvements.
- **Installation**: Install via bioconda: `conda install -c bioconda bugseq-porechop`

## Pitfalls

- **Nanopore Specific**: Designed for Nanopore data; not for Illumina.
- **Adapter Detection**: Automatic adapter detection may miss custom adapters.
- **Barcodes**: Demultiplexing depends on barcode quality and length.
- **Output Size**: Trimmed files may be significantly smaller.

## Examples

### Trim adapters
**Args:** `porechop -i reads.fq -o trimmed.fq`
**Explanation:** Removes adapter sequences from Nanopore reads.

### Demultiplex barcoded reads
**Args:** `porechop -i reads.fq --demultiplex -o demux_output/`
**Explanation:** Separates reads by barcode into individual files.

### Custom adapter sequence
**Args:** `porechop -i reads.fq --adapter_threshold 80 -o trimmed.fq`
**Explanation:** Uses 80% identity threshold for adapter detection.

### Verbose output
**Args:** `porechop -i reads.fq -o trimmed.fq -v 2`
**Explanation:** Verbose output showing adapter detection details.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
