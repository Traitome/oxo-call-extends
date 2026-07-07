---
name: umis
category: bioinformatics
description: UMIs - Toolkit for Unique Molecular Identifier processing.
tags: [umis, umi, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vals/umis"
---

## Concepts

- **Tool Overview**: UMIs - A toolkit for processing Unique Molecular Identifiers.
- **Core Function**: UMI extraction, deduplication, and analysis.
- **Input**: FASTQ or BAM files.
- **Output**: Processed reads with UMI information.
- **Installation**: Install via pip
- **Use Case**: UMI-based sequencing analysis, bioinformatics.

## Pitfalls

- **UMI Pattern**: Requires correct UMI pattern specification.
- **Memory**: May require significant memory for large datasets.

## Examples

### Extract UMIs
**Args:** `umis extract --input reads.fastq --output umi_reads.fastq`
**Explanation:** Extract UMIs from reads.

### Deduplicate by UMI
**Args:** `umis dedup --input aligned.bam --output deduplicated.bam`
**Explanation:** Deduplicate reads by UMI.
