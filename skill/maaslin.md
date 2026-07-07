---
name: maaslin
category: metagenomics
description: MaAsLin is a multivariate statistical framework that finds associations between clinical metadata and microbial community abundance or function.
tags: [maaslin, metagenomics, statistics]
author: oxo-call-community
source_url: "https://huttenhower.sph.harvard.edu/maaslin"
---

## Concepts

- **Tool Overview**: maaslin v0.05 is a multivariate statistical framework for finding associations in microbiome data.
- **Core Function**: Identifies associations between microbial community features and clinical metadata.
- **Statistical Framework**: Uses generalized linear models for association testing.
- **Input/Output**: Input: OTU table, metadata file; Output: Association results with p-values.
- **Installation**: `conda install -c bioconda maaslin`
- **Key Features**: Handles high-dimensional data, supports multiple covariates, provides visualization.

## Pitfalls

- **Data Requirements**: Requires properly formatted OTU tables and metadata.
- **Normalization**: May require careful normalization of feature counts.
- **Multiple Testing**: High false discovery rate possible without correction.
- **Missing Data**: Missing values may affect analysis results.
- **Model Assumptions**: GLM assumptions must be met for valid results.
- **Computation Time**: Can be slow for large datasets.

## Examples

### Basic association analysis
**Args:** `maaslin.py -i otu_table.tsv -m metadata.tsv -o results/`
**Explanation:** Runs MaAsLin analysis on OTU table and metadata.

### With covariates
**Args:** `maaslin.py -i otu_table.tsv -m metadata.tsv -f age,gender -o results/`
**Explanation:** Includes covariates in the model.

### Random effects
**Args:** `maaslin.py -i otu_table.tsv -m metadata.tsv -r subject_id -o results/`
**Explanation:** Adds random effects for repeated measures.

### Normalization
**Args:** `maaslin.py -i otu_table.tsv -m metadata.tsv -n TSS -o results/`
**Explanation:** Uses TSS normalization.

### Filtering
**Args:** `maaslin.py -i otu_table.tsv -m metadata.tsv -p 0.05 -o results/`
**Explanation:** Filters features by prevalence.

### Help documentation
**Args:** `maaslin.py --help`
**Explanation:** Displays all available options and parameters.