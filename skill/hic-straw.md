---
name: hic-straw
category: bioinformatics
description: hic-straw provides Python bindings for reading .hic files using pybind11.
tags: [hic-straw, Hi-C, data-format, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/aidenlab/straw/wiki"
---

## Concepts

- **.hic Format**: hic-straw reads .hic format files.

- **Hi-C Data**: Extracts Hi-C contact data.

- **Python Bindings**: Provides Python interface via pybind11.

- **Data Extraction**: Extracts contact matrices from .hic files.

- **Multi-resolution**: Supports multi-resolution data.

- **Juicer Integration**: Works with Juicer-generated .hic files.

## Pitfalls

- **File Compatibility**: Ensure compatibility with .hic format versions.

- **Memory Usage**: Large .hic files may require significant memory.

- **Resolution**: Choose appropriate resolution.

- **Data Integrity**: Verify data integrity after extraction.

- **Network Access**: Remote files require network access.

## Examples

### Extract Hi-C data
**Args:** `straw NONE input.hic chr1 chr2 BP 10000`
**Explanation:** Extracts contacts between chr1 and chr2 at 10kb resolution.

### With Python API
**Args:** `python -c "import straw; result = straw.straw('NONE', 'input.hic', 'chr1', 'chr2', 'BP', 10000)"`
**Explanation:** Uses Python API to extract data.

### Batch extraction
**Args:** `for chr in chr1 chr2 chr3; do straw NONE input.hic $chr $chr BP 10000 > ${chr}_contacts.txt; done`
**Explanation:** Extracts contacts for multiple chromosomes.

### All-to-all
**Args:** `straw NONE input.hic ALL ALL BP 10000 > all_contacts.txt`
**Explanation:** Extracts all contacts.

### Help command
**Args:** `straw --help`
**Explanation:** Shows available options and usage information.