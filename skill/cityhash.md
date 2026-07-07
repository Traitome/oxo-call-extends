---
name: cityhash
category: programming
description: Python-bindings for CityHash, a fast non-cryptographic hash algorithm
tags: [cityhash, python, hash, algorithm, programming]
author: oxo-call-community
source_url: "https://github.com/escherba/python-cityhash"
---

## Concepts

- **Tool Overview**: cityhash provides Python bindings for CityHash, a fast non-cryptographic hash algorithm developed by Google.
- **Core Function**: Computes hash values for strings and binary data with high performance.
- **Algorithm**: Implements CityHash algorithm for fast hashing of arbitrary length strings.
- **Input**: Strings or binary data.
- **Output**: 64-bit or 128-bit hash values.
- **Application**: Data indexing, checksums, hash tables, and bioinformatics data processing.
- **Installation**: Install via bioconda: `conda install -c bioconda cityhash` or pip: `pip install cityhash`

## Pitfalls

- **Non-Cryptographic**: Not suitable for cryptographic purposes; use for hash tables only.
- **Collision Risk**: May have hash collisions; not guaranteed to be unique.
- **String Encoding**: Ensure proper string encoding before hashing.
- **Python Version**: Compatibility depends on Python version.
- **Data Types**: Only works with string/binary data.

## Examples

### Compute 64-bit hash
**Args:** `import cityhash; h = cityhash.CityHash64("test_string")`
**Explanation:** Computes 64-bit hash of input string.

### Compute 128-bit hash
**Args:** `import cityhash; h = cityhash.CityHash128("test_string")`
**Explanation:** Computes 128-bit hash of input string.

### Hash binary data
**Args:** `import cityhash; h = cityhash.CityHash64(binary_data)`
**Explanation:** Computes hash of binary data.

### Hash with seed
**Args:** `import cityhash; h = cityhash.CityHash64WithSeed("test", 12345)`
**Explanation:** Computes hash with custom seed value.