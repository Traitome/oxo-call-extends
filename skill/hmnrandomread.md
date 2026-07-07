---
name: hmnrandomread
category: utility
description: HmnRandomRead is a sequence-read simulator program for generating synthetic NGS reads for testing and benchmarking.
tags: [hmnrandomread, simulation, NGS, reads]
author: oxo-call-community
source_url: "https://github.com/guillaume-gricourt/HmnRandomRead"
---

## Concepts

- **Synthetic Read Generation**: Generates realistic synthetic sequencing reads from reference genomes for testing bioinformatics pipelines.
- **Error Modeling**: Incorporates realistic sequencing error models including base substitutions, insertions, deletions, and quality score degradation.
- **Platform Simulation**: Supports simulation of different sequencing platforms including Illumina, Ion Torrent, and Oxford Nanopore.
- **Coverage Control**: Allows specification of target coverage depth or read count for controlled simulation experiments.
- **Paired-End Support**: Generates paired-end reads with configurable insert size distributions and mate orientation.
- **Quality Score Profiles**: Models quality score decay patterns characteristic of real sequencing data.

## Pitfalls

- **Reference Genome Requirements**: Requires a valid reference genome in FASTA format; fragmented or incomplete references may cause errors.
- **Computational Resources**: Generating large datasets requires significant memory and processing time.
- **Seed Reproducibility**: Set explicit random seed for reproducible results; default behavior may produce different outputs.
- **Insert Size Distribution**: Incorrect insert size parameters can produce unrealistic read pairs that don't reflect real sequencing libraries.
- **Error Rate Realism**: Default error rates may not match specific sequencing platforms; adjust based on target platform characteristics.
- **Output File Size**: Large-scale simulations can generate enormous output files; plan storage accordingly.

## Examples

### Generate single-end reads with default settings
**Args:** `hmnrandomread -r reference.fasta -o reads.fastq -n 1000000`
**Explanation:** Generates 1 million single-end reads from the reference genome with default error model.

### Generate paired-end reads with specific insert size
**Args:** `hmnrandomread -r reference.fasta -o1 reads_R1.fastq -o2 reads_R2.fastq -n 500000 -i 300 -s 50`
**Explanation:** Generates 500,000 paired-end read pairs with mean insert size of 300bp and standard deviation of 50bp.

### Simulate specific sequencing platform
**Args:** `hmnrandomread -r reference.fasta -o nanopore_reads.fastq -p nanopore -n 100000`
**Explanation:** Generates Oxford Nanopore-style reads with appropriate error profiles and read length distributions.

### Control coverage depth
**Args:** `hmnrandomread -r reference.fasta -o coverage_test.fastq -c 30`
**Explanation:** Generates reads to achieve approximately 30x coverage of the reference genome.

### Add realistic sequencing errors
**Args:** `hmnrandomread -r reference.fasta -o error_reads.fastq -e 0.02 -i 0.005 -d 0.005`
**Explanation:** Generates reads with 2% substitution error rate, 0.5% insertion rate, and 0.5% deletion rate.

### Reproducible simulation
**Args:** `hmnrandomread -r reference.fasta -o reproducible.fastq -n 100000 -S 42`
**Explanation:** Generates reproducible reads using seed 42, ensuring identical output across runs.