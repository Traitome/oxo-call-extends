---
name: chamois
category: metabolomics
description: Chemical Hierarchy Approximation for secondary Metabolism clusters Obtained In Silico
tags: [chamois, metabolomics, natural-products, chemical-clustering, bioinformatics]
author: oxo-call-community
source_url: "https://chamois.readthedocs.io/"
---

## Concepts

- **Tool Overview**: CHAMOIS performs chemical hierarchy approximation for identifying secondary metabolite clusters from genome sequences.
- **Core Function**: Predicts and clusters secondary metabolite biosynthetic gene clusters based on chemical similarity.
- **Algorithm**: Uses machine learning to predict chemical structures from biosynthetic gene clusters and cluster them hierarchically.
- **Input**: Genomic sequences with annotated biosynthetic gene clusters.
- **Output**: Clustered secondary metabolite families with predicted structures.
- **Application**: Natural product discovery and secondary metabolism analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda chamois`

## Pitfalls

- **Annotation Quality**: Depends on accurate gene cluster annotation.
- **Prediction Accuracy**: Chemical structure prediction may have uncertainties.
- **Database Dependencies**: Requires reference chemical databases.
- **Computational Time**: May require significant compute resources.

## Examples

### Run CHAMOIS analysis
**Args:** `chamois -i clusters.gff -o results/`
**Explanation:** Analyzes biosynthetic gene clusters and clusters metabolites.

### With custom database
**Args:** `chamois -i clusters.gff -d custom_db -o results/`
**Explanation:** Uses custom chemical database for clustering.

### Generate visualization
**Args:** `chamois -i clusters.gff -o results/ --visualize`
**Explanation:** Generates visualization of metabolite clusters.

### Display help
**Args:** `chamois --help`
**Explanation:** Shows all available options and usage information.