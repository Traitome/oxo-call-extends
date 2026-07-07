---
name: kf2vec
category: utility
description: K-mer frequency to vector tool for machine learning applications.
tags: [kf2vec, utility, k-mer, vector, machine learning]
author: oxo-call-community
source_url: "https://github.com/noraracht/kf2vec"
---

## Concepts

- **Tool Overview**: kf2vec (v1.0.62) - Converts k-mer frequencies to vectors.
- **k-mer Vectorization**: Converts sequence data to numerical vectors.
- **Machine Learning**: Prepares data for ML models.
- **Feature Engineering**: Creates features from k-mer counts.
- **Dimensionality Reduction**: Supports dimensionality reduction.
- **Multiple Formats**: Supports various input formats.

## Pitfalls

- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Vector Size**: Large k-mer sizes produce large vectors.
- **Memory Usage**: Large datasets require memory.
- **Normalization**: Requires proper normalization.
- **Computation Time**: Complex transformations can be slow.
- **Feature Selection**: May require feature selection.

## Examples

### Convert k-mer counts to vector
**Args:** `kf2vec -i counts.txt -o vector.txt`
**Explanation:** Converts k-mer counts to vector.

### Set k-mer size
**Args:** `kf2vec -i counts.txt -o vector.txt -k 21`
**Explanation:** Uses 21-mers for vectorization.

### Dimensionality reduction
**Args:** `kf2vec -i counts.txt -o vector.txt -d 100`
**Explanation:** Reduces vector to 100 dimensions.

### Normalize vector
**Args:** `kf2vec -i counts.txt -o vector.txt -n`
**Explanation:** Normalizes output vector.

### Multiple samples
**Args:** `kf2vec -i samples.txt -o matrix.txt -m`
**Explanation:** Processes multiple samples into matrix.

### Output as numpy array
**Args:** `kf2vec -i counts.txt -o vector.npy -f numpy`
**Explanation:** Outputs vector as numpy array.