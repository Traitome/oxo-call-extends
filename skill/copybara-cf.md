---
name: copybara-cf
category: qc
description: Copy number analysis for long-read cfDNA sequencing data
tags: [copybara-cf, copy-number, cfDNA, long-reads, liquid-biopsy]
author: oxo-call-community
source_url: "https://github.com/cortes-ciriano-lab/copybara-cf"
---

## Concepts

- **Tool Overview**: COPYBARA-CF is a tool for copy number variation analysis specifically designed for long-read cell-free DNA (cfDNA) sequencing data from liquid biopsies.
- **Core Function**: Detects copy number alterations in cfDNA samples using long-read sequencing technology.
- **Algorithm**: Analyzes read depth and fragmentation patterns to identify copy number changes.
- **Input**: Long-read sequencing reads from cfDNA samples (FASTQ/BAM).
- **Output**: Copy number profiles, segmentations, and variant calls.
- **Application**: Liquid biopsy analysis, cancer detection, and minimal residual disease monitoring.
- **Installation**: Install via bioconda: `conda install -c bioconda copybara-cf`

## Pitfalls

- **Input Quality**: Requires high-quality long-read data for accurate CNV calling.
- **Fragmentation**: cfDNA fragmentation patterns may affect read mapping.
- **Contamination**: Contamination from normal cells can obscure tumor signals.
- **Low Coverage**: cfDNA samples may have low coverage requiring careful analysis.
- **Reference Genome**: Requires appropriate reference genome for mapping.

## Examples

### Analyze copy number from reads
**Args:** `copybara-cf -i reads.fastq -r reference.fasta -o cnv_results/`
**Explanation:** Performs copy number analysis on long-read cfDNA data.

### From aligned BAM
**Args:** `copybara-cf -b aligned.bam -o cnv_results/`
**Explanation:** Analyzes copy number from pre-aligned BAM file.

### With tumor fraction estimation
**Args:** `copybara-cf -i reads.fastq -r reference.fasta --estimate-tumor -o cnv_results/`
**Explanation:** Estimates tumor fraction alongside CNV analysis.

### Display help
**Args:** `copybara-cf --help`
**Explanation:** Shows all available options and usage information.