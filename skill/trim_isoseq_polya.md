---
name: trim_isoseq_polya
category: utility
description: Trim Iso-seq PolyA - Tool for trimming polyA tails from Iso-seq reads.
tags: [trim_isoseq_polya, isoseq, polya-trimming, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/IsoSeq_Analysis"
---

## Concepts

- **Tool Overview**: Trim Iso-seq PolyA - A tool for trimming polyA tails from PacBio Iso-seq sequencing reads.
- **Core Function**: Identifies and removes polyA tails from long-read sequencing data.
- **Input**: FASTQ/FASTA files from Iso-seq sequencing.
- **Output**: Trimmed sequences, polyA statistics.
- **Installation**: Part of PacBio SMRT Analysis suite
- **Use Case**: Iso-seq data processing, long-read sequencing analysis.

## Pitfalls

- **PolyA Length**: Variable polyA tail lengths may affect trimming.
- **Sequence Quality**: Low-quality sequences may cause issues.

## Examples

### Trim polyA tails
**Args:** `trim_isoseq_polya -i reads.fastq -o trimmed.fastq`
**Explanation:** Trim polyA tails from Iso-seq reads.

### With quality filtering
**Args:** `trim_isoseq_polya -i raw.fastq -q 20 -o clean.fastq`
**Explanation:** Trim polyA tails with quality filtering.
