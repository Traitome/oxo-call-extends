---
name: tidehunter
category: analysis
description: TideHunter - Tandem repeat detection tool optimized for noisy long-read sequencing.
tags: [tidehunter, tandem-repeat, long-read, nanopore, pacbio, repeat-detection]
author: oxo-call-community
source_url: "https://github.com/SciLifeLab/TideHunter"
---

## Concepts

- **Tool Overview**: TideHunter - A tool for detecting tandem repeats in noisy long-read sequencing data, optimized for Oxford Nanopore and PacBio reads.
- **Core Function**: Identifies and characterizes tandem repeats by analyzing raw signal data and basecalled sequences.
- **Input**: Long-read sequencing data (FASTQ) from Nanopore or PacBio.
- **Output**: Tandem repeat annotations, repeat unit sequences, and read-level repeat counts.
- **Installation**: `conda install -c bioconda tidehunter`
- **Use Case**: Characterizing tandem repeats in noisy long-read data, repeat expansion disorders, genome assembly validation.

## Pitfalls

- **Long Reads Required**: Designed for long reads - not suitable for short-read data.
- **Noise Handling**: Despite optimization for noisy data, very low quality reads may affect results.

## Examples

### Detect tandem repeats
**Args:** `TideHunter -i reads.fastq.gz -o tandem_repeats/`
**Explanation:** Detect tandem repeats from long-read sequencing data.

### Adjust repeat unit size
**Args:** `TideHunter -i nanopore_reads.fastq -o results/ -min 5 -max 100`
**Explanation:** Search for tandem repeats with unit size between 5 and 100 bp.
