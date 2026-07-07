---
name: pairix
category: utility
description: pairix provides 2D indexing on bgzipped text files of paired genomic coordinates.
tags: [pairix, utility, indexing, genomic-coordinates]
author: oxo-call-community
source_url: "https://github.com/4dn-dcic/pairix"
---

## Concepts

- **Tool Overview**: pairix indexes and queries paired genomic coordinates.
- **Core Function**: Creates 2D index for efficient querying.
- **Algorithm**: Uses bgzip compression and binary indexing.
- **Input Format**: Accepts tab-delimited files with paired coordinates.
- **Output**: Produces indexed files and query results.
- **Use Case**: Hi-C analysis, chromatin interaction data, and genomic data querying.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Index Size**: Index files can be large.
- **Format Requirements**: Requires specific input format.
- **Query Complexity**: Complex queries may be slow.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pairix --help`
**Explanation:** Shows available options and usage instructions.

### Create index
**Args:** `pairix -f pairs.txt`
**Explanation:** Creates index for pairs file.

### Query pairs
**Args:** `pairix pairs.txt chr1:1000-2000 chr2:3000-4000`
**Explanation:** Queries pairs in specified regions.

### List chromosomes
**Args:** `pairix -l pairs.txt`
**Explanation:** Lists chromosomes in file.

### Statistics
**Args:** `pairix -s pairs.txt`
**Explanation:** Shows statistics about pairs file.

### Verbose mode
**Args:** `pairix -v pairs.txt chr1:1000-2000 chr2:3000-4000`
**Explanation:** Runs with verbose output.

### Batch query
**Args:** `pairix -r regions.txt pairs.txt`
**Explanation:** Queries multiple regions from file.