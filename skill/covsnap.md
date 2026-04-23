---
name: covsnap
category: annotation
description: Coverage inspector for targeted sequencing QC (hg38)
tags: [covsnap, annotation, BAM, CRAM, GTF, BED]
author: oxo-call-community
source_url: "https://github.com/enes-ak/covsnap/blob/main/README.md"
---

## Concepts

- **Tool Overview**: covsnap (v0.3.0) - Coverage inspector for targeted sequencing QC (hg38)
- **Core Function**: covsnap computes per-target and per-exon depth metrics from BAM/CRAM files, producing an interactive HTML report with PASS/FAIL classifications and visual coverage summaries. Includes a cross-platform...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda covsnap`

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
