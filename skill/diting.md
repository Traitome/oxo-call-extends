---
name: diting
category: metagenomics
description: DiTing - Snakemake pipeline for biogeochemical pathway inference in metagenomics.
tags: [diting, metagenomics, pathways, biogeochemical, snakemake]
author: oxo-call-community
source_url: "https://github.com/SilentGene/DiTing"
---

## Concepts

- **Tool Overview**: DiTing (v2.0.2+) is a Snakemake-based pipeline for inferring biogeochemical pathways from metagenomic data.
- **Core Function**: Identifies and compares metabolic pathways and biogeochemical cycles in metagenomic samples.
- **Input/Output**: Input: Metagenomic assemblies, gene annotations. Output: Pathway abundance, comparison results, visualization.
- **Algorithm**: Uses functional annotation and pathway databases to identify pathway presence/abundance.
- **Key Features**: Biogeochemical pathway analysis, functional annotation, pathway comparison, visualization, Snakemake workflow.
- **Installation**: `conda install -c bioconda diting`

## Pitfalls

- **Input Requirements**: Requires assembled contigs and gene annotations.
- **Annotation Quality**: Depends on gene annotation completeness.
- **Database Version**: Pathway database version affects results.
- **Computational Resources**: May require significant resources for large datasets.
- **Snakemake Knowledge**: Requires basic Snakemake understanding.

## Examples

### Run pathway analysis
**Args:** `diting run --config config.yaml --output results/`
**Explanation:** Runs biogeochemical pathway analysis pipeline.

### With custom database
**Args:** `diting run --config config.yaml --output results/ --database custom_db/`
**Explanation:** Use custom pathway database.

### Compare samples
**Args:** `diting run --config config.yaml --output results/ --compare`
**Explanation:** Compare pathway abundances between samples.

### Generate visualization
**Args:** `diting run --config config.yaml --output results/ --visualize`
**Explanation:** Generate pathway visualization.

### Resuming pipeline
**Args:** `diting run --config config.yaml --output results/ --resume`
**Explanation:** Resume interrupted pipeline run.