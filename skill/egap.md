---
name: egap
category: assembly
description: "EGAP pipeline for genome assembly and QC analysis"
tags: [egap, assembly]
author: oxo-call-community
source_url: "https://github.com/iPsychonaut/EGAP"
---

## Concepts
- **Tool Overview**: EGAP (Entheome Genome Assembly Pipeline) is a versatile bioinformatics pipeline for hybrid genome assembly from Oxford Nanopore, Illumina, and PacBio data. It supports multiple input modes and assembly methods and determines the best based on multiple metrics: BUSCO Completeness (Single + Duplicated), Assembly Contig Count, Assembly N50, Assembly L50, and Assembly GC-content.
- **Core Function**: EGAP pipeline for genome assembly and QC analysis
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda egap`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
