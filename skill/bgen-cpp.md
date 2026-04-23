---
name: bgen-cpp
category: variant-calling
description: Reference implementation of the BGEN format for genetic data
tags: [bgen, genotypes, genetic-data, format]
author: oxo-call-community
source_url: "https://github.com/nebfield/bgen-git-mirror"
---

## Concepts
- **Tool Overview**: bgen-cpp is the reference C++ implementation of the BGEN (Binary GENotype) format, a file format for storing genetic variation data. It includes tools for working with BGEN files.
- **BGEN Format**: BGEN is a compressed binary format for storing genotype data, designed as a modern alternative to VCF/BCF with better compression and faster random access.
- **Tools Included**: `bgenix` (index and query BGEN files), `cat-bgen` (concatenate BGEN files), `edit-bgen` (modify BGEN metadata).
- **Applications**: Widely used in large-scale genetic studies, particularly by UK Biobank.

## Pitfalls
- **Indexing**: Large BGEN files should be indexed with `bgenix` for efficient random access.
- **Version Compatibility**: Different BGEN versions may have incompatible features.
- **Memory Usage**: Processing large BGEN files requires sufficient memory.

## Examples
### Index a BGEN file
**Args:** `bgenix -g data.bgen -index`
**Explanation:** Creates an index file for efficient random access.

### Query specific region
**Args:** `bgenix -g data.bgen -i data.bgen.bgi -r chr1:1000000-2000000`
**Explanation:** Extracts genotype data for a specific genomic region.

### Concatenate BGEN files
**Args:** `cat-bgen -g part1.bgen part2.bgen -o combined.bgen`
**Explanation:** Merges multiple BGEN files into one.
