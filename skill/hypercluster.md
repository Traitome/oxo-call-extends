---
name: hypercluster
category: hpc
description: hypercluster - Automatic clustering hyperparameter optimization
tags: [hypercluster, clustering, hyperparameter optimization]
author: oxo-call-community
source_url: "https://hypercluster.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: hypercluster is a Python package for automatic clustering hyperparameter optimization.
- **AutoClusterer**: Main class that automates hyperparameter search across multiple clustering algorithms.
- **Random Search**: Supports random search for efficient exploration of hyperparameter space.
- **Multi-algorithm Support**: Can optimize parameters across multiple clustering algorithms simultaneously.
- **Evaluation Metrics**: Includes various evaluation metrics for clustering quality assessment.
- **Installation**: `conda install -c bioconda hypercluster`

## Pitfalls

- **Parameter Space**: Large parameter spaces can increase computation time significantly.
- **Data Scaling**: Clustering performance may be affected by feature scaling.
- **Algorithm Selection**: Choice of clustering algorithm depends on data characteristics.
- **Evaluation Metrics**: Different metrics may yield different optimal parameter sets.
- **Memory Usage**: Evaluating many parameter combinations can be memory-intensive.
- **Computation Time**: Full hyperparameter optimization may require significant computational resources.

## Examples

### Basic auto-clustering
**Args:** `hypercluster --input data.csv --output results/`
**Explanation:** Runs automatic clustering with default settings.

### Specify clustering algorithm
**Args:** `hypercluster --input data.csv --algorithm KMeans --output results/`
**Explanation:** Optimizes hyperparameters specifically for KMeans clustering.

### Multi-algorithm optimization
**Args:** `hypercluster --input data.csv --algorithms KMeans DBSCAN HDBSCAN --output results/`
**Explanation:** Optimizes parameters across multiple clustering algorithms.

### Enable random search
**Args:** `hypercluster --input data.csv --random_search --fraction 0.5 --output results/`
**Explanation:** Uses random search with 50% of parameter combinations.

### Custom parameter grid
**Args:** `hypercluster --input data.csv --params params.json --output results/`
**Explanation:** Uses custom parameter grid defined in JSON file.