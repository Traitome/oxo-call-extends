---
name: chromimpute
category: epigenomics
description: Large-scale systematic epigenome imputation software
tags: [chromimpute, epigenomics, imputation, chip-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jernst98/ChromImpute"
---

## Concepts

- **Tool Overview**: ChromImpute performs large-scale systematic epigenome imputation to predict missing epigenetic data across samples.
- **Core Function**: Imputes missing ChIP-seq data using correlations between marks and across samples.
- **Algorithm**: Uses random forests and matrix completion to predict missing epigenetic marks from existing data.
- **Input**: Matrix of epigenetic signals across samples and marks.
- **Output**: Imputed epigenetic data for missing marks/samples.
- **Application**: Epigenomic data integration, filling missing data, and generating complete epigenomic profiles.
- **Installation**: Install via bioconda: `conda install -c bioconda chromimpute`

## Pitfalls

- **Data Coverage**: Requires sufficient coverage across samples and marks for accurate imputation.
- **Correlation Assumption**: Assumes correlations between marks are consistent across samples.
- **Computational Time**: May be computationally intensive for large datasets.
- **Memory Usage**: Requires significant memory for large epigenomic datasets.
- **Validation**: Imputed data should be validated with experimental data when possible.

## Examples

### Run imputation
**Args:** `ChromImpute -i input_matrix.txt -o imputed_output/`
**Explanation:** Runs epigenome imputation on input matrix.

### With cross-validation
**Args:** `ChromImpute -i input_matrix.txt -o imputed_output/ --cv`
**Explanation:** Performs cross-validation during imputation.

### Specify marks
**Args:** `ChromImpute -i input_matrix.txt -m marks.txt -o imputed_output/`
**Explanation:** Specifies which marks to impute.

### Display help
**Args:** `ChromImpute --help`
**Explanation:** Shows all available options and usage information.