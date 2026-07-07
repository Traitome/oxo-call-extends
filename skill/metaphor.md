---
name: metaphor
category: assembly
description: Metaphor - Metagenomic Pipeline for Short Reads
tags: [metaphor, assembly, metagenomics, snakemake]
author: oxo-call-community
source_url: "https://github.com/vinisalazar/metaphor"
---

## Concepts

- **Tool Overview**: Metaphor v1.7.14 is a Snakemake-based workflow for assembly and binning of metagenomic short reads.
- **Core Function**: Provides a complete pipeline for metagenomic assembly, binning, and downstream analysis.
- **Snakemake Workflow**: Implemented as a Snakemake workflow for reproducibility and scalability.
- **Multi-step Processing**: Includes quality control, assembly, binning, and annotation steps.
- **Input/Output**: Accepts raw FASTQ sequencing reads; outputs assembled contigs, bins, and analysis reports.
- **Configurable**: Highly configurable with support for various assembly and binning tools.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Configuration Complexity**: Requires careful configuration for optimal performance.
- **Dependency Management**: Requires proper management of multiple dependencies.
- **Runtime**: Complete analysis of large datasets can be time-consuming.
- **Storage Requirements**: Intermediate files can require substantial storage space.
- **Parameter Tuning**: May require parameter adjustment for optimal results.

## Examples

### Initialize pipeline
**Args:** `metaphor init --input fastq/ --output results/`
**Explanation:** Initializes the Metaphor pipeline with input FASTQ files.

### Run complete workflow
**Args:** `metaphor run`
**Explanation:** Runs the complete metagenomic assembly and binning workflow.

### Run specific step
**Args:** `metaphor run assembly`
**Explanation:** Runs only the assembly step of the pipeline.

### Configure for cluster
**Args:** `metaphor run --profile cluster`
**Explanation:** Runs the pipeline on a cluster system using predefined profile.

### Generate report
**Args:** `metaphor run report`
**Explanation:** Generates a comprehensive HTML report of analysis results.