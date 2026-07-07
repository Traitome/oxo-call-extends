---
name: metagenome-atlas
category: alignment
description: ATLAS - Three commands to start analysing your metagenome data
tags: [metagenome-atlas, alignment, metagenomics, pipeline]
author: oxo-call-community
source_url: "https://github.com/metagenome-atlas"
---

## Concepts

- **Tool Overview**: ATLAS v19.0.1 is an easy-to-use metagenomic pipeline that simplifies metagenome data analysis with three simple commands.
- **Core Function**: Provides a complete metagenomic analysis workflow from raw reads to annotated results.
- **Three-Step Workflow**: init → run → analyze with automated database installation.
- **On-the-fly Installation**: Automatically installs required databases and dependencies.
- **Input/Output**: Accepts raw FASTQ sequencing reads; outputs comprehensive analysis results including assemblies, annotations, and reports.
- **Cluster Support**: Designed to run on cluster systems with configurable parallel processing.

## Pitfalls

- **Database Download**: Initial database installation can be time-consuming.
- **Configuration**: Requires careful configuration for optimal performance.
- **Resource Requirements**: Large datasets may require significant computational resources.
- **Storage Requirements**: Databases and intermediate files require substantial storage space.
- **Dependency Conflicts**: May encounter dependency conflicts with existing environment.
- **Runtime**: Complete analysis of large datasets can be time-consuming.

## Examples

### Initialize pipeline
**Args:** `atlas init --db-dir databases path/to/fastq/files`
**Explanation:** Initializes the ATLAS pipeline with input FASTQ files and database directory.

### Run complete analysis
**Args:** `atlas run`
**Explanation:** Runs the complete metagenomic analysis pipeline.

### Run specific step
**Args:** `atlas run assembly`
**Explanation:** Runs only the assembly step of the pipeline.

### Configure for cluster
**Args:** `atlas run --profile cluster`
**Explanation:** Runs the pipeline on a cluster system using predefined profile.

### Generate report
**Args:** `atlas run report`
**Explanation:** Generates a comprehensive HTML report of analysis results.