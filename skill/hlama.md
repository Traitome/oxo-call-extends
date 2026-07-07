---
name: hlama
category: immunology
description: Simple matching of HTS samples based on HLA typing for consistency checking.
tags: [hlama, HLA, sample matching, quality control, tumor-normal]
author: oxo-call-community
source_url: "https://github.com/bihealth/hlama"
---

## Concepts

- **Sample Matching**: hlama (v3.0.1) performs consistency checking by comparing HLA types across samples.
- **Tumor-Normal Validation**: Validates matched tumor/normal pairs by ensuring HLA types match between samples.
- **Pedigree Analysis**: Checks Mendelian inheritance rules in family-based sequencing data.
- **Multi-resolution Comparison**: Compares HLA types at both 2-digit (serological) and 4-digit (protein) resolution.
- **Snakemake Workflow**: Uses Snakemake for workflow orchestration, enabling parallel execution on compute clusters.

## Pitfalls

- **Coverage Requirements**: Requires sufficient coverage of HLA loci for accurate typing; low coverage may lead to false mismatches.
- **OptiType Dependency**: Relies on OptiType for HLA typing, which has its own memory requirements.
- **Yara Mapper**: Uses Yara for read prefiltering, requiring proper installation and configuration.
- **Python 3 Only**: Requires Python 3 environment; not compatible with Python 2.
- **Cluster Configuration**: Parallel execution requires proper cluster configuration for Snakemake.

## Examples

### Run tumor-normal matching
**Args:** `hlama --mode tumor-normal --tumor tumor.bam --normal normal.bam --output ./results`
**Explanation:** Compares HLA types between tumor and normal samples to verify sample identity.

### Analyze pedigree data
**Args:** `hlama --mode pedigree --samples samples.csv --pedigree family.ped --output ./pedigree_results`
**Explanation:** Checks Mendelian inheritance of HLA types across family members.

### Generate mismatch report
**Args:** `hlama --mode compare --input sample1.hla sample2.hla --output mismatch_report.txt`
**Explanation:** Compares two HLA typing results and generates a mismatch report.

### Run with increased threads
**Args:** `hlama --mode tumor-normal --tumor tumor.bam --normal normal.bam --threads 16 --output ./results`
**Explanation:** Executes HLA matching with 16 threads for faster processing.

### Integrate with Snakemake cluster
**Args:** `snakemake --profile cluster --snakefile $(hlama --snakefile) --config tumor=tumor.bam normal=normal.bam`
**Explanation:** Runs hlama workflow on a compute cluster using Snakemake.