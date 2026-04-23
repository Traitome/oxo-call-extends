---
name: splicemap
category: alignment
description: Detects splice junctions from RNA-seq data. This method does not depend on any existing annotation of gene structures and is capable of finding novel splice junctions with high sensitivity and specificity. It can handle long reads (50–100 nt) and can exploit paired-read information to improve mapping accuracy.
tags: [splicemap, alignment]
author: oxo-call-community
source_url: "https://web.stanford.edu/group/wonglab/SpliceMap"
---

## Concepts

- **Tool Overview**: splicemap (v3.3.5.2) - Detects splice junctions from RNA-seq data. This method does not depend on any existing annotation of gene structures and is capable of finding novel splice junctions with high sensitivity and specificity. It can handle long reads (50–100 nt) and can exploit paired-read information to improve mapping accuracy.
- **Core Function**: Detects splice junctions from RNA-seq data. This method does not depend on any existing annotation of gene structures and is capable of finding novel splice junctions with high sensitivity and specificity. It can handle long reads (50–100 nt) and can exploit paired-read information to improve mapping accuracy.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda splicemap`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `splicemap -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run splicemap with typical input and output options.
