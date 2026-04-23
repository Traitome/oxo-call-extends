---
name: music
category: epigenomics
description: MUltiScale enrIchment Calling for ChIP-Seq Datasets
tags: [music, epigenomics, chip-seq, enrichment, peak-calling]
author: oxo-call-community
source_url: "http://music.gersteinlab.org"
---

## Concepts

- **Tool Overview**: MUSIC (MUltiScale enrIchment Calling) v1.0.0 - a tool for multi-scale enrichment calling in ChIP-Seq datasets.
- **Core Function**: Identifies enriched regions in ChIP-Seq data across multiple scales, enabling detection of both narrow and broad peaks.
- **Input/Output**: Takes aligned BAM files from ChIP-Seq experiments; outputs enriched regions in BED or similar format.
- **Installation**: `conda install -c bioconda music`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure input BAM files are sorted and indexed.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `-i input.bam -o output.bed`
**Explanation:** Runs MUSIC on an input BAM file and writes enriched regions to output BED file.
