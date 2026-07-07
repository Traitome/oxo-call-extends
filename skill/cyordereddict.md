---
name: cyordereddict
category: programming
description: Cython implementation of Python's collections.OrderedDict
tags: [cyordereddict, programming, Cython, data-structure]
author: oxo-call-community
source_url: "https://github.com/shoyer/cyordereddict"
---

## Concepts

- **Tool Overview**: cyordereddict (v0.2.2+) is a Cython implementation of Python's collections.OrderedDict for improved performance.
- **Core Function**: Provides an ordered dictionary data structure with faster operations than the standard Python OrderedDict.
- **Input/Output**: Input: Key-value pairs. Output: Ordered dictionary object.
- **Key Features**: Maintains insertion order, faster iteration and lookups, compatible with Python's OrderedDict API.
- **Installation**: `conda install -c bioconda cyordereddict`

## Pitfalls

- **Python Version**: Ensure compatibility with Python version requirements.
- **API Differences**: Minor API differences from standard OrderedDict may exist.
- **Memory Usage**: May use more memory than standard dict for small datasets.
- **Pickling**: May have issues with pickle serialization in some versions.
- **Deprecation**: With Python 3.7+, standard dict maintains insertion order, reducing need for this package.

## Examples

### Create ordered dictionary
**Args:**
```python
from cyordereddict import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(list(od.keys()))  # ['a', 'b']
```
**Explanation:** Create and populate an ordered dictionary.

### Initialize from items
**Args:**
```python
from cyordereddict import OrderedDict
od = OrderedDict([('x', 10), ('y', 20), ('z', 30)])
print(od)  # OrderedDict([('x', 10), ('y', 20), ('z', 30)])
```
**Explanation:** Initialize ordered dictionary from list of tuples.

### Use as default dict
**Args:**
```python
from cyordereddict import OrderedDict
def get_default():
    return []
od = OrderedDict()
od.setdefault('items', []).append('value')
print(od)  # OrderedDict([('items', ['value'])])
```
**Explanation:** Use setdefault method with ordered dictionary.
