---
name: scmap-cli
category: single-cell
description: scmap-cli - CLI scripts for the scmap package
tags: ["scmap-cli", "single-cell", "cell-type-mapping", "annotation"]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/scmap-cli"
---

## Concepts

- **Tool Overview**: scmap-cli (v0.1.0) provides CLI scripts for the scmap package.
- **Core Function**: Maps single-cell RNA-seq data to reference datasets for cell type annotation.
- **Algorithm**: Uses correlation-based mapping for cell type identification.
- **Input/Output**: Accepts gene expression matrices and produces cell type annotations.
- **Reference Mapping**: Enables mapping to pre-computed reference datasets.
- **Applications**: Cell type annotation, data integration, and reference-based analysis.

## Pitfalls

- **Reference Quality**: Results depend on reference dataset quality.
- **Batch Effects**: May be affected by batch effects.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Algorithm Selection**: Choosing the right algorithm requires understanding of data characteristics.

## Examples

### Basic mapping
**Args:** `scmap-cli map -i query.h5ad -r reference.h5ad -o annotations.csv`
**Explanation:** `-i` query data; `-r` reference data; `-o` annotations.

### Train reference
**Args:** `scmap-cli train -i reference.h5ad -o model.pkl`
**Explanation:** Trains scmap model on reference data.

### Load model
**Args:** `scmap-cli map -i query.h5ad -m model.pkl -o annotations.csv`
**Explanation:** Uses pre-trained model for mapping.

### Multiple queries
**Args:** `scmap-cli map -i query1.h5ad query2.h5ad -r reference.h5ad -o annotations.csv`
**Explanation:** Processes multiple query datasets.

### Verbose logging
**Args:** `scmap-cli map -i query.h5ad -r reference.h5ad -v -o annotations.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Confidence threshold
**Args:** `scmap-cli map -i query.h5ad -r reference.h5ad -c 0.8 -o annotations.csv`
**Explanation:** `-c 0.8` requires minimum confidence of 0.8.

### Output probabilities
**Args:** `scmap-cli map -i query.h5ad -r reference.h5ad --probabilities -o predictions.csv`
**Explanation:** `--probabilities` outputs mapping probabilities.