---
name: dice
category: variant-calling
description: DICE - Distance-based Inference of Copy-number Evolution for cell lineage reconstruction from single-cell CNA data.
tags: [dice, variant-calling, single-cell, cna, lineage]
author: oxo-call-community
source_url: "https://github.com/samsonweiner/DICE"
---

## Concepts

- **Tool Overview**: DICE v1.1.0 - Tool for reconstructing cell lineage trees from single-cell copy number aberration data.
- **Core Function**: Infers cell lineage relationships using distance-based methods on copy number aberration profiles.
- **Input/Output**: Expects single-cell CNA matrices; outputs lineage trees in Newick format.
- **Installation**: `conda install -c bioconda dice`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires single-cell copy number aberration data matrix.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dice --input cna_matrix.tsv --output lineage.nwk`
**Explanation:** Reconstructs cell lineage tree from CNA data.
