---
name: cassiopeia
category: expression
description: End-to-end pipeline for single-cell lineage tracing experiments
tags: [cassiopeia, single-cell, lineage-tracing, crispr]
author: oxo-call-community
source_url: "https://github.com/YosefLab/Cassiopeia"
---

## Concepts

- **Tool Overview**: Cassiopeia is an end-to-end pipeline for single-cell lineage tracing.
- **Core Function**: Reconstructs cell lineages from CRISPR-based lineage tracing data.
- **Workflow**: Process reads → Call mutations → Reconstruct lineage tree.
- **Input**: FASTQ files from lineage tracing experiments.
- **Output**: Lineage trees and mutation character matrices.
- **Application**: Developmental biology and cancer evolution studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cassiopeia`

## Pitfalls

- **CRISPR Design**: Requires proper CRISPR lineage recorder design.
- **Sequencing Depth**: Sufficient coverage needed for accurate mutation calling.
- **Tree Reconstruction**: Different algorithms may give different topologies.
- **Python Required**: Python-based pipeline with multiple steps.

## Examples

### Process lineage tracing data
**Args:** `cassiopeia-process -i reads.fq -r reference.fa -o processed.tsv`
**Explanation:** Processes reads from lineage tracing experiment.

### Reconstruct lineage tree
**Args:** `cassiopeia-reconstruct -i character_matrix.tsv -o lineage_tree.nwk`
**Explanation:** Reconstructs cell lineage tree from mutation data.

### Display help
**Args:** `cassiopeia --help`
**Explanation:** Shows all available options and usage information.
