---
name: nanolyse
category: qc
description: Removing lambda DNA control reads from fastq dataset
tags: [nanolyse, qc, nanopore, lambda-dna, filtering]
author: oxo-call-community
source_url: "https://github.com/wdecoster/NanoLyse"
---

## Concepts

- **Tool Overview**: NanoLyse v1.2.1 - removes lambda DNA control reads from Nanopore datasets.
- **Core Function**: Filters out lambda phage control spike-in reads from Nanopore FASTQ files.
- **Input/Output**: Takes FASTQ (stdin); outputs filtered FASTQ (stdout) without lambda reads.
- **Installation**: `conda install -c bioconda nanolyse`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Reads from stdin; outputs to stdout.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Remove lambda reads
**Args:** `< input.fastq > filtered.fastq`
**Explanation:** Removes lambda DNA control reads from FASTQ stream.

### With reference
**Args:** `-r lambda.fasta < input.fastq > filtered.fastq`
**Explanation:** Removes lambda reads using specified reference.
