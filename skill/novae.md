---
name: novae
category: expression
description: NovAE is a graph-based foundation model for spatial transcriptomics data analysis.
tags: [novae, expression, spatial-transcriptomics, foundation-model]
author: oxo-call-community
source_url: "https://mics-lab.github.io/novae/"
---

## Concepts

- **Tool Overview**: NovAE analyzes spatial transcriptomics data using graph-based foundation models.
- **Core Function**: Processes spatial gene expression data for pattern discovery.
- **Algorithm**: Uses graph neural networks for spatial data analysis.
- **Input Format**: Accepts spatial transcriptomics data matrices.
- **Output**: Produces spatial patterns and expression analysis.
- **Use Case**: Spatial transcriptomics analysis, tissue mapping, and gene expression.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Data Quality**: Results depend on input data quality.
- **Computational Cost**: Analysis can be computationally intensive.
- **Memory Usage**: Large datasets require memory.
- **Model Training**: Requires training on appropriate datasets.
- **Interpretation**: Requires understanding of graph neural networks.

## Examples

### Display help
**Args:** `novae --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `novae -i spatial_data.h5ad -o results/`
**Explanation:** Runs spatial transcriptomics analysis.

### Train model
**Args:** `novae train -i train_data.h5ad -o model.pt`
**Explanation:** Trains foundation model on spatial data.

### Infer with model
**Args:** `novae infer -i data.h5ad -m model.pt -o predictions.h5ad`
**Explanation:** Runs inference with trained model.

### Cluster analysis
**Args:** `novae cluster -i spatial_data.h5ad -o clusters.h5ad`
**Explanation:** Performs spatial clustering.

### Visualize results
**Args:** `novae visualize -i results.h5ad -o plot.png`
**Explanation:** Generates visualization of results.

### Threads
**Args:** `novae -i spatial_data.h5ad -t 8 -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `novae -i spatial_data.h5ad -v -o results/`
**Explanation:** Runs with verbose output.