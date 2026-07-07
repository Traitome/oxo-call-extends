---
name: lrzip
category: utility
description: Long Range ZIP or Lzma RZIP. Compression program optimised for large files.
tags: [lrzip, utility, compression, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ckolivas/lrzip"
---

## Concepts

- **Tool Overview**: lrzip v0.651 is a compression program optimized for large files, particularly those larger than 100MB.
- **Core Function**: Uses a unique "long range" compression algorithm that finds repeated patterns across large distances.
- **Compression Strategy**: Combines LZ77 compression with LZMA, BZIP2, or ZPAQ for high compression ratios.
- **Input/Output**: Input: Any file type; Output: Compressed .lrz file or decompressed original file.
- **Installation**: `conda install -c bioconda lrzip` or `sudo apt install lrzip`
- **Key Features**: Excellent compression for large bioinformatics files (FASTQ, BAM, VCF), supports multiple compression levels.

## Pitfalls

- **Memory Usage**: Higher compression levels require significant memory (may need >1GB for large files).
- **Decompression Speed**: High-compression files may take longer to decompress.
- **File Size**: Best suited for files >100MB; overhead may not be worth it for small files.
- **Parallel Processing**: Compression is single-threaded, which can be slow for very large files.
- **Compatibility**: Requires lrzip to decompress; not as widely supported as gzip/bzip2.
- **Corruption Risk**: Corrupted .lrz files may be difficult to recover.

## Examples

### Compress file
**Args:** `lrzip -o output.lrz input.fastq`
**Explanation:** Compresses input.fastq to output.lrz using default settings.

### Maximum compression
**Args:** `lrzip -z -o output.lrz input.bam`
**Explanation:** Uses maximum compression level (LZMA) for best compression ratio.

### Fast compression
**Args:** `lrzip -f -o output.lrz input.vcf`
**Explanation:** Uses fast compression mode for quicker processing.

### Decompress file
**Args:** `lrunzip input.lrz`
**Explanation:** Decompresses input.lrz to original file.

### Test compressed file
**Args:** `lrzip -t input.lrz`
**Explanation:** Verifies integrity of compressed file.

### Help documentation
**Args:** `lrzip --help`
**Explanation:** Displays all available compression options and parameters.