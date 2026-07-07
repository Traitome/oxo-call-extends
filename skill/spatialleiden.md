---
name: spatialleiden
category: spatial-omics
description: SpatialLeiden - Multiplex Leiden clustering for spatial omics data
tags: [spatialleiden, spatial-omics, clustering, leiden, multiplex]
author: oxo-call-community
source_url: "https://spatialleiden.readthedocs.io/"
---

## Concepts

- **Tool Overview**: spatialleiden (v0.4.0) - A spatial clustering tool
- **Core Function**: Implements multiplex Leiden clustering for spatial omics
- **Input/Output**: Accepts spatial omics data; outputs cluster assignments
- **Algorithm**: Multiplex Leiden clustering algorithm
- **Installation**: `conda install -c bioconda spatialleiden`
- **Key Features**: Spatial clustering, Leiden algorithm, multiplex analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted spatial omics data
- **Spatial Information**: Requires spatial coordinates for clustering
- **Resolution**: Resolution parameter affects cluster granularity
- **Memory Usage**: Large spatial datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Cluster Quality**: Cluster quality depends on parameter settings

## Examples

### Display help
**Args:** `spatialleiden --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `spatialleiden -i spatial_data.tsv -o clusters.tsv`
**Explanation:** Perform Leiden clustering on spatial data.

### With spatial coordinates
**Args:** `spatialleiden -i spatial_data.tsv -c coordinates.tsv -o clusters.tsv`
**Explanation:** Use spatial coordinates for clustering.

### With resolution
**Args:** `spatialleiden -i spatial_data.tsv -o clusters.tsv --resolution 1.0`
**Explanation:** Set clustering resolution.

### Multiplex clustering
**Args:** `spatialleiden -i spatial_data.tsv -o clusters.tsv --multiplex`
**Explanation:** Perform multiplex clustering.

### With multiple modalities
**Args:** `spatialleiden -i modality1.tsv modality2.tsv -o clusters.tsv`
**Explanation:** Cluster using multiple modalities.

### Output detailed results
**Args:** `spatialleiden -i spatial_data.tsv -o clusters.tsv --detailed`
**Explanation:** Output detailed cluster information.

### Output statistics
**Args:** `spatialleiden -i spatial_data.tsv -o clusters.tsv --stats`
**Explanation:** Output clustering statistics.

### Generate report
**Args:** `spatialleiden -i spatial_data.tsv -o clusters.tsv --report`
**Explanation:** Generate clustering report.