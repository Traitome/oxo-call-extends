---
name: ucsc-bedgraphpack
category: utility
description: UCSC bedGraphPack - Tool for compressing bedGraph files.
tags: [ucsc-bedgraphpack, ucsc, bedgraph, compression, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedGraphPack - A tool for compressing bedGraph format files.
- **Core Function**: Compresses bedGraph data for efficient storage.
- **Input**: bedGraph format file.
- **Output**: Compressed bedGraph file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data compression, storage optimization, genome browser.

## Pitfalls

- **Format Requirements**: Requires proper bedGraph format.
- **Decompression**: Requires decompression for analysis.

## Examples

### Compress bedGraph
**Args:** `bedGraphPack input.bedgraph output.bedgraph.pack`
**Explanation:** Compress bedGraph file.

### Uncompress
**Args:** `bedGraphPack -unpack input.bedgraph.pack output.bedgraph`
**Explanation:** Decompress bedGraph file.
