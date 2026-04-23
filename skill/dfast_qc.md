---
name: dfast_qc
category: qc
description: DFAST_QC - Taxonomy and completeness check for prokaryotic genomes.
tags: [dfast_qc, qc, taxonomy, completeness, prokaryote]
author: oxo-call-community
source_url: "https://github.com/nigyta/dfast_qc"
---

## Concepts

- **Tool Overview**: DFAST_QC v1.1.1 - Quality control tool for checking taxonomy and completeness of prokaryotic genomes.
- **Core Function**: Verifies taxonomic assignment and assesses genome completeness using marker gene analysis.
- **Input/Output**: Expects genome FASTA files; outputs taxonomy reports and completeness metrics.
- **Installation**: `conda install -c bioconda dfast_qc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires assembled genome in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dfast_qc --genome assembly.fa --output qc_report/`
**Explanation:** Checks taxonomy and completeness of prokaryotic genome.
