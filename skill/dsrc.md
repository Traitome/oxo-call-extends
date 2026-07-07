---
name: dsrc
category: formatting
description: "High-performance compression of sequencing reads stored in FASTQ format."
tags: [dsrc, formatting, compression, FASTQ, sequencing]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/DSRC"
---

## Concepts

- **Tool Overview**: DSRC is a high-performance compression tool specifically designed for FASTQ sequencing data.
- **Core Function**: Compresses FASTQ files with high compression ratios while maintaining fast decompression speeds.
- **Input/Output**: Input: FASTQ files. Output: Compressed .dsrc files or decompressed FASTQ.
- **Algorithm**: Uses specialized compression algorithms optimized for DNA sequences and quality scores.
- **Key Features**: High compression ratio, fast decompression, multi-threading support, quality score compression.
- **Installation**: `conda install -c bioconda dsrc`

## Pitfalls

- **Compression Speed**: High compression modes are slower than fast modes.
- **Memory Usage**: Large files may require significant memory.
- **Format Compatibility**: Only supports standard FASTQ format.
- **Version Compatibility**: Use same version for compression and decompression.
- **Quality Encoding**: Handles various quality score encodings (Phred+33, Phred+64).

## Examples

### Compress FASTQ file
**Args:** `compress input.fastq output.dsrc`
**Explanation:** Compresses FASTQ file to DSRC format.

### Decompress file
**Args:** `decompress input.dsrc output.fastq`
**Explanation:** Decompresses DSRC file back to FASTQ format.

### Fast compression mode
**Args:** `compress input.fastq output.dsrc -m 0`
**Explanation:** Uses fastest compression mode.

### Maximum compression
**Args:** `compress input.fastq output.dsrc -m 2`
**Explanation:** Uses maximum compression mode.

### Multi-threaded compression
**Args:** `compress input.fastq output.dsrc -t 8`
**Explanation:** Uses 8 threads for parallel compression.