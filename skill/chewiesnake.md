---
name: chewiesnake
category: workflow
description: Snakemake workflow for cgMLST allele calling using chewBBACA
tags: [chewiesnake, snakemake, cgmlst, allele-calling, workflow, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.com/bfr_bioinformatics/chewieSnake"
---

## Concepts

- **Tool Overview**: ChewieSnake is a Snakemake workflow that automates cgMLST allele calling for assembled genomes using chewBBACA.
- **Core Function**: Provides a reproducible pipeline for allele calling, quality control, and result aggregation.
- **Features**: Automated workflow management, parallel processing, quality control, and result visualization.
- **Input**: Assembled genome FASTA files and optional chewBBACA schema.
- **Output**: Allele calls, QC reports, and summary statistics.
- **Application**: High-throughput bacterial strain typing and epidemiological analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda chewiesnake`

## Pitfalls

- **Workflow Setup**: Requires proper configuration file setup.
- **Dependency Management**: Depends on chewBBACA and Snakemake.
- **Schema Requirements**: Needs existing chewBBACA schema or reference genomes.
- **Computational Resources**: May require cluster environment for large datasets.
- **Configuration Errors**: Incorrect config may cause workflow failures.

## Examples

### Run workflow
**Args:** `snakemake --snakefile /path/to/chewieSnake/Snakefile -j 8 --configfile config.yaml`
**Explanation:** Runs ChewieSnake workflow with 8 parallel jobs.

### Generate config
**Args:** `chewieSnake init -o config.yaml`
**Explanation:** Generates template configuration file.

### Dry run
**Args:** `snakemake --snakefile Snakefile -n`
**Explanation:** Performs dry run to check workflow.

### Cluster execution
**Args:** `snakemake --snakefile Snakefile --cluster "qsub -pe smp {threads}" -j 32`
**Explanation:** Runs workflow on cluster with job scheduling.