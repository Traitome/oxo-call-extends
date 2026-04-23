---
name: bigslice
category: annotation
description: BiG-SLICE - Large scale analysis of Biosynthetic Gene Clusters
tags: [bgc, biosynthetic-gene-cluster, clustering, large-scale]
author: oxo-call-community
source_url: "https://github.com/satriaphd/bigslice"
---

## Concepts
- **Tool Overview**: BiG-SLICE is a highly scalable tool for large-scale analysis of Biosynthetic Gene Clusters (BGCs). It can cluster hundreds of thousands of BGCs efficiently using feature extraction and hierarchical clustering.
- **Scalability**: Designed to handle datasets too large for BiG-SCAPE, processing 100,000+ BGCs.
- **Feature Extraction**: Converts BGCs into numerical feature vectors based on domain composition and architecture.
- **Clustering**: Uses hierarchical clustering on feature vectors for efficient grouping of similar BGCs.
- **Interactive Results**: Provides web-based interface for exploring clustering results.

## Pitfalls
- **Input Format**: Requires BGC predictions in GenBank or JSON format.
- **Feature Granularity**: Feature extraction parameters affect clustering results.
- **Computational Resources**: Large datasets require significant CPU and memory.

## Examples
### Process BGC collection
**Args:** `bigslice process -i bgcs/ -o results/`
**Explanation:** Extracts features and clusters large BGC collection.

### Use specific clustering level
**Args:** `bigslice cluster -i results/ -c 1000 -o clusters/`
**Explanation:** Clusters BGCs into approximately 1000 groups.
