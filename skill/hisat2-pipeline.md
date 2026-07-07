---
name: hisat2-pipeline
category: alignment
description: A pipeline to automatically run RNA-seq analysis using HISAT2/StringTie with default settings.
tags: [hisat2-pipeline, RNA-seq, alignment, HISAT2, StringTie]
author: oxo-call-community
source_url: "https://github.com/mcamagna/HISAT2-pipeline"
---

## Concepts

- **RNA-seq Analysis**: Automated pipeline for RNA-seq data analysis.

- **HISAT2 Alignment**: Uses HISAT2 for fast and accurate read alignment.

- **StringTie Assembly**: Performs transcript assembly with StringTie.

- **Quality Control**: Integrated quality control steps.

- **Differential Expression**: Supports downstream differential expression analysis.

- **Pre-built Indices**: Supports pre-built genome indices for common organisms.

## Pitfalls

- **Reference Genome**: Requires appropriate reference genome index.

- **Input Format**: Requires properly formatted FASTQ input files.

- **Computational Resources**: May require significant computational resources.

- **Memory Usage**: Large datasets may require substantial memory.

- **Parameter Tuning**: Default parameters may need adjustment for specific datasets.

## Examples

### Run RNA-seq pipeline with paired-end reads
**Args:** `hisat2-pipeline --forward reads_1.fastq --reverse reads_2.fastq --output results/`
**Explanation:** Runs the complete RNA-seq analysis pipeline.

### With custom genome index
**Args:** `hisat2-pipeline --forward reads_1.fastq --reverse reads_2.fastq --index /path/to/index --output results/`
**Explanation:** Uses a custom HISAT2 genome index.

### With reference genome
**Args:** `hisat2-pipeline --forward reads_1.fastq --reverse reads_2.fastq --genome hg38 --output results/`
**Explanation:** Uses pre-built hg38 genome index.

### Single-end reads
**Args:** `hisat2-pipeline --single reads.fastq --output results/`
**Explanation:** Processes single-end sequencing data.

### With quality filtering
**Args:** `hisat2-pipeline --forward reads_1.fastq --reverse reads_2.fastq --quality 20 --output results/`
**Explanation:** Filters reads by quality score.

### Generate QC report
**Args:** `hisat2-pipeline --forward reads_1.fastq --reverse reads_2.fastq --qc-report --output results/`
**Explanation:** Generates comprehensive QC report.

### Help command
**Args:** `hisat2-pipeline --help`
**Explanation:** Shows available options and usage information.