---
name: mosdepth
category: qc
description: Fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing.
tags: [mosdepth, qc, alignment]
author: oxo-call-community
source_url: "https://github.com/brentp/mosdepth"
---

## Concepts

- **Tool Overview**: mosdepth v0.3.13 - Fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing..
- **Core Function**: Fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mosdepth`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Compute depth
**Args:** `mosdepth -t 4 output input.bam`
**Explanation:** Computes per-base depth from BAM file using 4 threads.

