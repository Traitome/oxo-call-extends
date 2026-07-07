---
name: chainmap
category: programming
description: Backport/clone of Python's ChainMap for compatibility with older Python versions
tags: [chainmap, python, data-structures, dictionary, compatibility]
author: oxo-call-community
source_url: "https://bitbucket.org/jeunice/chainmap"
---

## Concepts

- **Tool Overview**: chainmap provides a backport/clone of Python's collections.ChainMap for Python 2.6, Python 3.2, and PyPy3 compatibility.
- **Core Function**: Implements a class for quickly linking multiple dictionaries together for unified access.
- **Features**: Dictionary-like interface, ordered key access, nested mappings, and fallback lookup.
- **Input**: Multiple dictionary objects.
- **Output**: Unified view of all dictionaries as single mapping.
- **Application**: Configuration management, layered settings, and plugin systems.
- **Installation**: Install via bioconda: `conda install -c bioconda chainmap`

## Pitfalls

- **Python Version**: Not needed for Python 3.3+ which includes ChainMap in standard library.
- **Mutable Mapping**: Changes affect underlying dictionaries.
- **Key Order**: Follows insertion order of dictionaries.
- **Performance**: Lookup may be slower than single dictionary.

## Examples

### Create ChainMap from dictionaries
**Args:** `python -c "from chainmap import ChainMap; m = ChainMap(dict1, dict2)"`
**Explanation:** Creates ChainMap from multiple dictionaries.

### Access keys from multiple dicts
**Args:** `python -c "m['key']"`
**Explanation:** Retrieves value from first dict containing key.

### Add new dictionary
**Args:** `python -c "new_m = m.new_child(new_dict)"`
**Explanation:** Adds new dictionary to front of chain.

### Get all keys
**Args:** `python -c "keys = list(m.keys())"`
**Explanation:** Returns all unique keys from all dictionaries.