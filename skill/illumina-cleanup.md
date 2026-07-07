---
name: illumina-cleanup
category: hpc
description: Nextflow pipeline for pre-processing Illumina FASTQ files
tags: [illumina-cleanup, hpc, FASTQ, preprocessing, nextflow]
author: oxo-call-community
source_url: "https://github.com/rpetit3/illumina-cleanup"
---

## Concepts

- **Tool Overview**: illumina-cleanup (v1.0.0) - A Nextflow pipeline designed for automated pre-processing of Illumina sequencing data, including quality control, adapter trimming, and read filtering
- **Core Function**: Automates quality control, adapter removal, duplicate marking, and quality filtering for Illumina FASTQ files
- **Input/Output**: Accepts raw Illumina FASTQ files (single-end or paired-end), outputs cleaned and filtered FASTQ files with QC reports
- **Installation**: `conda install -c bioconda illumina-cleanup` or via Nextflow pipeline pull
- **Pipeline Structure**: Modular workflow with separate processes for FastQC, Trimmomatic, and MultiQC reporting

## Pitfalls

- **Version Differences**: Pipeline parameters and module availability may vary between Nextflow versions
- **Input Format**: Ensure input FASTQ files follow Illumina naming conventions (R1/R2 for paired-end)
- **Resource Requirements**: Large datasets require sufficient memory and CPU resources
- **Adapter Sequences**: Incorrect adapter specification can lead to incomplete trimming
- **Sample Sheet Format**: Improperly formatted sample sheets cause pipeline failures

## Examples

### Run basic preprocessing pipeline
**Args:** `nextflow run rpetit3/illumina-cleanup --input samplesheet.csv --outdir results`
**Explanation:** Executes the full preprocessing pipeline including QC, trimming, and filtering.

### Specify custom adapter sequences
**Args:** `nextflow run rpetit3/illumina-cleanup --input samplesheet.csv --outdir results --adapters custom_adapters.fa`
**Explanation:** Uses custom adapter sequences for trimming instead of default Illumina adapters.

### Run with specific quality thresholds
**Args:** `nextflow run rpetit3/illumina-cleanup --input samplesheet.csv --outdir results --phred-threshold 30 --min-length 50`
**Explanation:** Sets minimum Phred quality score to 30 and minimum read length to 50bp.

### Enable parallel processing
**Args:** `nextflow run rpetit3/illumina-cleanup --input samplesheet.csv --outdir results -profile slurm --max-cpus 32`
**Explanation:** Runs pipeline on SLURM cluster with 32 CPUs for parallel processing.

### Skip certain processing steps
**Args:** `nextflow run rpetit3/illumina-cleanup --input samplesheet.csv --outdir results --skip-trimming`
**Explanation:** Skips adapter trimming step, useful for already trimmed data.

### Generate comprehensive QC report
**Args:** `nextflow run rpetit3/illumina-cleanup --input samplesheet.csv --outdir results --multiqc`
**Explanation:** Generates aggregated MultiQC report summarizing all quality metrics.