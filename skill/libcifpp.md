---
name: libcifpp
category: variant-calling
description: Library containing code to manipulate mmCIF and PDB files.
tags: [libcifpp, variant-calling]
author: oxo-call-community
source_url: "https://github.com/PDB-REDO/libcifpp"
---

## Concepts

- **Tool Overview**: libcifpp v10.0.3 - This library, libcifpp, is a generic CIF library with some specific additions to work with mmCIF files. The main focus of this library is to make sure that files read or written are valid. That is, they are syntactically valid and their content is valid with respect to a CIF dictionary, if such a dictionary is available and specified..
- **Core Function**: Library containing code to manipulate mmCIF and PDB files.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda libcifpp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
