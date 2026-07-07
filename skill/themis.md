---
name: themis
category: analysis
description: THEMIS - Pipeline for processing and analyzing SARS-CoV-2 genomic data.
tags: [themis, covid-19, sars-cov-2, genomics, variant-calling, pipeline]
author: oxo-call-community
source_url: "https://github.com/secureamber/themis"
---

## Concepts

- **Tool Overview**: THEMIS - A comprehensive pipeline for processing and analyzing SARS-CoV-2 sequencing data with variant calling and clade assignment.
- **Core Function**: Processes raw sequencing data, calls variants, assigns pangolin lineages, and generates reports for SARS-CoV-2 surveillance.
- **Input**: SARS-CoV-2 sequencing reads (FASTQ) from Illumina or Nanopore.
- **Output**: Consensus genomes, VCF files, pangolin lineage reports, Nextstrain clade assignments.
- **Installation**: `conda install -c bioconda themis`
- **Use Case**: COVID-19 genomic epidemiology, variant surveillance, public health reporting.

## Pitfalls

- **SARS-CoV-2 Only**: Specialized pipeline for SARS-CoV-2.
- **Lineage Database**: Pangolin lineage assignment depends on updated reference databases.

## Examples

### Process sample
**Args:** `themis -i sample.fastq.gz -o results/`
**Explanation:** Run complete SARS-CoV-2 analysis pipeline on sample.

### Batch processing
**Args:** `themis batch -i samples.txt -o batch_results/`
**Explanation:** Process multiple samples from sample sheet.
