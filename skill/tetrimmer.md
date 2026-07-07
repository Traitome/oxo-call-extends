---
name: tetrimmer
category: preprocessing
description: TETrimmer - Adapter and quality trimmer specifically for transposable element sequencing data.
tags: [tetrimmer, trimming, adapter, quality, te-sequencing, preprocessing]
author: oxo-call-community
source_url: "https://github.com/compbio/tetrimmer"
---

## Concepts

- **Tool Overview**: TETrimmer - A read trimming tool specifically designed for transposable element sequencing data.
- **Core Function**: Removes adapters, low-quality bases, and artifacts specific to TE sequencing library preparation.
- **Input**: Raw FASTQ files from TE-targeted sequencing.
- **Output**: Trimmed FASTQ files ready for TE analysis.
- **Installation**: `pip install tetrimmer` or `conda install -c bioconda tetrimmer`
- **Use Case**: Preprocessing TE sequencing data before expression or enrichment analysis.

## Pitfalls

- **TE-specific**: Designed for TE sequencing protocols - may not be optimal for standard RNA-seq.
- **Over-trimming**: Aggressive trimming may remove biologically relevant sequence.

## Examples

### Basic trimming
**Args:** `tetrimmer -i raw_reads.fastq.gz -o trimmed_reads/`
**Explanation:** Trim adapters and low-quality bases from TE sequencing data.

### Strict mode
**Args:** `tetrimmer -i reads.fastq.gz -o output/ --stringency high`
**Explanation:** Use more aggressive trimming settings for low-quality data.
