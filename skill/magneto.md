---
name: magneto
category: metagenomics
description: MAGNETO is an automated snakemake workflow dedicated to MAG reconstruction from metagenomic data.
tags: [magneto, metagenomics, MAGs, snakemake]
author: oxo-call-community
source_url: "https://gitlab.univ-nantes.fr/bird_pipeline_registry/magneto"
---

## Concepts

- **Tool Overview**: magneto v1.5.2 - MAGNETO is an automated Snakemake workflow for reconstructing Metagenome-Assembled Genomes (MAGs) from metagenomic sequencing data.
- **Core Function**: Provides end-to-end pipeline for quality control, assembly, binning, and MAG refinement.
- **Input/Output**: Input: Raw sequencing reads (FASTQ), metadata; Output: Assembled contigs, MAG bins, quality reports.
- **Installation**: `conda install -c bioconda magneto`
- **Snakemake Workflow**: Uses Snakemake for reproducible and scalable workflow management.
- **Integrated Tools**: Combines FastQC, SPAdes, MetaBAT2, CheckM, and other tools.

## Pitfalls

- **Workflow Configuration**: Incorrect configuration files cause pipeline failures.
- **Resource Allocation**: Insufficient memory/CPU for assembly steps.
- **Read Quality**: Poor quality reads affect assembly quality.
- **Contamination**: Host or adapter contamination impacts MAG quality.
- **Dependency Versions**: Version mismatches between tools can break workflow.
- **Storage Requirements**: Large intermediate files require significant disk space.

## Examples

### Initialize workflow
**Args:** `magneto init --name my_project`
**Explanation:** Creates new project directory structure.

### Run full pipeline
**Args:** `magneto run --configfile config.yaml`
**Explanation:** Executes complete MAG reconstruction pipeline.

### Run on cluster
**Args:** `magneto run --configfile config.yaml --cluster "sbatch --mem 32G"`
**Explanation:** Runs pipeline on cluster with Slurm.

### Dry run
**Args:** `magneto run --configfile config.yaml --dryrun`
**Explanation:** Shows commands without executing them.

### Generate report
**Args:** `magneto report -i results/ -o report.html`
**Explanation:** Generates HTML report of MAG reconstruction.

### Restart from checkpoint
**Args:** `magneto run --configfile config.yaml --restart-times 2`
**Explanation:** Restarts failed steps up to 2 times.