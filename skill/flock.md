---
name: flock
category: hpc
description: "FLOCK is a flow cytometry clustering tool that automatically identifies cell populations without requiring prior specification of cluster number."
tags: [flock, hpc, flow-cytometry, clustering, bioinformatics, cell-analysis]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/immportflock/"
---

## Concepts
- **Tool Overview**: FLOCK (Flow Cytometry Clustering without K) is an automated clustering tool for flow cytometry data that identifies cell populations without requiring the user to specify the number of clusters.
- **Core Function**: Automatically identifies and clusters cell populations in flow cytometry data using density-based clustering algorithms.
- **Input/Output**: Input: FCS flow cytometry files. Output: Cluster assignments, population statistics, visualization.
- **Clustering Algorithm**: Uses a density-based approach that identifies clusters based on local density maxima, similar to DBSCAN.
- **Parameter-Free**: Requires minimal user input, automatically determining cluster number and boundaries.
- **Population Identification**: Identifies cell populations by analyzing marker expression patterns across all dimensions.
- **Installation**: `conda install -c bioconda flock` or download from SourceForge.

## Pitfalls
- **Data Quality**: Poor quality data with high background noise affects clustering accuracy. Clean data before analysis.
- **Marker Selection**: Requires appropriate marker panel for distinguishing cell populations. Insufficient markers produce poor clusters.
- **Density Variation**: Highly variable cell densities across samples may affect cluster consistency.
- **Computational Time**: Large datasets require significant computation time. Consider subsampling for exploration.
- **Memory Requirements**: Very large FCS files may exceed memory limits. Process files individually if needed.
- **Cluster Validation**: Always validate clusters manually. Automated clustering may produce unexpected results.

## Examples
### Basic clustering
**Args:** `flock --input sample.fcs --output clusters.txt`
**Explanation:** Runs FLOCK clustering on single FCS file and outputs cluster assignments.

### Batch processing
**Args:** `flock --input-dir fcs_files/ --output-dir results/`
**Explanation:** Processes all FCS files in directory and saves results to output directory.

### Custom density threshold
**Args:** `flock --input sample.fcs --output clusters.txt --density-threshold 0.5`
**Explanation:** Sets custom density threshold for cluster identification.

### Generate visualization
**Args:** `flock --input sample.fcs --output clusters.txt --visualize --plot output.png`
**Explanation:** Generates visualization of clustering results as PNG image.

### Cluster statistics
**Args:** `flock --input sample.fcs --output clusters.txt --stats stats.txt`
**Explanation:** Outputs detailed statistics for each identified cluster.
