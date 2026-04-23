---
name: comparative-annotation-toolkit
category: alignment
description: A straightforward end-to-end pipeline that takes as input a HAL-format multiple whole genome alignment as well as a GFF3 file representing annotations on one high quality assembly in the HAL alignment, and produces a output GFF3 annotation on all target genomes chosen
tags: [comparative-annotation-toolkit, alignment, GFF]
author: oxo-call-community
source_url: "https://github.com/ComparativeGenomicsToolkit/Comparative-Annotation-Toolkit"
---

## Concepts

- **Tool Overview**: comparative-annotation-toolkit (v0.1) - A straightforward end-to-end pipeline that takes as input a HAL-format multiple whole genome alignment as well as a GFF3 file representing annotations on one high quality assembly in the HAL alignment, and produces a output GFF3 annotation on all target genomes chosen
- **Core Function**: A straightforward end-to-end pipeline that takes as input a HAL-format multiple whole genome alignment as well as a GFF3 file representing annotations on one high quality assembly in the HAL alignment, and produces a output GFF3 annotation on all target genomes chosen
- **Input/Output**: GFF/GTF annotation input/output
- **Installation**: `conda install -c bioconda comparative-annotation-toolkit`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
