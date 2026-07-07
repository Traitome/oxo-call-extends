---
name: cell2cell
category: single-cell
description: Inferring cell-cell interactions from transcriptomic data
tags: [cell2cell, single-cell, cell-cell-interaction, transcriptomics, ligand-receptor]
author: oxo-call-community
source_url: "https://github.com/earmingol/cell2cell"
---

## Concepts

- **Tool Overview**: cell2cell infers cell-cell interactions from single-cell transcriptomic data.
- **Core Function**: Predicts ligand-receptor interactions between cell types.
- **Algorithm**: Uses ligand-receptor databases to predict potential cell-cell communication.
- **Input**: Single-cell RNA-seq expression matrix and cell type annotations.
- **Output**: Cell-cell interaction networks and communication scores.
- **Application**: Understanding cellular communication in tissues and tumors.
- **Installation**: Install via bioconda: `conda install -c bioconda cell2cell`

## Pitfalls

- **Database Dependencies**: Relies on ligand-receptor interaction databases.
- **Expression Thresholds**: Lowly expressed genes may affect predictions.
- **Cell Type Annotation**: Requires accurate cell type labels.
- **False Positives**: May predict non-functional interactions.

## Examples

### Infer cell-cell interactions
**Args:** `cell2cell infer -i expression.h5ad -c cell_types.tsv -o interactions/`
**Explanation:** Infers cell-cell interactions from single-cell data.

### Use custom ligand-receptor database
**Args:** `cell2cell infer -i data.h5ad -d custom_lr_db.tsv -o results/`
**Explanation:** Uses custom ligand-receptor database for inference.

### Visualize interactions
**Args:** `cell2cell plot -i interactions.tsv -o network.png`
**Explanation:** Visualizes cell-cell interaction network.

### Display help
**Args:** `cell2cell --help`
**Explanation:** Shows all available options and usage information.