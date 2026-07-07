---
name: smhasher
category: programming
description: Python extension for smhasher hash functions providing fast, high-quality hash algorithms
tags: [smhasher, programming, hash-functions, murmurhash, cityhash]
author: oxo-call-community
source_url: "http://github.com/phensley/python-smhasher"
---

## Concepts

- **Tool Overview**: smhasher (v0.150.1) - A Python extension wrapper for the smhasher hash library
- **Core Function**: Provides access to high-performance hash functions including MurmurHash, CityHash, etc.
- **Input/Output**: Accepts string/bytes input; outputs hash values
- **Algorithm**: Implements various non-cryptographic hash algorithms
- **Installation**: `conda install -c bioconda smhasher`
- **Key Features**: Fast performance, multiple hash algorithms, Python integration

## Pitfalls

- **Hash Collisions**: Non-cryptographic hashes can have collisions
- **Input Type**: Ensure correct input type (string vs bytes)
- **Version Compatibility**: API may change between versions
- **Seed Values**: Hash results depend on seed parameters
- **Platform Dependence**: Some hash functions may produce different results on different platforms
- **Security Limitations**: Not suitable for cryptographic applications

## Examples

### Display help
**Args:** `python -c "import smhasher; help(smhasher)"`
**Explanation:** Shows available hash functions and usage.

### Basic hash
**Args:** `python -c "import smhasher; print(smhasher.murmurhash3_x64_128(b'hello'))"`
**Explanation:** Compute MurmurHash3 128-bit hash.

### With seed
**Args:** `python -c "import smhasher; print(smhasher.murmurhash3_x64_64(b'hello', seed=42))"`
**Explanation:** Compute hash with custom seed value.

### CityHash
**Args:** `python -c "import smhasher; print(smhasher.cityhash128(b'hello'))"`
**Explanation:** Compute CityHash 128-bit hash.

### FarmHash
**Args:** `python -c "import smhasher; print(smhasher.farmhash64(b'hello'))"`
**Explanation:** Compute FarmHash 64-bit hash.

### SpookyHash
**Args:** `python -c "import smhasher; print(smhasher.spookyhash128(b'hello'))"`
**Explanation:** Compute SpookyHash 128-bit hash.

### Hash file
**Args:** `python -c "import smhasher; print(smhasher.murmurhash3_x64_128(open('file.txt', 'rb').read()))"`
**Explanation:** Compute hash of file contents.