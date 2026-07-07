---
name: sccellfie
category: expression
description: scCellFie - Inferring metabolic activities from single-cell and spatial transcriptomics
tags: ["sccellfie", "expression", "metabolic", "single-cell"]
author: oxo-call-community
source_url: "https://github.com/earmingol/scCellFie"
---

## Concepts

- **Tool Overview**: scCellFie (v0.5.0) is a tool for inferring metabolic activities from single-cell and spatial transcriptomics data.
- **Core Function**: Predicts metabolic pathway activities from gene expression profiles.
- **Algorithm**: Uses constraint-based modeling to infer metabolic activity.
- **Input/Output**: Accepts gene expression data and produces metabolic activity scores.
- **Multi-omics Support**: Works with both single-cell and spatial transcriptomics data.
- **Applications**: Metabolic analysis, cell type characterization, and spatial metabolomics.

## Pitfalls

- **Gene Coverage**: Requires comprehensive gene expression coverage.
- **Pathway Databases**: Results depend on pathway database completeness.
- **Normalization**: Requires proper data normalization.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Biological Interpretation**: Metabolic inference requires biological validation.

## Examples

### Basic metabolic inference
**Args:** `sccellfie -i expression.h5ad -o metabolic_scores.csv`
**Explanation:** `-i` input gene expression; `-o` metabolic activity scores.

### With spatial data
**Args:** `sccellfie -i spatial_data.h5ad -s -o metabolic_scores.csv`
**Explanation:** `-s` enables spatial transcriptomics mode.

### Pathway analysis
**Args:** `sccellfie -i expression.h5ad -p pathways.gmt -o scores.csv`
**Explanation:** `-p` specifies custom pathway database.

### Visualize results
**Args:** `sccellfie -i expression.h5ad --plot -o plot.png`
**Explanation:** Generates visualization of metabolic activities.

### Multiple conditions
**Args:** `sccellfie -i condition1.h5ad condition2.h5ad -o comparison.csv`
**Explanation:** Compares metabolic activities across conditions.

### Verbose logging
**Args:** `sccellfie -i expression.h5ad -v -o scores.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Output JSON
**Args:** `sccellfie -i expression.h5ad -f json -o scores.json`
**Explanation:** `-f json` outputs results in JSON format.