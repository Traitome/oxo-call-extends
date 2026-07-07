---
name: google-sparsehash
category: utility
description: Google SparseHash is a fast, memory-efficient hash map implementation for C++ with several variants for different use cases.
tags: [google-sparsehash, hash-map, C++, memory-efficient, utility]
author: oxo-call-community
source_url: "https://github.com/sparsehash/sparsehash"
---

## Concepts

- **Memory-Efficient Hashing**: Google SparseHash provides hash map implementations optimized for memory efficiency, using compressed representations to reduce memory footprint.

- **Multiple Implementations**: Includes sparse_hash_map (highly memory-efficient), dense_hash_map (faster but uses more memory), and sparse_hash_set for different performance requirements.

- **C++ Library**: Designed as a C++ template library, providing drop-in replacements for standard STL containers.

- **Compression**: Uses run-length encoding and other compression techniques to store hash table entries efficiently.

- **Performance**: Optimized for both speed and memory usage, with trade-offs available through different container types.

- **Cross-Platform**: Works across multiple platforms including Linux, macOS, and Windows.

## Pitfalls

- **Compression Overhead**: Memory-efficient variants may have slightly higher CPU overhead due to compression/decompression operations.

- **Hash Function Selection**: Default hash functions may not be optimal for all data types. Consider custom hash functions for specific use cases.

- **Iterator Invalidation**: Modifying the hash map can invalidate iterators. Follow STL iterator semantics carefully.

- **Memory Alignment**: Ensure proper memory alignment when using custom allocators or memory pools.

- **Version Compatibility**: Different versions may have API changes. Check the documentation for your installed version.

## Examples

### Basic sparse_hash_map usage
**Args:** `#include <sparsehash/sparse_hash_map>; google::sparse_hash_map<int, std::string> map; map[42] = "value";`
**Explanation:** Creates a memory-efficient hash map and inserts a key-value pair.

### Using dense_hash_map for speed
**Args:** `#include <sparsehash/dense_hash_map>; google::dense_hash_map<std::string, int> map; map.set_empty_key("");`
**Explanation:** Creates a faster hash map with higher memory usage, requiring empty key initialization.

### Using sparse_hash_set
**Args:** `#include <sparsehash/sparse_hash_set>; google::sparse_hash_set<int> set; set.insert(1); set.insert(2);`
**Explanation:** Creates a memory-efficient hash set for storing unique integer values.

### Reserve capacity
**Args:** `map.reserve(10000);`
**Explanation:** Pre-allocates space for 10,000 elements to avoid rehashing during insertion.

### Clear and shrink
**Args:** `map.clear(); map.resize(0);`
**Explanation:** Clears the hash map and releases all allocated memory.

### Custom hash function
**Args:** `struct MyHash { size_t operator()(const MyType& t) const { return t.hash(); } }; google::sparse_hash_map<MyType, Value, MyHash> map;`
**Explanation:** Uses a custom hash function for user-defined types.

### Iterate over map
**Args:** `for (const auto& pair : map) { std::cout << pair.first << ": " << pair.second << std::endl; }`
**Explanation:** Iterates over all key-value pairs in the hash map.