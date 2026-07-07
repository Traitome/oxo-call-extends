---
name: sompy
category: programming
description: SomPy - Numpy-based Self-Organizing Map (SOM) library
tags: [sompy, programming, machine-learning, som, numpy]
author: oxo-call-community
source_url: "https://github.com/ttlg/sompy"
---

## Concepts

- **Tool Overview**: sompy (v0.1.1) - A Self-Organizing Map library
- **Core Function**: Implements SOM algorithm for data clustering and visualization
- **Input/Output**: Accepts numpy arrays; outputs trained SOM model
- **Algorithm**: Self-Organizing Map for unsupervised learning
- **Installation**: `conda install -c bioconda sompy`
- **Key Features**: SOM training, data clustering, visualization

## Pitfalls

- **Input Requirements**: Requires properly formatted numpy arrays
- **Map Size**: Map size affects clustering quality
- **Training Parameters**: Requires proper training parameter selection
- **Normalization**: Data normalization affects SOM results
- **Memory Usage**: Large datasets require significant memory
- **Visualization**: Requires proper visualization setup

## Examples

### Display help
**Args:** `python -c "import sompy; help(sompy)"`
**Explanation:** Shows module documentation.

### Basic SOM training
**Args:** `python -c "import sompy; som = sompy.SOM(mapsize=(10,10), data=data); som.train()"`
**Explanation:** Train SOM on data.

### With custom map size
**Args:** `python -c "import sompy; som = sompy.SOM(mapsize=(20,20), data=data); som.train()"`
**Explanation:** Set custom map size.

### With training parameters
**Args:** `python -c "import sompy; som = sompy.SOM(mapsize=(10,10), data=data); som.train(njob=4, train_algo='seq')"`
**Explanation:** Set training parameters.

### Cluster data
**Args:** `python -c "import sompy; som = sompy.SOM(mapsize=(10,10), data=data); som.train(); clusters = som.cluster(data)"`
**Explanation:** Cluster data using trained SOM.

### Visualize SOM
**Args:** `python -c "import sompy; som = sompy.SOM(mapsize=(10,10), data=data); som.train(); som.visualize()"`
**Explanation:** Visualize trained SOM.

### Save model
**Args:** `python -c "import sompy; som = sompy.SOM(mapsize=(10,10), data=data); som.train(); som.save('model.pkl')"`
**Explanation:** Save trained SOM model.

### Load model
**Args:** `python -c "import sompy; som = sompy.load('model.pkl')"`
**Explanation:** Load saved SOM model.