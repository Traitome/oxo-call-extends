---
name: maaslin3
category: qc
description: Refining and extending generalized multivariate linear models for meta-omic association discovery
tags: [maaslin3, qc, metagenomics, statistics]
author: oxo-call-community
source_url: "https://github.com/biobakery/maaslin3"
---

## Concepts

- **Tool Overview**: maaslin3 v0.99.16 is a statistical framework for finding associations between microbiome features and metadata.
- **Core Function**: Uses generalized multivariate linear models to identify associations in meta-omic data.
- **Statistical Methods**: Supports multiple covariates, repeated measures, and ordered predictors.
- **Input/Output**: Input: Feature abundance table, metadata table; Output: Association results with statistics.
- **Installation**: `conda install -c bioconda maaslin3`
- **Key Features**: Multiple normalization options, filtering capabilities, support for complex study designs.

## Pitfalls

- **Data Quality**: Requires high-quality metadata and feature tables.
- **Multiple Testing**: Requires careful handling of multiple testing corrections.
- **Model Selection**: Choosing appropriate models requires statistical expertise.
- **Missing Data**: May require imputation for missing values.
- **Computation Time**: Processing large datasets can be time-consuming.
- **Interpretation**: Results require careful interpretation by domain experts.

## Examples

### Run MaAsLin3 analysis
**Args:** `maaslin3 --input features.tsv --metadata metadata.tsv --output results/`
**Explanation:** Runs association analysis on features and metadata.

### With covariates
**Args:** `maaslin3 --input features.tsv --metadata metadata.tsv --fixed effects age,gender --output results/`
**Explanation:** Includes fixed effects covariates in the model.

### Repeated measures
**Args:** `maaslin3 --input features.tsv --metadata metadata.tsv --random effects subject_id --output results/`
**Explanation:** Handles repeated measures with random effects.

### Normalization
**Args:** `maaslin3 --input features.tsv --metadata metadata.tsv --normalization TSS --output results/`
**Explanation:** Uses TSS normalization for feature counts.

### Filtering
**Args:** `maaslin3 --input features.tsv --metadata metadata.tsv --min_prevalence 0.1 --output results/`
**Explanation:** Filters features with prevalence < 10%.

### Help documentation
**Args:** `maaslin3 --help`
**Explanation:** Displays all available options and parameters.