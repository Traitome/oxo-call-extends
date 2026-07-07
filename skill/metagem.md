---
name: metagem
category: metagenomics
description: Generate context specific genome-scale metabolic models and predict metabolic interactions directly from metagenomic data
tags: [metagem, metagenomics, metabolic-modeling]
author: oxo-call-community
source_url: "https://github.com/franciscozorrilla/metaGEM"
---

## Concepts

- **Tool Overview**: metaGEM v1.0.5 is a tool for generating context-specific genome-scale metabolic models and predicting metabolic interactions directly from metagenomic data.
- **Core Function**: Constructs genome-scale metabolic models (GEMs) from metagenomic assemblies to predict microbial metabolic interactions.
- **Metabolic Modeling**: Builds constraint-based metabolic models for individual genomes and communities.
- **Interaction Prediction**: Predicts metabolic interactions between different species in microbial communities.
- **Input/Output**: Accepts metagenomic assemblies and annotations; outputs metabolic models and interaction predictions.
- **Context-specific**: Generates models tailored to specific environmental conditions.

## Pitfalls

- **Computational Resources**: Building metabolic models requires significant computational resources.
- **Annotation Quality**: Model accuracy depends on gene annotation quality.
- **Gap Filling**: May require gap filling for incomplete metabolic networks.
- **Parameter Tuning**: Model parameters may need adjustment for different environments.
- **Model Complexity**: Complex models can be difficult to interpret.
- **Reference Databases**: Depends on comprehensive metabolic databases for model construction.

## Examples

### Generate metabolic model
**Args:** `metagem build -i contigs.fasta -a annotations.gff -o model.xml`
**Explanation:** Builds a genome-scale metabolic model from metagenomic data.

### Community modeling
**Args:** `metagem community -i models/ -o community_model.xml`
**Explanation:** Constructs a community metabolic model from individual genome models.

### Predict interactions
**Args:** `metagem predict -i community_model.xml -o interactions.txt`
**Explanation:** Predicts metabolic interactions in microbial communities.

### Flux balance analysis
**Args:** `metagem fba -i model.xml -o flux_results.txt`
**Explanation:** Performs flux balance analysis on metabolic model.

### Gap filling
**Args:** `metagem gapfill -i model.xml -o filled_model.xml`
**Explanation:** Fills gaps in incomplete metabolic networks.