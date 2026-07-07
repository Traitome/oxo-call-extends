---
name: kgwasflow
category: hpc
description: kGWASflow - Snakemake workflow for k-mer-based GWAS analysis.
tags: [kgwasflow, hpc, Snakemake, GWAS, k-mer, workflow]
author: oxo-call-community
source_url: "https://github.com/akcorut/kGWASflow/blob/master/README.md"
---

## Concepts

- **Tool Overview**: kgwasflow (v1.3.0) - Snakemake workflow for k-mer based GWAS.
- **k-mer GWAS**: Uses k-mer counts for genome-wide association studies.
- **Snakemake**: Implemented as Snakemake workflow for reproducibility.
- **Automation**: Automates entire GWAS pipeline.
- **Scalability**: Scales to large datasets and HPC clusters.
- **Reproducibility**: Ensures reproducible analyses.

## Pitfalls

- **Snakemake Knowledge**: Requires understanding of Snakemake.
- **Resource Requirements**: Requires significant computational resources.
- **Configuration**: Complex configuration required.
- **Input Quality**: Requires high-quality input data.
- **Memory Usage**: Large k-mer counts require memory.
- **Runtime**: Complex analyses can be time-consuming.

## Examples

### Run kGWAS workflow
**Args:** `snakemake --snakefile kgwasflow/Snakefile --configfile config.yaml --cores 16`
**Explanation:** Runs kGWAS workflow with 16 cores.

### Generate configuration
**Args:** `kgwasflow init -o config.yaml`
**Explanation:** Generates template configuration file.

### Dry run
**Args:** `snakemake --snakefile kgwasflow/Snakefile --configfile config.yaml --dryrun`
**Explanation:** Performs dry run to check workflow.

### Cluster execution
**Args:** `snakemake --snakefile kgwasflow/Snakefile --configfile config.yaml --cluster "qsub -pe smp {threads}"`
**Explanation:** Runs workflow on cluster.

### Generate report
**Args:** `snakemake --snakefile kgwasflow/Snakefile --configfile config.yaml --report report.html`
**Explanation:** Generates HTML report.

### Resume workflow
**Args:** `snakemake --snakefile kgwasflow/Snakefile --configfile config.yaml --cores 16 --resume`
**Explanation:** Resumes interrupted workflow.