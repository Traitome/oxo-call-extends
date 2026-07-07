---
name: ucsc-bigbednameditems
category: utility
description: UCSC bigBedNamedItems - Tool for extracting named items from BigBed files.
tags: [ucsc-bigbednameditems, ucsc, bigbed, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigBedNamedItems - A tool for extracting named items from BigBed files.
- **Core Function**: Retrieves items by name from indexed BigBed files.
- **Input**: BigBed file, name list.
- **Output**: Matching items from BigBed file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data extraction, feature retrieval, annotation lookup.

## Pitfalls

- **Name Matching**: Requires exact name matching.
- **Index Requirement**: Requires indexed BigBed file.

## Examples

### Extract named items
**Args:** `bigBedNamedItems input.bb names.txt > output.bed`
**Explanation:** Extract items by name from BigBed file.

### With output format
**Args:** `bigBedNamedItems -format=bed input.bb names.txt > output.bed`
**Explanation:** Extract with specified output format.
