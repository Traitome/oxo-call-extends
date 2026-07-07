---
name: igua
category: hpc
description: Iterative Gene clUster Analysis, a high-throughput method for gene cluster family identification
tags: [igua, gene clusters, BGC, GCF, metagenomics]
author: oxo-call-community
source_url: "https://github.com/zellerlab/IGUA"
---

## Concepts

- **Tool Overview**: IGUA is a fast, scalable method for identifying Gene Cluster Families (GCFs) from genomic and metagenomic data
- **Core Function**: Performs iterative clustering to group similar gene clusters into families, enabling efficient analysis of large BGC datasets
- **Input/Output**: Accepts gene cluster annotations in GenBank/GFF format; outputs GCF assignments and visualizations
- **Installation**: `pip install igua` or `conda install -c bioconda igua`
- **Key Features**: Over 10x faster than state-of-the-art tools, memory-efficient, supports parallel processing

## Pitfalls

- **Cluster Quality**: Poorly defined input clusters can lead to inaccurate family assignments
- **Parameter Tuning**: Optimal clustering parameters depend on dataset characteristics
- **Memory Usage**: Extremely large datasets may require distributed computing resources
- **Annotation Dependencies**: Relies on accurate gene annotations for meaningful clustering
- **Output Interpretation**: Large numbers of GCFs require careful downstream analysis

## Examples

### Basic GCF identification
**Args:** `igua -i clusters.gff -o gcf_results/`
**Explanation:** Identifies Gene Cluster Families from annotated gene clusters.

### Run with custom similarity threshold
**Args:** `igua -i clusters.gff -o gcf_results/ --threshold 0.7`
**Explanation:** Sets custom similarity threshold (0.7 = 70% similarity cutoff).

### Enable parallel processing
**Args:** `igua -i clusters.gff -o gcf_results/ --threads 8`
**Explanation:** Uses 8 threads for faster computation on multi-core systems.

### Generate visualization
**Args:** `igua -i clusters.gff -o gcf_results/ --visualize`
**Explanation:** Creates visualizations of GCF relationships and clustering results.

### Process metagenomic clusters
**Args:** `igua -i metagenome_clusters.gff -o mg_gcf_results/ --mode metagenomic`
**Explanation:** Optimizes clustering parameters for metagenomic datasets with higher diversity.
