---
name: tabixpp
category: indexing
description: C++ wrapper around tabix for fast random access to genomic position files.
tags: [tabixpp, indexing, c++, vcf]
author: oxo-call-community
source_url: "https://github.com/vcflib/tabixpp"
---

## Concepts

- **Tool Overview**: tabixpp (v1.1.2) is a C++ wrapper for tabix indexing library.
- **Core Function**: Provides C++ API for tabix indexing and querying.
- **Algorithm**: Wraps htslib tabix functionality in C++ classes.
- **Input/Output**: Input: Tab-delimited files; Output: Indexed files.
- **Applications**: Integration into C++ bioinformatics tools, fast interval queries.
- **Installation**: `conda install -c bioconda tabixpp` or download from GitHub.

## Pitfalls

- **C++ Dependencies**: Requires proper C++ compilation environment.
- **Linking**: May require linking against htslib.
- **Memory Management**: Requires careful memory handling in C++ code.
- **Index Format**: Must match tabix index format.
- **Coordinate System**: Uses 1-based indexing.
- **Error Handling**: Requires proper error checking in code.

## Examples

### Display help
**Args:** `tabixpp --help`
**Explanation:** Shows available options and usage information.

### Index file
**Args:** `tabixpp index -i input.txt.gz`
**Explanation:** Create tabix index for gzipped file.

### Query region
**Args:** `tabixpp query -i input.txt.gz -r chr1:1000-2000`
**Explanation:** Query specific genomic region.

### Extract to file
**Args:** `tabixpp query -i input.txt.gz -r chr1:1-1000000 -o output.txt`
**Explanation:** Extract region to output file.

### Multiple regions
**Args:** `tabixpp query -i input.txt.gz -r chr1:1-1000000 chr2:500000-1500000`
**Explanation:** Query multiple regions.

### Using BED file
**Args:** `tabixpp query -i input.txt.gz -b regions.bed`
**Explanation:** Query using BED file regions.

### List sequences
**Args:** `tabixpp list -i input.txt.gz`
**Explanation:** List all sequences in indexed file.

### Check index
**Args:** `tabixpp check -i input.txt.gz`
**Explanation:** Verify index validity.

### Convert format
**Args:** `tabixpp convert -i input.txt.gz -o output.bed`
**Explanation:** Convert indexed file format.
