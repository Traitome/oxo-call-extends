---
name: nanonet
category: utility
description: Nanonet provides recurrent neural network basecalling for Oxford Nanopore MinION data.
tags: [nanonet, utility, nanopore, basecalling, rnn]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/nanonet"
---

## Concepts

- **Tool Overview**: NanoNet v2.0.0 - RNN basecalling for Oxford Nanopore MinION data.
- **Core Function**: Basecalls Nanopore signal using recurrent neural network models.
- **Input/Output**: Takes FAST5 files; outputs FASTQ basecalled reads.
- **Installation**: `conda install -c bioconda nanonet`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FAST5 files from MinION runs.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i fast5_dir -o output.fastq`
**Explanation:** Basecalls FAST5 files using RNN model.
