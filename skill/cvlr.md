---
name: cvlr
category: hpc
description: Clustering and Visualization of Long Reads
tags: [cvlr, hpc, long-reads, clustering, visualization, nanopore]
author: oxo-call-community
source_url: "https://github.com/EmanueleRaineri/cvlr"
---

## Concepts

- **Tool Overview**: cvlr (v1.0+) is a tool for clustering and visualization of long sequencing reads from platforms like Oxford Nanopore.
- **Core Function**: Clusters long reads based on sequence similarity and provides visualization of clustering results.
- **Input/Output**: Input: FASTA/FASTQ long reads, optionally alignment files. Output: Clustered reads, visualization plots, cluster statistics.
- **Algorithm**: Uses MinHash or alignment-based methods for efficient clustering of long reads.
- **Key Features**: Efficient clustering of long reads, interactive visualization, cluster quality metrics.
- **Installation**: `conda install -c bioconda cvlr`

## Pitfalls

- **Read Length**: Designed for long reads; short reads may produce poor clustering.
- **Memory Usage**: Large datasets may require significant memory for clustering.
- **Parameter Tuning**: Clustering parameters require careful adjustment for specific data.
- **Quality Filtering**: Low-quality reads should be filtered before clustering.
- **Visualization**: Very large clusters may produce cluttered visualizations.

## Examples

### Cluster long reads
**Args:** `cvlr cluster -i long_reads.fastq -o clusters/ --kmer-size 15`
**Explanation:** Cluster long reads using k-mer based similarity.

### Generate visualization
**Args:** `cvlr visualize -i clusters.txt -o plot.png --method umap`
**Explanation:** Generate UMAP visualization of read clusters.

### Evaluate cluster quality
**Args:** `cvlr evaluate -i clusters.txt -o quality_report.txt`
**Explanation:** Generate quality metrics for clustering results.
