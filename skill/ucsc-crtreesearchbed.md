---
name: ucsc-crtreesearchbed
category: utility
description: UCSC crTreeSearchBed - Tool for searching indexed BED files.
tags: [ucsc-crtreesearchbed, ucsc, search, bed, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC crTreeSearchBed - A tool for searching crTree-indexed BED files.
- **Core Function**: Performs fast spatial queries on indexed BED data.
- **Input**: Indexed BED file, query regions.
- **Output**: Matching regions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Fast querying, genome browser, data retrieval.

## Pitfalls

- **Index Requirement**: Requires pre-built crTree index.
- **Query Format**: Requires proper query format.

## Examples

### Search BED file
**Args:** `crTreeSearchBed index.idx query.bed > results.bed`
**Explanation:** Search indexed BED file.

### With options
**Args:** `crTreeSearchBed -overlap=50 index.idx query.bed > results.bed`
**Explanation:** Search with minimum overlap requirement.
