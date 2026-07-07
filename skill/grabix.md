---
name: grabix
category: bioinformatics
description: grabix provides random access to BGZF-compressed files, enabling fast retrieval of specific regions without decompressing the entire file.
tags: [grabix, BGZF, random-access, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/arq5x/grabix"
---

## Concepts

- **BGZF Random Access**: grabix enables fast random access to BGZF-compressed files, a common compression format in bioinformatics.

- **Indexing**: Creates indexes for BGZF files to quickly locate compressed blocks containing specific data.

- **Range Extraction**: Extracts specific ranges or regions from compressed files efficiently.

- **Stream Integration**: Works seamlessly with command-line pipelines and streaming operations.

- **Multiple Format Support**: Supports various bioinformatics formats stored in BGZF format.

- **Performance**: Significantly faster than decompressing entire files for region-specific queries.

## Pitfalls

- **BGZF Format**: Only works with BGZF-compressed files, not standard gzip.

- **Index Generation**: Indexes must be generated before querying. Missing indexes will cause errors.

- **File Compatibility**: Ensure files are properly BGZF-compressed. Invalid files may produce unexpected results.

- **Coordinate System**: Be aware of coordinate systems (0-based vs 1-based) when specifying regions.

- **Memory Usage**: Very large regions may require significant memory for decompression.

## Examples

### Create index for BGZF file
**Args:** `grabix index data.txt.gz`
**Explanation:** Creates an index file for BGZF-compressed data.

### Extract specific lines
**Args:** `grabix grab data.txt.gz 100 200`
**Explanation:** Extracts lines 100-200 from the compressed file.

### Extract by byte offset
**Args:** `grabix grab data.txt.gz --offset 1000 --length 500`
**Explanation:** Extracts 500 bytes starting from offset 1000.

### Stream extraction
**Args:** `grabix grab data.txt.gz 1 1000 | head -50`
**Explanation:** Extracts first 1000 lines and pipes to head command.

### Check index status
**Args:** `grabix check data.txt.gz`
**Explanation:** Verifies if an index exists for the file.

### Batch extraction
**Args:** `grabix batch data.txt.gz regions.txt`
**Explanation:** Extracts multiple regions specified in a file.

### Output to file
**Args:** `grabix grab data.txt.gz 500 600 -o extracted.txt`
**Explanation:** Extracts lines 500-600 and saves to output file.