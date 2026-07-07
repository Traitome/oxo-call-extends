---
name: cmph
category: programming
description: CMPH - C Minimal Perfect Hashing Library
tags: [cmph, hashing, perfect-hash, c-library, bioinformatics]
author: oxo-call-community
source_url: "http://cmph.sourceforge.net/"
---

## Concepts

- **Tool Overview**: CMPH is a C library for generating minimal perfect hash functions, which map a set of keys to unique integers without collisions.
- **Core Function**: Generates minimal perfect hash functions for efficient key lookup in large datasets.
- **Algorithm**: Implements multiple perfect hashing algorithms including CHD, BDZ, and FCH.
- **Input**: Set of keys for which to generate a perfect hash function.
- **Output**: Hash function data structure for constant-time key lookup.
- **Application**: Bioinformatics indexing, database indexing, and efficient key-value storage.
- **Installation**: Install via bioconda: `conda install -c bioconda cmph`

## Pitfalls

- **Key Set**: Must have complete set of keys before generating hash function.
- **Memory Usage**: May require significant memory for very large key sets.
- **Algorithm Selection**: Different algorithms have different performance characteristics.
- **Build Time**: Hash function generation can be time-consuming for large key sets.
- **Static Set**: Hash function is static and must be regenerated if keys change.

## Examples

### Create perfect hash
**Args:** `cmph -i keys.txt -o hash.cmph`
**Explanation:** Creates minimal perfect hash from key file.

### Query hash
**Args:** `cmph query -i hash.cmph -k "key1"`
**Explanation:** Looks up key in perfect hash table.

### Benchmark hash
**Args:** `cmph benchmark -i hash.cmph -t queries.txt`
**Explanation:** Benchmarks hash lookup performance.

### Display help
**Args:** `cmph --help`
**Explanation:** Shows all available options and usage information.