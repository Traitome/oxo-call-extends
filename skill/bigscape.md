---
name: bigscape
category: annotation
description: BiG-SCAPE - Biosynthetic Genes Similarity Clustering and Prospecting Engine
tags: [bgc, biosynthetic-gene-cluster, clustering, similarity, natural-products]
author: oxo-call-community
source_url: "https://github.com/medema-group/BiG-SCAPE"
---

## Concepts
- **Tool Overview**: BiG-SCAPE (Biosynthetic Gene Similarity Clustering and Prospecting Engine) clusters and analyzes Biosynthetic Gene Clusters (BGCs) based on domain architecture similarity. It creates gene cluster family (GCF) networks for exploring BGC diversity.
- **Clustering Approach**: Uses a combination of domain architecture similarity, sequence similarity, and synteny to cluster BGCs into gene cluster families (GCFs).
- **Input**: Accepts BGC predictions from antiSMASH, PRISM, or other tools in GenBank format.
- **Visualization**: Generates interactive network visualizations showing relationships between BGCs.
- **Reference Integration**: Can include known BGCs from MIBiG database for comparison and annotation.

## Pitfalls
- **Input Format**: Requires properly formatted GenBank files with annotated BGCs.
- **Memory Usage**: Large BGC collections require substantial memory for distance matrix computation.
- **Clustering Threshold**: Choice of clustering threshold affects GCF granularity. Default threshold (0.3) may need adjustment.

## Examples
### Cluster BGCs from antiSMASH output
**Args:** `bigscape.py -i antismash_output/ -o bigscape_results/`
**Explanation:** Clusters BGC predictions from antiSMASH into gene cluster families.

### Include MIBiG reference
**Args:** `bigscape.py -i bgcs/ --mibig -o results/`
**Explanation:** Clusters input BGCs with MIBiG reference BGCs for comparison.

### Adjust clustering threshold
**Args:** `bigscape.py -i bgcs/ --cutoffs 0.3 0.5 0.7 -o results/`
**Explanation:** Performs clustering at multiple similarity thresholds.
