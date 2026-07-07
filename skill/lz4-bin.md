---
name: lz4-bin
category: utility
description: Extremely Fast Compression Application
tags: [lz4-bin, utility, compression]
author: oxo-call-community
source_url: "http://cyan4973.github.io/lz4"
---

## Concepts

- **Tool Overview**: lz4-bin v131 is an extremely fast compression application with high compression ratio.
- **Core Function**: Provides fast compression and decompression with minimal CPU usage.
- **Speed Performance**: Known for extremely fast decompression speed (~1GB/s per core).
- **Input/Output**: Input: Any file type; Output: Compressed .lz4 file or decompressed original.
- **Installation**: `conda install -c bioconda lz4-bin`
- **Key Features**: Ultra-fast compression, good compression ratio, supports large files.

## Pitfalls

- **Compression Ratio**: Lower compression ratio compared to gzip or bzip2.
- **Compatibility**: Less widely supported than gzip; requires lz4 to decompress.
- **File Size**: Best suited for large files; overhead may not be worth it for small files.
- **Memory Usage**: May require significant memory for very large files.
- **Corruption Risk**: Corrupted files may be difficult to recover.
- **Single-threaded**: Compression is single-threaded; may not fully utilize multi-core systems.

## Examples

### Compress file
**Args:** `lz4 input.fastq output.lz4`
**Explanation:** Compresses input file using LZ4 compression.

### Decompress file
**Args:** `lz4 -d input.lz4 output.fastq`
**Explanation:** Decompresses LZ4 compressed file.

### Maximum compression
**Args:** `lz4 -9 input.fastq output.lz4`
**Explanation:** Uses maximum compression level.

### Fast compression
**Args:** `lz4 -1 input.fastq output.lz4`
**Explanation:** Uses fastest compression mode.

### Stream compression
**Args:** `cat input.fastq | lz4 > output.lz4`
**Explanation:** Compresses data from stdin.

### Help documentation
**Args:** `lz4 --help`
**Explanation:** Displays all available compression options.