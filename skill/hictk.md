---
name: hictk
category: bioinformatics
description: hictk is a fast toolkit for working with .hic and .cool Hi-C data files.
tags: [hictk, Hi-C, bioinformatics]
author: oxo-call-community
source_url: "https://hictk.readthedocs.io/en/stable/"
---

## Concepts

- **Hi-C Toolkit**: hictk provides tools for Hi-C data processing.

- **.hic Format**: Supports Juicer's .hic format.

- **.cool Format**: Supports cooler's .cool format.

- **Fast Processing**: Optimized for speed.

- **Data Conversion**: Converts between Hi-C formats.

- **Matrix Operations**: Performs matrix operations on Hi-C data.

## Pitfalls

- **File Compatibility**: Ensure compatibility between formats.

- **Memory Usage**: Large files may require significant memory.

- **Performance**: May have performance considerations.

- **Version Compatibility**: Ensure compatibility with file versions.

- **Data Integrity**: Verify data integrity after operations.

## Examples

### Convert .hic to .cool
**Args:** `hictk convert input.hic output.cool`
**Explanation:** Converts .hic file to .cool format.

### Extract matrix
**Args:** `hictk extract input.cool chr1 chr2 > contacts.txt`
**Explanation:** Extracts contacts between chromosomes.

### Merge matrices
**Args:** `hictk merge -o merged.cool sample1.cool sample2.cool`
**Explanation:** Merges multiple Hi-C matrices.

### Batch processing
**Args:** `for f in *.hic; do hictk convert $f ${f%.hic}.cool; done`
**Explanation:** Converts multiple .hic files.

### Help command
**Args:** `hictk --help`
**Explanation:** Shows available options and usage information.