---
name: isonclust
category: expression
description: De novo clustering of long-read transcriptome reads, original implementation.
tags: [isonclust, expression, long reads, transcriptomics, clustering]
author: oxo-call-community
source_url: "https://github.com/ksahlin/isONclust"
---

## Concepts

- **De Novo Transcript Clustering**: Groups long-read transcriptomic sequences into gene clusters without reference genome.
- **Graph-Based Clustering**: Uses graph algorithms to identify connected components of similar reads.
- **Overlap Detection**: Detects read overlaps to determine transcript relationships.
- **Error-Tolerant Matching**: Accounts for high error rates in long-read sequencing data.
- **Isoform Identification**: Identifies different isoforms within gene clusters.
- **Output Formats**: Generates cluster assignments in various formats for downstream analysis.

## Pitfalls

- **High Error Rates**: Long-read errors can lead to incorrect cluster assignments.
- **Computational Complexity**: Clustering large datasets is computationally intensive.
- **Memory Usage**: Processing millions of reads requires significant memory.
- **Parameter Sensitivity**: Results can be sensitive to clustering parameters.
- **Transcript Similarity**: Highly similar transcripts may be merged incorrectly.
- **Coverage Bias**: Uneven sequencing coverage affects clustering completeness.

## Examples

### Basic usage
**Args:** `isonclust --fastq reads.fastq --outfolder output/`
**Explanation:** Performs de novo clustering of long-read transcriptome reads.

### With preprocessing
**Args:** `isonclust --fastq reads.fastq --preprocess --outfolder output/`
**Explanation:** Applies preprocessing steps before clustering.

### Specify minimum length
**Args:** `isonclust --fastq reads.fastq --min_len 500 --outfolder output/`
**Explanation:** Filters reads shorter than 500 bases before clustering.

### Adjust sensitivity
**Args:** `isonclust --fastq reads.fastq --sensitivity high --outfolder output/`
**Explanation:** Uses high sensitivity mode for more precise clustering.

### Generate FASTA output
**Args:** `isonclust --fastq reads.fastq --outfolder output/ --fasta`
**Explanation:** Generates consensus sequences in FASTA format.

### Quality filtering
**Args:** `isonclust --fastq reads.fastq --quality_filter --outfolder output/`
**Explanation:** Filters reads based on quality scores before clustering.