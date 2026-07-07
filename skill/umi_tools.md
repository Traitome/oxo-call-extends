---
name: umi_tools
category: bioinformatics
description: UMI-tools - Tools for UMI-based sequencing analysis.
tags: [umi_tools, umi, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/CGATOxford/UMI-tools"
---

## Concepts

- **Tool Overview**: UMI-tools - A comprehensive suite for UMI-based analysis.
- **Core Function**: UMI extraction, deduplication, and counting.
- **Input**: FASTQ, BAM, or SAM files.
- **Output**: Processed data with UMI information.
- **Installation**: Install via pip or conda
- **Use Case**: RNA-seq, scRNA-seq, ChIP-seq analysis, bioinformatics.

## Pitfalls

- **UMI Design**: Results depend on UMI design quality.
- **Memory**: May require significant memory for large datasets.

## Examples

### Extract UMIs
**Args:** `umi_tools extract --bc-pattern=NNNN --stdin=reads.fastq --stdout=umi_reads.fastq`
**Explanation:** Extract UMIs from reads.

### Deduplicate
**Args:** `umi_tools dedup --stdin=aligned.bam --stdout=deduplicated.bam`
**Explanation:** Deduplicate reads by UMI.
