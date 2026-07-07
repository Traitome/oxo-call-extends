---
name: aquamis
category: assembly
description: AQUAMIS - Snakemake pipeline for routine assembly and quality assessment of microbial isolate sequencing experiments
tags: [aquamis, snakemake, microbial-assembly, quality-control, bioinformatics-pipeline]
author: oxo-call-community
source_url: "https://gitlab.com/bfr_bioinformatics/AQUAMIS"
---

## Concepts

- **Tool Overview**: AQUAMIS (v1.4.0) - A Snakemake pipeline for routine assembly and quality assessment of microbial isolate sequencing experiments.
- **Core Function**: Performs read trimming, quality control, taxonomic classification, de-novo assembly, reference identification, assembly QC, and contamination detection for microbial whole-genome sequencing data.
- **Integrated Tools**:
  - **fastp**: Read trimming and quality control
  - **shovill (Spades)**: De-novo assembly
  - **mash**: Reference search and species determination
  - **QUAST v5 (BUSCO)**: Assembly QC
  - **confindr**: Inter and intra genus contamination analysis
  - **kraken2**: Taxonomic profiling
- **Key Features**:
  - Reference-based and reference-free quality assessment
  - Species-specific QC thresholds
  - Interactive HTML report generation
  - JSON output for downstream analyses
  - High-throughput processing support
- **Input**: Paired-end FASTQ files (gzipped) from Illumina sequencing
- **Output**: Assembled contigs, quality reports, JSON results
- **Applications**: Microbial isolate sequencing analysis, routine QC, contamination detection
- **Installation**: `conda create -n aquamis -c conda-forge -c bioconda aquamis`

## Pitfalls

- **Database Requirements**: Requires reference databases installation via setup script
- **Conda Environment**: Requires proper conda environment setup with mamba
- **Resource Requirements**: High memory and CPU requirements for large datasets
- **Input Format**: Requires gzipped paired-end FASTQ files
- **Reference Database**: Needs NCBI RefSeq reference genome database for reference-based measures

## Examples

### Initialize AQUAMIS project
**Args:** `aquamis init --project-dir my_project --species "Escherichia coli"`
**Explanation:** Creates a new AQUAMIS project directory with configuration files.

### Run AQUAMIS pipeline
**Args:** `aquamis run --project-dir my_project --cores 16`
**Explanation:** Runs the complete pipeline with 16 cores for parallel processing.

### Run with custom database path
**Args:** `aquamis run --project-dir my_project --db-path /path/to/databases --cores 8`
**Explanation:** Uses custom database location instead of default.

### Setup reference databases
**Args:** `aquamis_setup.sh --install-dbs --db-path /path/to/databases`
**Explanation:** Downloads and sets up required reference databases.

### Help documentation
**Args:** `aquamis --help`
**Explanation:** Shows available commands and options.

### Create HTML report only
**Args:** `aquamis report --project-dir my_project --output report.html`
**Explanation:** Generates HTML report from existing analysis results.