---
name: muse
category: variant-calling
description: An accurate and ultra-fast somatic point mutation calling tool for whole-genome sequencing (WGS) and whole-exome sequencing (WES) data from heterogeneous tumor samples.
tags: [muse, variant-calling, alignment]
author: oxo-call-community
source_url: "https://bioinformatics.mdanderson.org/public-software/muse"
---

## Concepts

- **Tool Overview**: muse v2.1.2 - An accurate and ultra-fast somatic point mutation calling tool for whole-genome sequencing (WGS) and whole-exome sequencing (WES) data from heterogeneous tumor samples..
- **Core Function**: An accurate and ultra-fast somatic point mutation calling tool for whole-genome sequencing (WGS) and whole-exome sequencing (WES) data from heterogeneous tumor samples.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda muse`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Call variants
**Args:** `muse call -r reference.fa -f tumor.bam -o output.vcf`
**Explanation:** Calls somatic variants from tumor BAM file.

