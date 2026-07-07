---
name: dice
category: variant-calling
description: DICE - Distance-based inference of copy-number evolution for cell lineage reconstruction.
tags: [dice, variant-calling, single-cell, cna, lineage]
author: oxo-call-community
source_url: "https://github.com/samsonweiner/DICE"
---

## Concepts

- **Tool Overview**: dice (v1.1.0+) is a tool for reconstructing cell lineage trees from single-cell copy number aberration (CNA) data.
- **Core Function**: Infers cell lineage relationships using distance-based methods on copy number aberration profiles.
- **Input/Output**: Input: Single-cell CNA matrix (rows=cells, columns=genomic regions). Output: Lineage tree in Newick format, visualization.
- **Algorithm**: Uses distance matrix construction and phylogenetic tree inference for lineage reconstruction.
- **Key Features**: Single-cell CNA analysis, lineage tree reconstruction, distance-based methods, visualization support, multiple tree formats.
- **Installation**: `conda install -c bioconda dice`

## Pitfalls

- **Input Requirements**: Requires single-cell copy number aberration data matrix.
- **Data Quality**: Results depend on CNA calling quality and coverage.
- **Cell Number**: May struggle with very large number of cells.
- **Memory Usage**: May require significant memory for large datasets.
- **Parameter Sensitivity**: Tree topology may be sensitive to distance metric choice.

## Examples

### Reconstruct lineage tree
**Args:** `dice --input cna_matrix.tsv --output lineage.nwk`
**Explanation:** Reconstructs cell lineage tree from CNA data.

### With custom distance metric
**Args:** `dice --input cna_matrix.tsv --output lineage.nwk --distance cosine`
**Explanation:** Use cosine distance metric instead of default.

### Generate visualization
**Args:** `dice --input cna_matrix.tsv --output lineage.nwk --plot tree.png`
**Explanation:** Generate visualization of lineage tree.

### Bootstrap support values
**Args:** `dice --input cna_matrix.tsv --output lineage.nwk --bootstrap 100`
**Explanation:** Calculate bootstrap support values with 100 replicates.

### Output in Nexus format
**Args:** `dice --input cna_matrix.tsv --output lineage.nex --format nexus`
**Explanation:** Output lineage tree in Nexus format.