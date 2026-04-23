---
name: dockq
category: annotation
description: DockQ - A quality measure for protein, nucleic acid and small ligand docking models.
tags: [dockq, annotation, docking, protein, structure]
author: oxo-call-community
source_url: "https://github.com/bjornwallner/DockQ"
---

## Concepts

- **Tool Overview**: DockQ v2.1.3 - Quality measure for evaluating protein, nucleic acid and ligand docking models.
- **Core Function**: Scores docking predictions by comparing predicted and reference complex structures.
- **Input/Output**: Expects PDB models; outputs DockQ quality scores.
- **Installation**: `conda install -c bioconda dockq`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires PDB format structure files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dockq --model predicted.pdb --reference native.pdb`
**Explanation:** Evaluates docking model quality against reference.
