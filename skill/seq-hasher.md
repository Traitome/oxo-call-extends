---
name: seq-hasher
category: utility
description: seq-hasher - Compute hash digests for DNA sequences with circular permutation support
tags: ["seq-hasher", "utility", "hash", "FASTA"]
author: oxo-call-community
source_url: "https://github.com/apcamargo/seq-hasher"
---

## Concepts

- **Tool Overview**: seq-hasher (v0.2.0) computes hash digests for DNA sequences in FASTA files.
- **Core Function**: Generates hash values for sequence identification and comparison.
- **Algorithm**: Implements various hash algorithms with circular permutation support.
- **Input/Output**: Accepts FASTA files and produces hash values.
- **Sequence Hashing**: Focuses on generating unique identifiers for sequences.
- **Applications**: Sequence deduplication, database indexing, and sequence comparison.

## Pitfalls

- **Hash Collisions**: Potential for hash collisions with very large datasets.
- **Memory Usage**: High memory requirements for large FASTA files.
- **Input Format**: Requires correct FASTA format.
- **Performance**: May be slow for very large files.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Compute hashes
**Args:** `seq-hasher -i input.fasta -o hashes.txt`
**Explanation:** `-i` input FASTA; `-o` output hash file.

### Circular permutation
**Args:** `seq-hasher -i input.fasta -c -o hashes.txt`
**Explanation:** `-c` enables circular permutation support.

### MD5 hash
**Args:** `seq-hasher -i input.fasta -a md5 -o hashes.txt`
**Explanation:** `-a md5` uses MD5 algorithm.

### Verbose logging
**Args:** `seq-hasher -i input.fasta -v -o hashes.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seq-hasher --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seq-hasher --version`
**Explanation:** Shows current version.

### Compare sequences
**Args:** `seq-hasher compare -i hashes1.txt -j hashes2.txt -o diff.txt`
**Explanation:** Compares two hash files.