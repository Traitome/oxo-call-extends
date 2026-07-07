---
name: scoring-matrices
category: sequence-analysis
description: scoring-matrices - Dependency free, Cython-compatible scoring matrices for biological sequences
tags: ["scoring-matrices", "sequence-analysis", "alignment", "bioinformatics"]
author: oxo-call-community
source_url: "https://scoring-matrices.readthedocs.org"
---

## Concepts

- **Tool Overview**: scoring-matrices (v0.3.4) provides dependency-free, Cython-compatible scoring matrices for biological sequences.
- **Core Function**: Offers standardized scoring matrices for sequence alignment and comparison.
- **Algorithm**: Implements various scoring matrices including BLOSUM and PAM matrices.
- **Input/Output**: Accepts sequence data and produces alignment scores.
- **Performance**: Optimized for fast computation with Cython support.
- **Applications**: Sequence alignment, protein comparison, and bioinformatics analysis.

## Pitfalls

- **Matrix Selection**: Choosing the wrong matrix affects alignment quality.
- **Gap Penalties**: Requires appropriate gap penalty settings.
- **Memory Usage**: Large matrices may require significant memory.
- **Version Compatibility**: Different versions may have breaking changes.
- **Performance**: May require optimization for very large datasets.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Load BLOSUM62 matrix
**Args:** `from scoring_matrices import BLOSUM62; matrix = BLOSUM62()`
**Explanation:** Loads BLOSUM62 scoring matrix.

### Load PAM250 matrix
**Args:** `from scoring_matrices import PAM250; matrix = PAM250()`
**Explanation:** Loads PAM250 scoring matrix.

### Get score
**Args:** `score = matrix['A']['T']`
**Explanation:** Gets alignment score for amino acids A and T.

### Custom matrix
**Args:** `from scoring_matrices import ScoringMatrix; custom = ScoringMatrix(matrix_dict)`
**Explanation:** Creates custom scoring matrix.

### Save matrix
**Args:** `matrix.to_file('matrix.txt')`
**Explanation:** Saves matrix to file.

### Load from file
**Args:** `from scoring_matrices import load_matrix; matrix = load_matrix('matrix.txt')`
**Explanation:** Loads matrix from file.

### Matrix properties
**Args:** `size = matrix.size; is_symmetric = matrix.is_symmetric`
**Explanation:** Gets matrix properties.