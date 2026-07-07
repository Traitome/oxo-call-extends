---
name: micro_razers
category: alignment
description: MicroRazerS - Rapid Alignment of Small RNA Reads
tags: [micro_razers, alignment, small-rna]
author: oxo-call-community
source_url: "https://github.com/seqan/seqan/tree/seqan-v2.1.1/apps/micro_razers"
---

## Concepts

- **Tool Overview**: MicroRazerS v1.0.6 is a rapid aligner for small RNA sequencing reads.
- **Core Function**: Aligns small RNA sequencing reads to reference sequences.
- **Small RNA Alignment**: Optimized for small RNA sequencing data.
- **Rapid Alignment**: Provides fast alignment of short reads.
- **Input/Output**: Accepts small RNA reads; outputs alignments.
- **RNA-seq Analysis**: Supports small RNA-seq data analysis.

## Pitfalls

- **Small RNA Specific**: Designed for small RNA sequences.
- **Read Length**: Optimized for short reads.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal alignment.
- **Data Quality**: Alignment accuracy depends on input data quality.
- **Reference Genome**: Requires appropriate reference sequences.

## Examples

### Align small RNA reads
**Args:** `micro_razers -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Aligns small RNA reads to reference genome.

### With custom settings
**Args:** `micro_razers -i reads.fastq -r reference.fasta -o alignments.sam -m 2`
**Explanation:** Allows up to 2 mismatches.

### Paired-end alignment
**Args:** `micro_razers -i reads_1.fastq -R reads_2.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Processes paired-end small RNA data.

### Batch processing
**Args:** `micro_razers -i fastq/ -r reference.fasta -o alignments/`
**Explanation:** Processes multiple read files in batch mode.

### Generate statistics
**Args:** `micro_razers -i reads.fastq -r reference.fasta -o alignments.sam -s stats.txt`
**Explanation:** Generates alignment statistics.