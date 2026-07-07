---
name: annembed
category: dimension-reduction
description: Ultra-fast and scalable non-linear dimension reduction/embedding algorithm for large-scale biological data
tags: [annembed, dimension-reduction, embedding, UMAP, t-SNE, HNSW, single-cell]
author: oxo-call-community
source_url: "https://github.com/jianshu93/annembed"
---

## Concepts

- **Tool Overview**: annembed (v0.2.6) is an ultra-fast and scalable non-linear dimension reduction algorithm similar to UMAP or t-SNE, optimized for large-scale biological data analysis.
- **Core Function**: Performs dimensionality reduction by constructing nearest neighbor graphs using HNSW (Hierarchical Navigable Small World) algorithm and optimizing embeddings with cross-entropy loss.
- **HNSW Graph Construction**: Uses Hierarchical Navigable Small World graphs for efficient approximate nearest neighbor search, enabling sub-sampling of 2%-4% of data for initialization.
- **Algorithm Mix**: Combines aspects of t-SNE (probability normalization) and UMAP (exponential distance weighting) for optimal embedding quality.
- **Diffusion Maps Initialization**: Supports iterative/hierarchical initialization using diffusion maps algorithm for better convergence.
- **Quality Estimation**: Provides embedding faithfulness metrics by quantifying neighborhood stability through the embedding process.
- **Input/Output**: Accepts dense or sparse matrices; outputs low-dimensional embeddings (typically 2D or 3D for visualization).
- **Installation**: Available via Bioconda (`conda install -c bioconda annembed`) or pip (`pip install annembed-rs`).

## Pitfalls

- **Version Differences**: Options may vary between versions; check compatibility when upgrading.
- **Input Format**: Requires properly formatted numeric matrices; non-numeric data must be pre-processed.
- **Parameter Tuning**: Embedding quality depends on parameters like n_neighbors, min_dist, and target dimension.
- **Memory Usage**: Large datasets require careful memory management; consider subsampling for extremely large data.
- **Determinism**: Results may vary between runs due to random initialization; set random seed for reproducibility.
- **Computational Resources**: GPU acceleration may be beneficial for very large datasets.

## Examples

### Display help
**Args:** `annembed --help`
**Explanation:** Shows available options and usage information.

### Basic embedding from CSV
**Args:** `annembed -i input.csv -o embedding.tsv`
**Explanation:** Reads high-dimensional data from CSV file and outputs 2D embedding to TSV. Default target dimension is 2.

### 3D embedding
**Args:** `annembed -i input.csv -o embedding.tsv -d 3`
**Explanation:** Generates 3D embedding for 3D visualization or downstream analysis.

### Custom number of neighbors
**Args:** `annembed -i input.csv -o embedding.tsv -k 50`
**Explanation:** Sets number of nearest neighbors to 50 (default varies by dataset size). Larger k preserves global structure better.

### Sparse matrix input
**Args:** `annembed -i sparse_matrix.mtx -o embedding.tsv --sparse`
**Explanation:** Processes sparse matrix input (e.g., scRNA-seq count matrices in Matrix Market format).

### Quality estimation
**Args:** `annembed -i input.csv -o embedding.tsv --quality`
**Explanation:** Outputs embedding quality metrics along with coordinates. Helps select best embedding from multiple runs.

### Set random seed for reproducibility
**Args:** `annembed -i input.csv -o embedding.tsv -s 42`
**Explanation:** Sets random seed to ensure reproducible results across runs.

### Custom output format
**Args:** `annembed -i input.csv -o embedding.npy --format numpy`
**Explanation:** Outputs embedding as NumPy array instead of text format for direct use in Python scripts.