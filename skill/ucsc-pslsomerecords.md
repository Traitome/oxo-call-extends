---
name: ucsc-pslsomerecords
category: utility
description: UCSC pslSomeRecords - Tool for extracting some PSL records.
tags: [ucsc-pslsomerecords, ucsc, psl, extraction, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslSomeRecords - A tool for extracting specific PSL records.
- **Core Function**: Extracts subsets of PSL records.
- **Input**: PSL file, ID list.
- **Output**: Extracted PSL records.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data extraction, subset selection, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Extract some records
**Args:** `pslSomeRecords ids.txt input.psl > subset.psl`
**Explanation:** Extract specific records.

### With options
**Args:** `pslSomeRecords -verbose ids.txt input.psl > subset.psl`
**Explanation:** Extract with verbose output.
