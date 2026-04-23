---
name: bactopia
category: assembly
description: Bactopia - Flexible pipeline for complete analysis of bacterial genomes
tags: [bacterial-genomics, pipeline, assembly, annotation, nextflow]
author: oxo-call-community
source_url: "https://github.com/bactopia/bactopia"
---

## Concepts

- **Tool Overview**: Bactopia is a comprehensive Nextflow-based pipeline for complete bacterial genome analysis, from raw reads through assembly, annotation, and comparative genomics.

- **Three-Part Pipeline**: Bactopia consists of Bactopia Tools (individual analyses), Bactopia Datasets (reference data), and Bactopia Build (complete pipeline).

- **Multiple Input Types**: Accepts raw reads (Illumina, Nanopore, PacBio), assemblies, or accession numbers from public databases.

- **Quality Control**: Includes comprehensive QC with FastQC, fastp, and custom quality metrics.

- **Assembly Options**: Supports multiple assemblers including Shovill, Unicycler, and hybrid assembly approaches.

- **Annotation**: Provides automated annotation with Prokka and custom functional annotation.

## Pitfalls

- **Nextflow Requirement**: Requires Nextflow and appropriate execution environment (Docker/Singularity/Conda).

- **Resource Intensive**: Full pipeline requires significant CPU and memory. Adjust based on available resources.

- **Database Downloads**: Reference datasets can be large. Pre-download using bactopia-datasets.

- **Sample Sheet Format**: Requires properly formatted sample sheet. Incorrect format causes pipeline failures.

## Examples

### Basic pipeline run
**Args:** `bactopia --accession SRR123456 --out-dir results/`
**Explanation:** Downloads and processes SRA accession through complete Bactopia pipeline.

### Run from local reads
**Args:** `bactopia --samples samples.tsv --out-dir results/`
**Explanation:** Processes local samples defined in sample sheet through complete pipeline.

### Run with specific assembler
**Args:** `bactopia --samples samples.tsv --assembler unicycler --out-dir results/`
**Explanation:** Uses Unicycler assembler instead of default Shovill for better hybrid assemblies.

### Run Bactopia Tools individually
**Args:** `bactopia-tools staphopia-saureus --bactopia-dir results/ --out-dir saureus_results/`
**Explanation:** Runs specific Bactopia Tool for S. aureus analysis on completed pipeline results.

### Download reference datasets
**Args:** `bactopia-datasets --species "Staphylococcus aureus" --out-dir datasets/`
**Explanation:** Downloads reference datasets for S. aureus for use in comparative analysis.

### Custom parameters
**Args:** `bactopia --samples samples.tsv --max_cpus 16 --max_memory 64 --out-dir results/`
**Explanation:** Limits resource usage to 16 CPUs and 64GB RAM maximum.
