---
name: mitorsaw
category: utility
description: A tool for mitochondrial analysis for HiFi sequencing data
tags: [mitorsaw, utility, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/mitorsaw"
---

## Concepts

- **Tool Overview**: MitorSaw v0.2.8 analyzes mitochondrial genomes from HiFi data.
- **Core Function**: Processes PacBio HiFi sequencing data for mtDNA analysis.
- **HiFi Sequencing**: Optimized for high-fidelity sequencing data.
- **Mitochondrial Analysis**: Performs mtDNA-specific analyses.
- **Input/Output**: Accepts HiFi reads; outputs mitochondrial sequences.
- **Long-read Sequencing**: Supports long-read mitochondrial sequencing workflows.

## Pitfalls

- **HiFi Specific**: Designed for PacBio HiFi data.
- **Computational Resources**: Processing may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal analysis.
- **Data Quality**: Results depend on input data quality.
- **PacBio Data**: Requires PacBio-specific input format.

## Examples

### Analyze mitochondrial HiFi data
**Args:** `mitorsaw analyze -i hifi_reads.fastq -o results/`
**Explanation:** Runs mitochondrial analysis on HiFi data.

### With reference
**Args:** `mitorsaw analyze -i hifi_reads.fastq -r ref_mito.fasta -o results/`
**Explanation:** Uses reference mitochondrial genome.

### Assemble mtDNA
**Args:** `mitorsaw assemble -i hifi_reads.fastq -o mito_genome.fasta`
**Explanation:** Assembles mitochondrial genome.

### Batch processing
**Args:** `mitorsaw analyze -i fastq/ -o results/`
**Explanation:** Processes multiple HiFi files.

### Generate statistics
**Args:** `mitorsaw analyze -i hifi_reads.fastq -o results/ -s stats.txt`
**Explanation:** Generates analysis statistics.