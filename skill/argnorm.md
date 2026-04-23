---
name: argnorm
category: metagenomics
description: Normalize antibiotic resistance genes (ARGs) abundance tables (e.g., from metagenomics) by using the ARO ontology (developed by CARD).
tags: [argnorm, metagenomics]
author: oxo-call-community
source_url: "https://argnorm.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: argnorm (v1.1.0) - Normalize antibiotic resistance genes (ARGs) abundance tables (e.g., from metagenomics) by using the ARO ontology (developed by CARD).
- **Core Function**: Normalize antibiotic resistance genes (ARGs) abundance tables (e.g., from metagenomics) by using the ARO ontology (developed by CARD).
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda argnorm`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i contigs.fasta -o bins_dir`
**Explanation:** Perform metagenomic analysis
