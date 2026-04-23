---
name: mvip
category: metagenomics
description: MVP pipeline for standard viromics analyses combining multiple tools for viral genome identification, annotation, and binning.
tags: [mvip, metagenomics, viromics, viral, annotation]
author: oxo-call-community
source_url: "https://gitlab.com/ccoclet/mvp"
---

## Concepts

- **Tool Overview**: MVP v1.1.5 - user-friendly viromics pipeline for viral genome identification, characterization, clustering, annotation, and binning.
- **Core Function**: Provides standardized and reproducible pipeline for characterization of viruses from large-scale sequencing data.
- **Input/Output**: Takes metagenomic/metatranscriptomic/virome assemblies; outputs annotated viral genomes with comprehensive summaries.
- **Installation**: `conda install -c bioconda mvip`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires pre-assembled contigs from metagenomic or virome data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i contigs.fasta -o output_dir`
**Explanation:** Runs the MVP viromics pipeline on input contigs.
