---
name: liana
category: single-cell
description: LIANA+ - comprehensive framework for cell-cell communication analysis
tags: [liana, single-cell, cell-cell-communication, scRNA-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/saezlab/liana-py"
---

## Concepts

- **Cell-Cell Communication**: Analyzes intercellular signaling from scRNA-seq data
- **Multi-method Integration**: Combines multiple inference methods
- **Ligand-Receptor Pairs**: Identifies ligand-receptor interactions
- **Single-cell Analysis**: Works with single-cell RNA sequencing data
- **Signaling Pathways**: Maps communication through signaling pathways
- **Visualization**: Provides visualization of communication networks

## Pitfalls

- **Data Quality**: Poor quality scRNA-seq data affects results
- **Dropout Events**: RNA dropout affects gene expression estimates
- **Cell Type Annotation**: Incorrect cell type annotations mislead results
- **Database Coverage**: Limited ligand-receptor databases
- **False Positives**: Multiple testing correction essential
- **Expression Thresholds**: Threshold selection affects detection

## Examples

### Run LIANA analysis
**Args:** `liana -i counts.h5ad -o results/`
**Explanation:** Performs cell-cell communication analysis.

### Specify cell type column
**Args:** `liana -i counts.h5ad -c cell_type -o results/`
**Explanation:** Uses specific column for cell type annotation.

### Multiple methods
**Args:** `liana -i counts.h5ad -m cellphonedb,natmi,iceberg -o results/`
**Explanation:** Uses multiple inference methods.

### Filter by p-value
**Args:** `liana -i counts.h5ad -p 0.05 -o results/`
**Explanation:** Filters results by p-value threshold.

### Generate visualization
**Args:** `liana plot -i results/ -o plot.pdf`
**Explanation:** Creates visualization of communication network.

### Batch mode
**Args:** `liana batch -d datasets/ -o results/`
**Explanation:** Processes multiple datasets.