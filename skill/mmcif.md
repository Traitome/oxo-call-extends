---
name: mmcif
category: programming
description: mmCIF Core Access Library
tags: [mmcif, programming, pdb]
author: oxo-call-community
source_url: "https://rcsb.github.io/py-mmcif"
---

## Concepts

- **Tool Overview**: mmcif v1.1.0 provides Python API for mmCIF data files and dictionaries.
- **Core Function**: mmCIF Core Access Library for macromolecular structure data.
- **PDB Integration**: Supports Protein Data Bank (PDB) format operations.
- **Data Access**: Provides native Python API for mmCIF files.
- **Input/Output**: Accepts mmCIF files; outputs structured data.
- **Structural Biology**: Supports macromolecular structure analysis.

## Pitfalls

- **Format Specific**: Designed for mmCIF format files.
- **Memory Requirements**: Memory usage depends on file size.
- **Parameter Tuning**: May require API parameter adjustment.
- **Data Quality**: Results depend on input file quality.
- **Version Compatibility**: May require specific Python versions.
- **Schema Knowledge**: Requires understanding of mmCIF schema.

## Examples

### Parse mmCIF file
**Args:** `python -c "from mmcif.io.IoAdapterCore import IoAdapterCore; io = IoAdapterCore(); data = io.readFile('structure.cif')"`
**Explanation:** Reads mmCIF file using Python API.

### Write mmCIF file
**Args:** `python -c "from mmcif.io.IoAdapterCore import IoAdapterCore; io = IoAdapterCore(); io.writeFile('output.cif', data)"`
**Explanation:** Writes data to mmCIF file.

### Access data items
**Args:** `python -c "from mmcif.io.IoAdapterCore import IoAdapterCore; io = IoAdapterCore(); data = io.readFile('structure.cif'); print(data['_entry.id'])"`
**Explanation:** Accesses specific data items.

### Validate mmCIF
**Args:** `python -c "from mmcif.io.IoAdapterCore import IoAdapterCore; io = IoAdapterCore(); result = io.validateFile('structure.cif')"`
**Explanation:** Validates mmCIF file format.

### Batch processing
**Args:** `python script.py cif/`
**Explanation:** Processes multiple mmCIF files.