---
name: theiacov-gc
category: analysis
description: theiaCoV-GC - The National SARS-CoV-2 Genomics Database pipeline for consensus sequence generation.
tags: [theiacov-gc, covid-19, sars-cov-2, consensus, genomics, public-health]
author: oxo-call-community
source_url: "https://github.com/aphred/theiaCoV-GC"
---

## Concepts

- **Tool Overview**: theiaCoV-GC (TheiaCoV Genome Consensus) - Part of the SARS-CoV-2 genomics database pipeline for generating consensus genome sequences.
- **Core Function**: Processes raw SARS-CoV-2 sequencing data to generate consensus genomes suitable for public health surveillance and variant calling.
- **Input**: Illumina or Oxford Nanopore sequencing reads (FASTQ), reference genome.
- **Output**: Consensus FASTA sequences, BAM alignments, variant calls in VCF format.
- **Installation**: `conda install -c bioconda theiacov-gc`
- **Use Case**: COVID-19 genomics surveillance, public health monitoring, variant tracking.

## Pitfalls

- **SARS-CoV-2 Only**: Designed specifically for SARS-CoV-2 - not generalizable to other viruses.
- **Quality Control**: Low-quality samples may produce incomplete consensus sequences.

## Examples

### Generate consensus genome
**Args:** `theiacov-gc -i reads.fastq.gz -o consensus.fasta -r sars-cov-2-reference.fasta`
**Explanation:** Generate consensus genome from raw reads.

### With default reference
**Args:** `theiacov-gc -i sample.fastq.gz -o results/`
**Explanation:** Use built-in SARS-CoV-2 reference for consensus generation.
