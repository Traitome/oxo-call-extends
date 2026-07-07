---
name: libcifpp
category: structural-biology
description: Library for manipulating mmCIF and PDB structure files
tags: [libcifpp, structural-biology, mmCIF, PDB, protein-structure]
author: oxo-call-community
source_url: "https://github.com/PDB-REDO/libcifpp"
---

## Concepts

- **mmCIF Handling**: Manipulation of mmCIF format files
- **PDB Support**: Support for PDB format
- **Validation**: Ensures file validity against dictionaries
- **Data Parsing**: Parsing and processing structural data
- **File Conversion**: Conversion between formats
- **Dictionary Validation**: Validates against CIF dictionaries

## Pitfalls

- **Format Complexity**: mmCIF format is complex
- **Dictionary Dependencies**: Requires proper dictionary files
- **Version Incompatibilities**: Different mmCIF versions
- **Large Files**: Very large structure files may cause issues
- **Memory Usage**: Memory-intensive for large structures
- **Parsing Errors**: Invalid files may cause parsing failures

## Examples

### Read mmCIF file
**Args:** `cifpp read -i structure.cif -o parsed.json`
**Explanation:** Reads and parses mmCIF file.

### Validate file
**Args:** `cifpp validate -i structure.cif -d dictionary.dic`
**Explanation:** Validates mmCIF against dictionary.

### Convert to PDB
**Args:** `cifpp convert -i structure.cif -o structure.pdb`
**Explanation:** Converts mmCIF to PDB format.

### Extract data
**Args:** `cifpp extract -i structure.cif -f author -o author.txt`
**Explanation:** Extracts specific field from mmCIF.

### Modify file
**Args:** `cifpp modify -i structure.cif -s title="New Title" -o modified.cif`
**Explanation:** Modifies field in mmCIF file.

### Statistics
**Args:** `cifpp stats -i structure.cif`
**Explanation:** Shows file statistics.