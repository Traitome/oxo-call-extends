---
name: diffacto
category: annotation
description: Diffacto - Protein summarization for shotgun proteomics experiments.
tags: [diffacto, annotation, proteomics, protein-summarization, quantification]
author: oxo-call-community
source_url: "https://github.com/statisticalbiotechnology/diffacto"
---

## Concepts

- **Tool Overview**: diffacto (v1.0.7+) is a protein summarization method for shotgun proteomics that combines peptide-level quantifications.
- **Core Function**: Summarizes peptide-level quantifications to protein-level abundances using quality-weighted aggregation.
- **Input/Output**: Input: Peptide quantification table with intensities and quality scores. Output: Protein-level summaries with confidence scores.
- **Algorithm**: Uses robust aggregation methods to combine peptide measurements into protein-level quantifications.
- **Key Features**: Quality-weighted aggregation, missing value handling, confidence estimation, supports multiple quantification methods.
- **Installation**: `conda install -c bioconda diffacto`

## Pitfalls

- **Input Requirements**: Requires peptide-level quantification data with quality scores.
- **Protein Groups**: Handles shared peptides between protein groups.
- **Missing Values**: Requires appropriate handling of missing peptide measurements.
- **Normalization**: May require pre-normalization of peptide intensities.
- **Computational Time**: May be slow for large proteomics datasets.

## Examples

### Summarize peptides to proteins
**Args:** `diffacto --input peptides.tsv --output proteins.tsv`
**Explanation:** Summarizes peptide quantifications to protein-level abundances.

### With quality weights
**Args:** `diffacto --input peptides.tsv --output proteins.tsv --weights quality_scores.tsv`
**Explanation:** Use quality scores to weight peptide contributions.

### Handle missing values
**Args:** `diffacto --input peptides.tsv --output proteins.tsv --impute`
**Explanation:** Impute missing peptide values before aggregation.

### Batch processing
**Args:** `diffacto --input-dir peptide_files/ --output proteins.tsv`
**Explanation:** Process multiple peptide files in batch.

### Generate statistics
**Args:** `diffacto --input peptides.tsv --output proteins.tsv --stats stats.tsv`
**Explanation:** Generate summary statistics for protein quantification.