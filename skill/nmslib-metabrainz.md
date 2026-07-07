---
name: nmslib-metabrainz
category: programming
description: NMSLIB provides efficient approximate nearest neighbor search for non-metric spaces.
tags: [nmslib-metabrainz, programming, nearest-neighbor, search]
author: oxo-call-community
source_url: "https://github.com/nmslib/nmslib"
---

## Concepts

- **Tool Overview**: NMSLIB is a library for efficient approximate nearest neighbor search.
- **Core Function**: Performs fast similarity search in high-dimensional spaces.
- **Algorithm**: Implements various indexing and search algorithms.
- **Input Format**: Accepts vectors and distance matrices.
- **Output**: Produces nearest neighbor results.
- **Use Case**: Similarity search, recommendation systems, and data mining.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large indexes require memory.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Dependency**: Requires proper library linkage.
- **Documentation**: Limited documentation for some features.
- **Performance**: May have performance considerations.

## Examples

### Install package
**Args:** `pip install nmslib`
**Explanation:** Installs NMSLIB package.

### Import module
**Args:** `import nmslib`
**Explanation:** Imports NMSLIB module in Python.

### Create index
**Args:** `index = nmslib.init(method='hnsw', space='cosinesimil')`
**Explanation:** Creates HNSW index for cosine similarity.

### Add data
**Args:** `index.addDataPointBatch(vectors)`
**Explanation:** Adds data points to index.

### Build index
**Args:** `index.createIndex({'post': 2}, print_progress=True)`
**Explanation:** Builds the search index.

### Query neighbors
**Args:** `results = index.knnQuery(query_vector, k=10)`
**Explanation:** Queries k nearest neighbors.

### Save index
**Args:** `index.saveIndex('index.bin')`
**Explanation:** Saves index to file.