---
name: damidseq_pipeline
category: qc
description: Automated pipeline for processing DamID sequencing datasets
tags: [damidseq_pipeline, qc, DamID, chromatin-profiling, pipeline]
author: oxo-call-community
source_url: "https://owenjm.github.io/damidseq_pipeline"
---

## Concepts

- **Tool Overview**: damidseq_pipeline (v1.6.2+) is an automated pipeline for processing DNA adenine methyltransferase identification (DamID) sequencing datasets.
- **Core Function**: Processes raw DamID-seq data to identify protein-DNA interaction sites.
- **Input/Output**: Input: FASTQ reads, genome reference. Output: BedGraph/Wiggle tracks, gene lists.
- **Algorithm**: Implements standard DamID analysis with GATC fragment normalization.
- **Key Features**: Automated processing, quality control, visualization support.
- **Installation**: `conda install -c bioconda damidseq_pipeline`

## Pitfalls

- **DamID-specific**: Designed specifically for DamID-seq experiments.
- **Control Sample**: Requires appropriate GATC control sample.
- **Genome Index**: Requires genome-specific indexes for mapping.
- **Quality Control**: QC steps are important for reliable results.
- **Interpretation**: Results require biological interpretation.

## Examples

### Run DamID pipeline
**Args:** `damidseq_pipeline -1 R1.fastq.gz -2 R2.fastq.gz -g dm3 -o results/`
**Explanation:** Process DamID-seq data with Drosophila genome.

### Run with control
**Args:** `damidseq_pipeline -1 R1.fastq.gz -2 R2.fastq.gz -c control.fastq.gz -g hg19 -o results/`
**Explanation:** Process with GATC-only control sample.

### Generate bedGraph
**Args:** `damidseq_pipeline -1 R1.fastq.gz -2 R2.fastq.gz -g hg38 -o results/ --bedgraph`
**Explanation:** Output results in bedGraph format.
