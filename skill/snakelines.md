---
name: snakelines
category: sequencing
description: Snakelines - Computational pipelines for processing paired-end sequencing reads
tags: [snakelines, sequencing, snakemake, ngs, pipeline]
author: oxo-call-community
source_url: "https://snakelines.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: snakelines (v1.1.8) - Snakemake pipelines for paired-end sequencing data processing
- **Core Function**: Processes raw sequencing reads through quality control, trimming, and alignment
- **Input/Output**: Accepts FASTQ reads; outputs aligned BAM files and QC reports
- **Algorithm**: Integrates multiple bioinformatics tools for NGS data processing
- **Installation**: `conda install -c bioconda snakelines`
- **Key Features**: Modular pipelines, quality control, reproducibility

## Pitfalls

- **Input Requirements**: Requires properly formatted paired-end FASTQ files
- **Reference Genome**: Must use compatible reference genome
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for alignment
- **Parameter Tuning**: Requires careful parameter adjustment
- **Dependency Management**: All dependencies must be properly installed

## Examples

### Display help
**Args:** `snakelines --help`
**Explanation:** Shows available options and usage information.

### Run pipeline
**Args:** `snakelines -c config.yaml -o results/`
**Explanation:** Run Snakelines pipeline with config file.

### Dry run
**Args:** `snakelines -c config.yaml --dryrun`
**Explanation:** Perform dry run to check pipeline.

### Specify threads
**Args:** `snakelines -c config.yaml -o results/ -t 8`
**Explanation:** Use 8 threads for parallel processing.

### Resume interrupted run
**Args:** `snakelines -c config.yaml -o results/ --resume`
**Explanation:** Resume previously interrupted pipeline run.

### Generate report
**Args:** `snakelines -c config.yaml -o results/ --report`
**Explanation:** Generate analysis report.

### With custom reference
**Args:** `snakelines -c config.yaml -r custom_reference.fasta -o results/`
**Explanation:** Use custom reference genome.

### Quality control only
**Args:** `snakelines -c config.yaml -o results/ --qc-only`
**Explanation:** Run only quality control steps.