---
name: dmox
category: annotation
description: DMOX - Drug Metabolism and Oxidation prediction.
tags: [dmox, annotation, drug-metabolism, oxidation, prediction]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DMOX - Tool for predicting drug metabolism and oxidation sites.
- **Core Function**: Predicts metabolic oxidation sites and drug metabolism pathways.
- **Input/Output**: Expects molecular structures (SMILES/SDF); outputs predicted metabolism sites.
- **Installation**: `conda install -c bioconda dmox`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires molecular structure data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dmox --input molecule.smi --output metabolism.tsv`
**Explanation:** Predicts drug metabolism and oxidation sites.
