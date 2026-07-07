---
name: mmlong2
category: metagenomics
description: An all-in-one genome-centric metagenomics workflow using long reads
tags: [mmlong2, metagenomics, assembly]
author: oxo-call-community
source_url: "https://github.com/Serka-M/mmlong2"
---

## Concepts

- **Tool Overview**: mmlong2 v1.2.1 is an all-in-one genome-centric metagenomics workflow.
- **Core Function**: Processes long-read metagenomic data for genome recovery.
- **Long-read Support**: Optimized for Nanopore and PacBio sequencing data.
- **Genome-centric**: Focuses on recovering complete microbial genomes.
- **Input/Output**: Accepts raw reads; outputs assembled genomes and annotations.
- **End-to-end Workflow**: Integrated pipeline from raw reads to finished genomes.

## Pitfalls

- **Long-read Specific**: Designed for long-read sequencing data only.
- **Computational Resources**: Metagenomic analysis requires significant resources.
- **Memory Requirements**: Memory usage depends on dataset complexity.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Results depend on read quality and sequencing depth.
- **Contamination Risk**: Requires careful sample handling to avoid contamination.

## Examples

### Run complete workflow
**Args:** `mmlong2 --reads reads.fastq --output results/`
**Explanation:** Runs the complete metagenomics workflow.

### With Nanopore reads
**Args:** `mmlong2 --reads reads.fastq --platform nanopore --output results/`
**Explanation:** Optimized for Oxford Nanopore data.

### With PacBio reads
**Args:** `mmlong2 --reads reads.fastq --platform pacbio --output results/`
**Explanation:** Optimized for PacBio sequencing data.

### With quality filtering
**Args:** `mmlong2 --reads reads.fastq --quality-filter --output results/`
**Explanation:** Applies quality filtering before assembly.

### Batch processing
**Args:** `mmlong2 --input-dir fastq/ --output-dir results/`
**Explanation:** Processes multiple samples.