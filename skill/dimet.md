---
name: dimet
category: metabolomics
description: DIMET - Differential analysis of metabolomics data.
tags: [dimet, metabolomics, differential-analysis, statistics]
author: oxo-call-community
source_url: "https://github.com/computational-metabolomics/dimet"
---

## Concepts

- **Tool Overview**: dimet is a tool for differential analysis of metabolomics data, enabling comparison between experimental conditions.
- **Core Function**: Performs statistical differential analysis on metabolomics datasets to identify metabolites with significant abundance differences.
- **Input/Output**: Input: Metabolomics abundance table, sample metadata. Output: Differential metabolite results with statistics.
- **Algorithm**: Uses statistical tests (t-test, ANOVA, etc.) to compare metabolite abundances between groups.
- **Key Features**: Multiple statistical methods, normalization support, missing value handling, visualization, FDR correction.
- **Installation**: `conda install -c bioconda dimet`

## Pitfalls

- **Input Requirements**: Requires properly formatted metabolomics data matrix.
- **Normalization**: Data must be appropriately normalized before analysis.
- **Missing Values**: Requires handling of missing metabolite measurements.
- **Sample Size**: Requires sufficient biological replicates for statistical power.
- **Multiple Testing**: Must apply multiple testing correction to avoid false positives.

## Examples

### Perform differential analysis
**Args:** `dimet --input metabolites.tsv --output diff_results.tsv`
**Explanation:** Performs differential analysis on metabolomics data.

### With group information
**Args:** `dimet --input metabolites.tsv --groups groups.tsv --output diff_results.tsv`
**Explanation:** Specify sample group assignments for comparison.

### Use specific test
**Args:** `dimet --input metabolites.tsv --output diff_results.tsv --test ttest`
**Explanation:** Use t-test for differential analysis.

### Handle missing values
**Args:** `dimet --input metabolites.tsv --output diff_results.tsv --impute knn`
**Explanation:** Use k-NN imputation for missing values.

### Generate volcano plot
**Args:** `dimet --input metabolites.tsv --output diff_results.tsv --volcano volcano.png`
**Explanation:** Generate volcano plot of differential results.