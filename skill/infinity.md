---
name: infinity
category: programming
description: All-in-one infinity value for Python that can be compared to any object
tags: [infinity, python, utility, mathematics]
author: oxo-call-community
source_url: "https://github.com/kvesteri/infinity"
---

## Concepts

- **Tool Overview**: infinity (v1.4) is a Python library providing a robust infinity value implementation.
- **Core Function**: Represents mathematical infinity that can be compared to any Python object.
- **Features**: Supports arithmetic operations, comparisons, hashability, and JSON serialization.
- **Input/Output**: Works seamlessly with Python numeric types and collections.
- **Use Cases**: Useful in algorithms, data analysis, and mathematical computations involving unbounded values.

## Pitfalls

- **Type Coercion**: May produce unexpected results when mixed with non-numeric types.
- **JSON Serialization**: Requires custom encoder for JSON serialization.
- **Hashability**: Infinity objects are hashable but care needed in dictionary keys.
- **Arithmetic Operations**: Division by infinity and other edge cases require handling.
- **Comparisons**: Be cautious with comparisons involving None or complex objects.

## Examples

### Basic usage
**Args:** `from infinity import inf; x = inf; print(x > 1000)`
**Explanation:** Creates infinity object and compares with integer.

### Arithmetic operations
**Args:** `from infinity import inf; result = inf + 5; print(result)`
**Explanation:** Performs arithmetic operations with infinity.

### Comparison with None
**Args:** `from infinity import inf; print(inf > None)`
**Explanation:** Compares infinity with None (returns True).

### Hashability
**Args:** `from infinity import inf; d = {inf: "infinite"}; print(d[inf])`
**Explanation:** Uses infinity as dictionary key.

### JSON serialization
**Args:** `import json; from infinity import inf; print(json.dumps({"val": inf}, default=str))`
**Explanation:** Serializes infinity to JSON using custom handler.

### Negative infinity
**Args:** `from infinity import inf; ninf = -inf; print(ninf < 0)`
**Explanation:** Uses negative infinity in comparisons.