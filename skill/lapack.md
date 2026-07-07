---
name: lapack
category: library
description: Linear Algebra Package - standard library for numerical linear algebra
tags: [lapack, library, linear-algebra, numerical-computation, matrix]
author: oxo-call-community
source_url: "https://github.com/Reference-LAPACK/lapack"
---

## Concepts

- **Linear Algebra**: Standard library for numerical linear algebra
- **Matrix Operations**: Provides matrix decomposition and operations
- **Eigenvalue Problems**: Solves eigenvalue and singular value problems
- **Linear Equations**: Solves systems of linear equations
- **Factorization**: Implements LU, QR, Cholesky factorization
- **Fortran Interface**: Original Fortran implementation

## Pitfalls

- **Fortran Ordering**: Uses column-major memory layout
- **Memory Allocation**: Large matrices need careful allocation
- **Numerical Stability**: Some algorithms may be numerically unstable
- **Thread Safety**: Not all routines are thread-safe
- **Interface Complexity**: Complex API requires careful usage
- **Version Differences**: Results may vary between versions

## Examples

### Solve linear system
**Args:** `lapackgesv A b x`
**Explanation:** Solves linear system Ax = b.

### Eigenvalue computation
**Args:** `lapackgeev A eigenvalues eigenvectors`
**Explanation:** Computes eigenvalues and eigenvectors.

### SVD computation
**Args:** `lapackgesvd A U S V`
**Explanation:** Computes singular value decomposition.

### LU factorization
**Args:** `lapackgetrf A L U P`
**Explanation:** Computes LU factorization with pivoting.

### QR factorization
**Args:** `lapackgeqrf A Q R`
**Explanation:** Computes QR factorization.

### Cholesky decomposition
**Args:** `lapackpotrf A L`
**Explanation:** Computes Cholesky factorization for SPD matrices.