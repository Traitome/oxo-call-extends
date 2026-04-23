---
name: bohra
category: utility
description: Pipeline for analysing Illumina data for microbiological public health
tags: [bohra, pipeline, public-health, microbiology, illumina]
author: oxo-call-community
source_url: "https://github.com/MDU-PHL/bohra"
---

## Concepts

- **Tool Overview**: Bohra is a bioinformatics pipeline for analyzing Illumina sequencing data in public health microbiology.
- **Core Function**: Automates quality control, assembly, and typing of bacterial isolates.
- **Pipeline Steps**: Read QC, assembly, MLST typing, and species identification.
- **Workflow Manager**: Built on Nextflow for reproducible and scalable analysis.
- **Input**: Illumina paired-end FASTQ files.
- **Installation**: Install via bioconda: `conda install -c bioconda bohra`

## Pitfalls

- **Container Required**: Best run with Docker or Singularity for reproducibility.
- **Database Setup**: Requires MLST and other databases to be available.
- **Sample Naming**: Follow naming conventions for proper sample handling.
- **Resource Requirements**: Assembly step requires significant memory for large genomes.

## Examples

### Run full pipeline
**Args:** `bohra --input samples/ --outdir results/`
**Explanation:** Runs complete analysis pipeline on all samples in input directory.

### Run with specific samples
**Args:** `bohra --input samples/ --samples sample1,sample2 --outdir results/`
**Explanation:** Processes only specified samples from the input directory.

### Run with containers
**Args:** `bohra --input samples/ --outdir results/ --use-singularity`
**Explanation:** Uses Singularity containers for reproducible execution.

### Skip assembly step
**Args:** `bohra --input samples/ --outdir results/ --skip-assembly`
**Explanation:** Skips genome assembly and performs only QC and typing.

### Display help
**Args:** `--help`
**Explanation:** Shows all available pipeline options and parameters.
