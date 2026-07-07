---
name: milonga
category: assembly
description: MiLongA - A snakemake workflow for Microbial Long-read Assembly
tags: [milonga, assembly, snakemake]
author: oxo-call-community
source_url: "https://gitlab.com/bfr_bioinformatics/milonga"
---

## Concepts

- **Tool Overview**: MiLongA v1.0.3 is a Snakemake workflow for microbial long-read assembly.
- **Core Function**: Assembles microbial genomes from long-read sequencing data.
- **Snakemake Workflow**: Implemented as a Snakemake pipeline for reproducibility.
- **Long-read Assembly**: Optimized for PacBio and Oxford Nanopore reads.
- **Input/Output**: Accepts long-read sequences; outputs assembled genomes.
- **Microbial Genomics**: Specialized for microbial genome assembly.

## Pitfalls

- **Snakemake Dependency**: Requires Snakemake workflow management.
- **Computational Resources**: Assembly requires significant computational resources.
- **Memory Requirements**: Memory usage can be high for large genomes.
- **Parameter Tuning**: May require parameter adjustment for optimal assembly.
- **Data Quality**: Assembly quality depends on input read quality.
- **Runtime**: Assembly of large genomes can be time-consuming.

## Examples

### Run MiLongA workflow
**Args:** `snakemake --use-conda --cores 8`
**Explanation:** Runs the MiLongA assembly workflow.

### With custom configuration
**Args:** `snakemake --use-conda --cores 8 --configfile config.yaml`
**Explanation:** Uses custom configuration file.

### Dry run
**Args:** `snakemake --use-conda --dryrun`
**Explanation:** Performs dry run to check workflow.

### Resume interrupted run
**Args:** `snakemake --use-conda --cores 8 --resume`
**Explanation:** Resumes interrupted workflow.

### Generate DAG
**Args:** `snakemake --dag | dot -Tpng > dag.png`
**Explanation:** Generates workflow visualization.