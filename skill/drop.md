---
name: drop
category: programming
description: "Detection of RNA Outlier Pipeline"
tags: [drop, programming, RNA-outlier, gene-expression, rare-disease]
author: oxo-call-community
source_url: "https://gagneurlab-drop.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: DROP (Detection of RNA Outlier Pipeline) is a computational pipeline for detecting aberrant gene expression in RNA-seq data.
- **Core Function**: Identifies genes with significantly abnormal expression levels that may indicate disease-causing mutations.
- **Input/Output**: Input: Gene expression matrix, phenotype data. Output: Outlier gene calls, significance scores.
- **Algorithm**: Uses statistical modeling to identify expression outliers across samples.
- **Key Features**: Multiple outlier detection methods, batch correction, prioritization of candidate genes, visualization tools.
- **Installation**: `conda install -c bioconda drop`

## Pitfalls

- **Sample Size**: Requires sufficient sample size for robust statistical testing.
- **Normalization**: Proper normalization is critical for accurate outlier detection.
- **Batch Effects**: Batch variation can produce false positive outlier calls.
- **Multiple Testing**: Requires correction for multiple hypothesis testing.
- **Gene Filtering**: Lowly expressed genes should be filtered before analysis.

## Examples

### Basic outlier detection
**Args:** `--input counts.csv --output outliers.txt`
**Explanation:** Detects expression outliers in RNA-seq data.

### With phenotype data
**Args:** `--input counts.csv --pheno pheno.txt --output outliers.txt`
**Explanation:** Incorporates phenotype information for conditional outlier detection.

### Batch correction
**Args:** `--input counts.csv --batch batch.txt --output outliers.txt`
**Explanation:** Corrects for batch effects before outlier detection.

### Multiple methods
**Args:** `--input counts.csv --output outliers.txt --methods zscore mad`
**Explanation:** Uses multiple outlier detection methods (Z-score and MAD).

### Generate report
**Args:** `--input counts.csv --output outliers.txt --report report.html`
**Explanation:** Generates HTML report with outlier analysis results.