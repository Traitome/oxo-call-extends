---
name: genecircuitry
category: expression
description: GeneCircuitry - Transcriptional Regulatory Network (TRN) analysis from single-cell data using Scanpy, CellOracle, and Hotspot.
tags: [genecircuitry, single-cell, trn, gene-regulatory-network]
author: oxo-call-community
source_url: "https://github.com/samuelecancellieri/genecircuitry/blob/main/README.md"
---

## Concepts
- **Single-cell Analysis**: Analyzes single-cell RNA sequencing data.
- **Regulatory Network**: Constructs transcriptional regulatory networks.
- **Scanpy Integration**: Integrates with Scanpy for preprocessing.
- **CellOracle**: Uses CellOracle for GRN inference.
- **Hotspot**: Identifies co-expression modules.

## Pitfalls
- **Data Quality**: Requires high-quality single-cell data.
- **Computational Resources**: Large datasets require significant resources.
- **Memory Usage**: Single-cell analysis can be memory-intensive.
- **Parameter Tuning**: Network inference parameters need careful adjustment.
- **Interpretation**: Network results require careful biological interpretation.

## Examples
### Analyze single-cell data
**Args:** `genecircuitry analyze -i anndata.h5ad -o results/`
**Explanation:** Performs comprehensive TRN analysis on single-cell data.

### Build regulatory network
**Args:** `genecircuitry network -i anndata.h5ad -o network.pkl`
**Explanation:** Constructs transcriptional regulatory network.

### Identify modules
**Args:** `genecircuitry modules -i anndata.h5ad -o modules.csv`
**Explanation:** Identifies co-expression modules using Hotspot.

### Visualize network
**Args:** `genecircuitry plot -i network.pkl -o network_plot.png`
**Explanation:** Generates visualization of regulatory network.

### Differential analysis
**Args:** `genecircuitry diff -i anndata.h5ad -c cell_type -o diff_results.csv`
**Explanation:** Performs differential network analysis between cell types.