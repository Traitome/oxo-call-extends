---
name: dligand2
category: annotation
description: Tool for ligand binding site prediction.
tags: [dligand2, annotation, ligand, binding-site, protein]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: dligand2 - Tool for predicting ligand binding sites in protein structures.
- **Core Function**: Identifies potential ligand binding pockets in protein 3D structures.
- **Input/Output**: Expects PDB structures; outputs predicted binding sites with coordinates.
- **Installation**: `conda install -c bioconda dligand2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires protein structure in PDB format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dligand2 --input protein.pdb --output binding_sites.tsv`
**Explanation:** Predicts ligand binding sites in protein structure.
