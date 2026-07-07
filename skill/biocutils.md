---
name: biocutils
category: utility
description: Miscellaneous utilities for BiocPy, mostly to mimic base functionality in R
tags: [biocpy, utilities, r-interoperability]
author: oxo-call-community
source_url: "https://github.com/BiocPy/biocutils"
---

## Concepts

- **Tool Overview**: biocutils is a Python library providing utilities for the BiocPy project, primarily mirroring R's base functionality for easier transition from R to Python.
- **R Interoperability**: Provides R-like functions such as `match`, `order`, `unique`, and `table` that are familiar to R/Bioconductor users.
- **Named Lists**: Implements NamedList data structure similar to R's named lists.
- **BiocObject**: Base class for BiocPy objects with common methods.

## Pitfalls

- **R-Centric Design**: Functions follow R semantics which may differ from Python conventions.
- **BiocPy Ecosystem**: Primarily designed for use within the BiocPy ecosystem.

## Examples

### Use match function
**Args:** `from biocutils import match; result = match(['a', 'b'], ['b', 'c', 'a'])`
**Explanation:** Finds indices of first matches, similar to R's match() function.

### Create NamedList
**Args:** `from biocutils import NamedList; nl = NamedList(a=[1,2,3], b='hello')`
**Explanation:** Creates a named list object with named elements.