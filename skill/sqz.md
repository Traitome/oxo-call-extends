---
name: sqz
category: graph-genomics
description: SQZ - Tool for compressing and decompressing path annotations in GFA files
tags: [sqz, graph-genomics, gfa, compression, path-annotations]
author: oxo-call-community
source_url: "https://github.com/codialab/sqz"
---

## Concepts

- **Tool Overview**: sqz (v0.2.0) - A GFA compression tool
- **Core Function**: Compresses and decompresses path annotations in GFA files
- **Input/Output**: Accepts GFA files; outputs compressed GFA files
- **Algorithm**: Path annotation compression algorithms
- **Installation**: `conda install -c bioconda sqz`
- **Key Features**: GFA compression, path annotations, storage optimization

## Pitfalls

- **Input Requirements**: Requires properly formatted GFA files
- **Path Annotation**: Path annotation structure affects compression
- **Compression Ratio**: Ratio depends on annotation characteristics
- **Memory Usage**: Large GFA files require significant memory
- **Output Format**: Output format depends on configuration
- **Decompression**: Requires SQZ for decompression

## Examples

### Display help
**Args:** `sqz --help`
**Explanation:** Shows available options and usage information.

### Basic GFA compression
**Args:** `sqz -i graph.gfa -o compressed.gfa`
**Explanation:** Compress GFA path annotations.

### Decompression
**Args:** `sqz -i compressed.gfa -o decompressed.gfa --decompress`
**Explanation:** Decompress GFA file.

### With compression level
**Args:** `sqz -i graph.gfa -o compressed.gfa --level 9`
**Explanation:** Set compression level.

### Multiple files
**Args:** `sqz -i graph1.gfa graph2.gfa -o compressed.gfa`
**Explanation:** Compress multiple GFA files.

### Output detailed results
**Args:** `sqz -i graph.gfa -o compressed.gfa --detailed`
**Explanation:** Output detailed compression information.

### Output statistics
**Args:** `sqz -i graph.gfa -o compressed.gfa --stats`
**Explanation:** Output compression statistics.

### Generate report
**Args:** `sqz -i graph.gfa -o compressed.gfa --report`
**Explanation:** Generate compression report.

### With threads
**Args:** `sqz -i graph.gfa -o compressed.gfa -p 8`
**Explanation:** Use multiple threads for compression.