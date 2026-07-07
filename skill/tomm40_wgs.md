---
name: tomm40_wgs
category: analysis
description: TOMM40-WGS - Tool for analyzing TOMM40 repeat expansions from whole-genome sequencing.
tags: [tomm40_wgs, tomm40, repeat-expansion, wgs, alzheimer]
author: oxo-call-community
source_url: "https://github.com/compbio/tomm40_wgs"
---

## Concepts

- **Tool Overview**: TOMM40-WGS - A tool for analyzing TOMM40 repeat expansions from whole-genome sequencing data.
- **Core Function**: Identifies and characterizes TOMM40 repeat length variations associated with Alzheimer's disease risk.
- **Input**: Whole-genome sequencing data (BAM/FASTQ), reference genome.
- **Output**: Repeat length calls, risk classification, quality metrics.
- **Installation**: `pip install tomm40-wgs` or `conda install -c bioconda tomm40-wgs`
- **Use Case**: Alzheimer's disease research, genetic risk assessment, population genetics.

## Pitfalls

- **Repeat Complexity**: Complex repeat structures may affect accuracy.
- **Coverage**: Requires sufficient coverage in TOMM40 region.

## Examples

### Analyze TOMM40 repeats
**Args:** `tomm40-wgs -i wgs.bam -o tomm40_results/`
**Explanation:** Analyze TOMM40 repeat expansions from WGS data.

### Batch processing
**Args:** `tomm40-wgs --batch samples.list -o batch_results/`
**Explanation:** Process multiple samples for TOMM40 repeat analysis.
