---
name: macs2
category: epigenomics
description: Model Based Analysis for ChIP-Seq data.
tags: [macs2, epigenomics]
author: oxo-call-community
source_url: "https://github.com/macs3-project/MACS"
---

## Concepts

- **Tool Overview**: macs2 v2.2.9.1 - Model Based Analysis for ChIP-Seq data..
- **Core Function**: Model Based Analysis for ChIP-Seq data.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda macs2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Call peaks
**Args:** `macs2 callpeak -t treatment.bam -c control.bam -f BAM -g hs -n output`
**Explanation:** Calls peaks from ChIP-seq data with control.

