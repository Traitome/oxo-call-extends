---
name: artex
category: utility
description: Artex - Artic pipeline extension for enhanced pathogen genome assembly
tags: [artex, utility, artic, pathogen-genomics, outbreak-surveillance, nanopore]
author: oxo-call-community
source_url: "https://github.com/JMencius/Artex"
---

## Concepts

- **Tool Overview**: Artex is an extension to the Artic pipeline for improved pathogen genome assembly from nanopore sequencing data. Version 0.2.0.
- **Core Function**: Enhances Artic pipeline with additional features for outbreak surveillance and pathogen genomics.
- **Artic Integration**: Builds upon Artic pipeline for real-time nanopore-based pathogen genome assembly.
- **Outbreak Tracking**: Supports rapid genome assembly for outbreak surveillance and epidemiological investigations.
- **Quality Control**: Includes additional QC metrics and filtering options for improved assembly quality.
- **Nanopore Optimization**: Optimized for Oxford Nanopore long-read sequencing data.
- **Input/Output**: Accepts nanopore FASTQ reads and outputs assembled genomes with QC reports.
- **Installation**: `conda install -c bioconda artex` or install from GitHub.

## Pitfalls

- **Artic Dependency**: Requires Artic pipeline installation and configuration. Ensure Artic is properly set up.
- **Nanopore Quality**: Basecalling quality affects assembly accuracy. Use high-quality basecalled reads.
- **Coverage Requirements**: Requires adequate coverage (>50x) for reliable assembly. Low coverage produces fragmented assemblies.
- **Reference Genome**: Requires appropriate reference genome for primer scheme and assembly.
- **Primer Scheme**: Artic requires primer scheme for amplicon-based sequencing. Incorrect scheme causes assembly failure.

## Examples

### Display help
**Args:** `artex --help`
**Explanation:** Shows all available command-line options and usage information.

### Run extended Artic pipeline
**Args:** `artex run --input reads.fastq --primer_scheme scheme.txt --outdir results/`
**Explanation:** Runs extended Artic pipeline with Artex enhancements. Outputs assembled genome and QC reports.

### Specify reference genome
**Args:** `artex run --input reads.fastq --reference genome.fasta --outdir results/`
**Explanation:** Uses specified reference genome for assembly and variant calling.

### Adjust coverage threshold
**Args:** `artex run --input reads.fastq --min_coverage 30 --outdir results/`
**Explanation:** Sets minimum coverage threshold of 30x for assembly. Filters low-coverage regions.

### Enable additional QC
**Args:** `artex run --input reads.fastq --extended_qc --outdir results/`
**Explanation:** Enables extended quality control metrics and reporting beyond standard Artic.

### Batch processing
**Args:** `artex batch --input_dir fastq_files/ --primer_scheme scheme.txt --output_dir results/`
**Explanation:** Processes multiple samples in batch mode for high-throughput analysis.

### Generate detailed report
**Args:** `artex run --input reads.fastq --report detailed_report.html --outdir results/`
**Explanation:** Generates detailed HTML report with assembly statistics, QC metrics, and visualizations.