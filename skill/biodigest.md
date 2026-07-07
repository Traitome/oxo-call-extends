---
name: biodigest
category: annotation
description: In silico Validation of Disease and Gene sets, Clusterings or Subnetworks (DIGEST)
tags: [gene-set-analysis, validation, disease-gene, enrichment-analysis]
author: oxo-call-community
source_url: "https://github.com/bionetslab/digest-py"
---

## Concepts

- **Tool Overview**: biodigest (DIGEST) is a Python-based validation tool for in silico validation of disease and gene sets, clusterings, or subnetworks. It provides automated pipelines for disease/gene ID mapping, enrichment analysis, and background distribution estimation.
- **Validation Modes**: Set validation (reference-free or against reference), clustering validation (Dunn Index, Silhouette Score, Davies-Bouldin index), and subnetwork validation.
- **Enrichment Analysis**: Uses GO and KEGG for functional analysis of gene sets.
- **Background Estimation**: Generates empirical P-values using random target sets based on user-selected background models.

## Pitfalls

- **Data Requirements**: Requires precalculated mappings and distance matrices; first-time setup requires downloading reference data.
- **graph-tool Dependency**: Requires graph-tool package for subnetwork analysis.
- **Internet Access**: Initial data download requires internet connection.

## Examples

### Validate gene set
**Args:** `biodigest validate --targets genes.txt --id-type entrez --mode set`
**Explanation:** Validates a gene set using reference-free mode.

### Validate clustering
**Args:** `biodigest validate --targets clusters.txt --id-type entrez --mode clustering`
**Explanation:** Validates clustering using quality measures (Dunn Index, Silhouette Score, Davies-Bouldin).

### Download reference data
**Args:** `biodigest download-data`
**Explanation:** Downloads precalculated mappings and distance matrices for validation.