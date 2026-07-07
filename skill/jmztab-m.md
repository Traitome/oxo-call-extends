---
name: jmztab-m
category: formatting
description: Reference reader, writer and validator implementation for mzTab for metabolomics 2.0+.
tags: [jmztab-m, formatting, metabolomics, mzTab, validation]
author: oxo-call-community
source_url: "https://github.com/lifs-tools/jmztab-m"
---

## Concepts

- **Tool Overview**: jmztab-m (v1.0.6) - Reference implementation for reading, writing and validating mzTab files for metabolomics.
- **mzTab Format**: Implements the mzTab standard format for metabolomics data.
- **File Reading**: Reads mzTab files into structured data objects.
- **File Writing**: Writes metabolomics data to mzTab format.
- **Validation**: Validates mzTab files against the specification.
- **Metabolomics Data**: Handles identification and quantification data.

## Pitfalls

- **Format Version**: Different mzTab versions have different specifications.
- **Required Fields**: Missing required fields can cause validation errors.
- **Data Consistency**: Inconsistent data types can cause parsing errors.
- **Controlled Vocabularies**: Must use correct CV terms.
- **File Size**: Very large mzTab files require significant memory.
- **Encoding Issues**: Character encoding can affect parsing.

## Examples

### Validate mzTab file
**Args:** `jmztab-m validate --input results.mztab`
**Explanation:** Validates an mzTab file against the specification.

### Convert to JSON
**Args:** `jmztab-m convert --input results.mztab --output results.json`
**Explanation:** Converts mzTab file to JSON format.

### Extract metadata
**Args:** `jmztab-m extract --input results.mztab --metadata --output metadata.txt`
**Explanation:** Extracts metadata from mzTab file.

### Filter by score
**Args:** `jmztab-m filter --input results.mztab --min-score 0.9 --output filtered.mztab`
**Explanation:** Filters identifications by confidence score.

### Merge mzTab files
**Args:** `jmztab-m merge --input file1.mztab file2.mztab --output merged.mztab`
**Explanation:** Merges multiple mzTab files into one.

### Check format version
**Args:** `jmztab-m version --input results.mztab`
**Explanation:** Displays the mzTab format version of a file.