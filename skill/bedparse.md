---
name: bedparse
category: formatting
description: A simple library and CLI tool to manipulate BED files
tags: [bed, parsing, format-validation, genomic-intervals]
author: oxo-call-community
source_url: "https://github.com/tleonardi/bedparse"
---

## Concepts
- **Tool Overview**: bedparse is a Python-based CLI tool and library for manipulating and validating BED files. It provides utilities for parsing, filtering, and transforming BED format data.
- **BED Format**: BED (Browser Extensible Data) is a tab-separated format for describing genomic intervals with 3 required columns (chrom, start, end) and up to 9 optional columns.
- **Validation**: bedparse can validate BED files for proper formatting, coordinate consistency, and column structure.

## Pitfalls
- **Coordinate System**: BED uses 0-based half-open coordinates. Start positions are 0-based and end positions are exclusive.
- **Column Count**: BED files can have 3-12 columns. bedparse handles variable column counts but may require specification of expected format.

## Examples
### Validate a BED file
**Args:** `bedparse validate input.bed`
**Explanation:** Validates the format and structure of a BED file, reporting any issues.

### Filter BED by chromosome
**Args:** `bedparse filter --chrom chr1 input.bed > chr1.bed`
**Explanation:** Filters BED records to keep only those on chromosome 1.

### Convert BED3 to BED6
**Args:** `bedparse pad --name N/A --score 0 --strand . input.bed3 > output.bed6`
**Explanation:** Converts a 3-column BED file to 6-column format by adding placeholder name, score, and strand values.
