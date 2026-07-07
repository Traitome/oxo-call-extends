---
name: graph_embed
category: bioinformatics
description: graph_embed computes 2D embeddings of data matrices using supervised class information for visualization and analysis.
tags: [graph_embed, dimensionality-reduction, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fabriziocosta/GraphEmbed"
---

## Concepts

- **Dimensionality Reduction**: graph_embed reduces high-dimensional data to 2D for visualization and analysis.

- **Supervised Embedding**: Uses class labels to guide the embedding process, preserving class separation.

- **Graph Construction**: Constructs similarity graphs from data matrices for embedding.

- **Visualization**: Generates 2D visualizations that highlight patterns and clusters in the data.

- **Multiple Algorithms**: Supports various embedding algorithms including t-SNE, UMAP, and custom methods.

- **Quality Metrics**: Provides metrics for evaluating embedding quality and class separation.

## Pitfalls

- **Parameter Sensitivity**: Embedding results can be sensitive to parameter choices. Experiment with different settings.

- **Computational Resources**: Processing very large datasets may require significant memory.

- **Class Imbalance**: Uneven class distribution can affect embedding quality. Consider balancing classes.

- **Data Normalization**: Ensure data is properly normalized before embedding.

- **Result Interpretation**: Embedding results require careful interpretation. Clusters may not always correspond to true biological groups.

## Examples

### Basic embedding
**Args:** `graph_embed -i data_matrix.txt -l labels.txt -o embedding.txt`
**Explanation:** Computes 2D embedding using class labels for guidance.

### Specify algorithm
**Args:** `graph_embed -i data_matrix.txt -l labels.txt -a umap -o embedding.txt`
**Explanation:** Uses UMAP algorithm for embedding instead of default.

### Generate visualization
**Args:** `graph_embed -i data_matrix.txt -l labels.txt -p -o plot.png`
**Explanation:** Creates a 2D scatter plot of the embedding.

### Adjust perplexity
**Args:** `graph_embed -i data_matrix.txt -l labels.txt -x 30 -o embedding.txt`
**Explanation:** Sets perplexity parameter to 30 for t-SNE-like algorithms.

### Batch processing
**Args:** `graph_embed batch -d datasets/ -o results/`
**Explanation:** Processes multiple data matrices in a directory.

### Evaluate embedding quality
**Args:** `graph_embed -i data_matrix.txt -l labels.txt -e -o metrics.txt`
**Explanation:** Computes quality metrics for the embedding.

### Custom distance metric
**Args:** `graph_embed -i data_matrix.txt -l labels.txt -d cosine -o embedding.txt`
**Explanation:** Uses cosine distance instead of Euclidean distance.