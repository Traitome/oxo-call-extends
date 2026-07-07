---
name: metamlst
category: metagenomics
description: A computational pipeline for MLST typing from metagenomic data
tags: [metamlst, metagenomics, MLST, typing]
author: oxo-call-community
source_url: "https://github.com/SegataLab/metamlst"
---

## Concepts

- **Tool Overview**: MetaMLST v1.2.3 is a computational pipeline for Multi-Locus Sequence Typing (MLST) directly from metagenomic sequencing data.
- **Core Function**: Performs MLST typing on metagenomic samples to identify bacterial strains and sequence types.
- **MLST Typing**: Determines sequence types based on conserved housekeeping genes.
- **Direct from Metagenome**: Enables MLST typing without prior isolation of bacterial strains.
- **Input/Output**: Accepts FASTQ sequencing reads; outputs MLST profiles with sequence types.
- **Strain Identification**: Identifies bacterial strains present in metagenomic samples.

## Pitfalls

- **Coverage Depth**: Requires sufficient coverage depth for accurate MLST typing.
- **Reference Database**: MLST typing accuracy depends on reference database completeness.
- **Mixed Samples**: May struggle with samples containing multiple strains of the same species.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Sequence Quality**: Poor quality sequences may affect typing accuracy.
- **Allele Calling**: May have difficulty calling alleles from short reads.

## Examples

### Run MLST typing
**Args:** `metamlst -i reads.fastq -o results/`
**Explanation:** Performs MLST typing on metagenomic reads.

### With custom database
**Args:** `metamlst -i reads.fastq -d custom_db/ -o results/`
**Explanation:** Uses a custom MLST database for typing.

### Specify species
**Args:** `metamlst -i reads.fastq -s Escherichia_coli -o results/`
**Explanation:** Focuses MLST typing on a specific species.

### Paired-end analysis
**Args:** `metamlst -i reads_1.fastq reads_2.fastq -o results/`
**Explanation:** Processes paired-end sequencing data.

### Generate report
**Args:** `metamlst -i reads.fastq -o results/ -r report.txt`
**Explanation:** Generates a detailed MLST typing report.