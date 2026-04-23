---
name: onebam
category: alignment
description: ONEcode replacement for SAM/BAM in large-scale eDNA mapping and taxonomic analysis.
tags: [onebam, alignment]
author: oxo-call-community
source_url: "https://github.com/richarddurbin/onebam"
---

## Concepts
- **Tool Overview**: onebam converts read-sorted SAM/BAM/CRAM files into a compact ONEcode .1read format, storing reads with sequences, quality scores, best-match damage information, and taxonomy hit data. It supports merging, LCA (Lowest Common Ancestor) assignment, taxonomic reporting, and read extraction, making it suitable for eDNA workflows mapping against very large reference databases such as all of NCBI.
- **Core Function**: Processes bioinformatics data for alignment tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda onebam`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
