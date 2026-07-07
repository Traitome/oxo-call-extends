---
name: dscr
category: formatting
description: "high-performance compression of sequencing reads stored in FASTQ format"
tags: [dscr, formatting, compression, FASTQ, sequencing]
author: oxo-call-community
source_url: "https://github.com/lrog/dsrc"
---

## Concepts

- **Tool Overview**: DSRC (DNA Sequence Reads Compression) is a high-performance compression tool for FASTQ sequencing data.
- **Core Function**: Compresses FASTQ files with high compression ratios while maintaining fast decompression speeds.
- **Input/Output**: Input: FASTQ files. Output: Compressed .dsrc files or decompressed FASTQ.
- **Algorithm**: Uses specialized compression algorithms optimized for sequencing data characteristics.
- **Key Features**: High compression ratio, fast decompression, lossless compression, multi-threading support.
- **Installation**: `conda install -c bioconda dscr`

## Pitfalls

- **Compression Time**: High compression ratios may require longer compression times.
- **Memory Usage**: Large files may require significant memory during compression.
- **Format Compatibility**: Only supports standard FASTQ format.
- **Version Compatibility**: Ensure same version for compression and decompression.
- **Quality Scores**: Quality score encoding must be properly handled.

## Examples

### Compress FASTQ file
**Args:** `compress input.fastq output.dsrc`
**Explanation:** Compresses FASTQ file to DSRC format.

### Decompress file
**Args:** `decompress input.dsrc output.fastq`
**Explanation:** Decompresses DSRC file back to FASTQ format.

### Fast compression mode
**Args:** `compress input.fastq output.dsrc --fast`
**Explanation:** Uses faster compression with slightly lower compression ratio.

### Maximum compression
**Args:** `compress input.fastq output.dsrc --best`
**Explanation:** Uses maximum compression for smallest file size.

### Multi-threaded compression
**Args:** `compress input.fastq output.dsrc --threads 8`
**Explanation:** Uses 8 threads for parallel compression.