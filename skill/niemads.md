---
name: niemads
category: programming
description: NiemaDS provides non-standard data structures for Python 2 and 3.
tags: [niemads, programming, python, data-structures]
author: oxo-call-community
source_url: "https://github.com/niemasd/NiemaDS"
---

## Concepts

- **Tool Overview**: NiemaDS offers specialized data structures for bioinformatics applications.
- **Core Function**: Provides efficient data structures for sequence analysis.
- **Algorithm**: Implements optimized data structures for biological data.
- **Input Format**: Python objects and biological sequence data.
- **Output**: Processed data structures and analysis results.
- **Use Case**: Bioinformatics programming, sequence analysis, and algorithm development.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Python Version**: Supports both Python 2 and 3.
- **Dependency**: Requires Python installation.
- **Documentation**: Limited documentation.
- **Performance**: May have performance considerations.
- **Compatibility**: Check compatibility with other libraries.

## Examples

### Install package
**Args:** `pip install niemads`
**Explanation:** Installs NiemaDS package.

### Import module
**Args:** `import niemads`
**Explanation:** Imports NiemaDS module in Python.

### Create sequence index
**Args:** `from niemads import SequenceIndex; idx = SequenceIndex(sequences)`
**Explanation:** Creates sequence index for fast lookup.

### K-mer counting
**Args:** `from niemads import KmerCounter; counter = KmerCounter(k=31)`
**Explanation:** Creates k-mer counter for sequence analysis.

### Suffix array
**Args:** `from niemads import SuffixArray; sa = SuffixArray(sequence)`
**Explanation:** Builds suffix array for efficient substring search.

### LCP array
**Args:** `from niemads import LCPArray; lcp = LCPArray(suffix_array)`
**Explanation:** Builds LCP array from suffix array.

### Documentation
**Args:** `pydoc niemads`
**Explanation:** Shows documentation for NiemaDS.