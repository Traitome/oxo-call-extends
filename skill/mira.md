---
name: mira
category: assembly
description: MIRA is a whole genome shotgun and EST sequence assembler for Sanger, 454, Solexa (Illumina), IonTorrent data and PacBio (the later at the moment only CCS and error-corrected CLR reads).
tags: [mira, assembly, genome]
author: oxo-call-community
source_url: "https://github.com/DrMicrobit/mira"
---

## Concepts

- **Tool Overview**: MIRA v5.0.0rc2 is a versatile genome and transcriptome assembler.
- **Core Function**: Assembles sequencing data from multiple platforms.
- **Multi-platform Support**: Handles Sanger, 454, Illumina, IonTorrent, and PacBio data.
- **Hybrid Assembly**: Supports combining data from different sequencing platforms.
- **Input/Output**: Accepts sequencing reads; outputs assembled contigs.
- **Genome Assembly**: Supports whole genome and EST assembly workflows.

## Pitfalls

- **Computational Resources**: Assembly may require significant resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal assembly.
- **Data Quality**: Assembly quality depends on input data quality.
- **Complexity**: May have steep learning curve for optimal usage.
- **Runtime**: Assembly can be time-consuming for large genomes.

## Examples

### Assemble genome
**Args:** `mira -project=my_project -job=genome,denovo,accurate -fasta -reads=reads.fastq`
**Explanation:** Runs genome assembly with default parameters.

### RNA-seq assembly
**Args:** `mira -project=my_project -job=est,denovo,accurate -fasta -reads=reads.fastq`
**Explanation:** Assembles transcriptome from RNA-seq data.

### Hybrid assembly
**Args:** `mira -project=my_project -job=genome,denovo,hybrid -fasta -reads=illumina.fastq,pacbio.fastq`
**Explanation:** Combines Illumina and PacBio data.

### Custom parameters
**Args:** `mira -project=my_project -job=genome,denovo,accurate -fasta -reads=reads.fastq -parameter=K:31`
**Explanation:** Uses custom k-mer size.

### Generate statistics
**Args:** `mira -project=my_project -job=genome,denovo,accurate -fasta -reads=reads.fastq -outputstats`
**Explanation:** Generates assembly statistics.