---
name: mageck-vispr
category: qc
description: MAGeCK-VISPR is a comprehensive quality control, analysis and visualization workflow for CRISPR/Cas9 screens based on MAGeCK, VISPR, Snakemake, FastQC and cutadapt.
tags: [mageck-vispr, qc, CRISPR, workflow]
author: oxo-call-community
source_url: "https://bitbucket.org/liulab/mageck-vispr"
---

## Concepts

- **Tool Overview**: mageck-vispr v0.5.6 - A comprehensive Snakemake workflow for CRISPR/Cas9 screening data analysis, integrating MAGeCK, VISPR, FastQC, and cutadapt.
- **Core Function**: Provides end-to-end processing pipeline for CRISPR screening data from raw reads to final analysis.
- **Input/Output**: Input: FASTQ files, sample sheet, library file; Output: Processed counts, QC reports, essentiality scores, visualizations.
- **Installation**: `conda install -c bioconda mageck-vispr`
- **Snakemake Workflow**: Uses Snakemake for reproducible and scalable workflow management.
- **Integrated Tools**: Combines FastQC (QC), cutadapt (trimming), MAGeCK (analysis), and VISPR (visualization).

## Pitfalls

- **Workflow Configuration**: Incorrect configuration files cause pipeline failures.
- **Dependency Versions**: Version mismatches between tools can break the workflow.
- **Resource Allocation**: Insufficient memory/CPU allocation for large datasets.
- **Sample Sheet Format**: Incorrect sample sheet format leads to processing errors.
- **Library File Format**: Malformed library files cause counting errors.
- **Parallel Execution**: Improper parallelization settings may cause race conditions.

## Examples

### Initialize workflow
**Args:** `mageck-vispr init --name my_project`
**Explanation:** Creates new project directory structure.

### Run full pipeline
**Args:** `mageck-vispr run --snakefile Snakefile --configfile config.yaml`
**Explanation:** Executes the complete analysis pipeline.

### Run with cluster
**Args:** `mageck-vispr run --snakefile Snakefile --cluster "qsub -pe smp {threads}"`
**Explanation:** Runs pipeline on cluster using qsub.

### Generate report
**Args:** `mageck-vispr report -i results/ -o report.html`
**Explanation:** Generates HTML report of analysis results.

### Dry run
**Args:** `mageck-vispr run --snakefile Snakefile --dryrun`
**Explanation:** Shows what commands will be executed without running them.

### Restart from failed step
**Args:** `mageck-vispr run --snakefile Snakefile --restart-times 3`
**Explanation:** Attempts to restart failed steps up to 3 times.