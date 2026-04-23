---
name: architeuthis
category: annotation
description: Tool to analyze and summarize data for Kraken.
tags: [architeuthis, annotation, SAM]
author: oxo-call-community
source_url: "https://github.com/cdiener/architeuthis"
---

## Concepts

- **Tool Overview**: architeuthis (v0.5.0) - Tool to analyze and summarize data for Kraken.
- **Core Function**: architeuthis is a fast standalone command to supplement the Kraken suite of software tools such like Kraken2, KrakenUniq, and Bracken. I saw myself repeatedly rewriting the same code in my pipelines w...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda architeuthis`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o annotation.gff`
**Explanation:** Annotate genomic features
