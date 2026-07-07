---
name: naf
category: formatting
description: NAF - Compressed binary file format for sequence data
tags: [naf, formatting, compression, sequence, binary, fasta, fastq]
author: oxo-call-community
source_url: "https://github.com/KirillKryukov/naf"
---

## Concepts

- **Tool Overview**: NAF v1.3.0 is a highly efficient compressed binary format for DNA, RNA, and protein sequence data. It provides significantly better compression than gzip while enabling fast random access to sequences.
- **Core Function**: Compresses FASTA/FASTQ files into NAF format for storage efficiency, with full support for decompressing back to original formats. Supports random access to individual sequences without decompressing the entire file.
- **Compression Algorithm**: Uses advanced compression techniques optimized for biological sequences, achieving ~40% smaller files compared to gzip while maintaining fast decompression speeds.
- **Input Format**: Accepts FASTA and FASTQ files (gzipped or uncompressed) for compression. For decompression, accepts NAF files.
- **Output**: Produces compressed NAF files during compression, or decompresses to FASTA/FASTQ format. Supports streaming operations for large files.
- **Use Case**: Large-scale sequencing data archival, reducing storage requirements for genomics projects, fast sequence retrieval from compressed databases, and efficient data transfer.

## Pitfalls

- **Format Conversion**: NAF is not natively supported by most bioinformatics tools. Always keep original FASTA/FASTQ for tools that don't support NAF.
- **Random Access Overhead**: While random access is supported, it requires index files (.nafi) which must be created separately.
- **Compression Time**: Compression is slower than gzip but worthwhile for frequently accessed data. Decompression is fast.
- **Lossless**: Compression is fully lossless. No sequence information is lost during compression/decompression cycles.
- **Line Endings**: FASTQ quality scores with different line ending conventions may have minor differences after round-trip.
- **Metadata Handling**: Some sequence metadata (read headers) may be normalized during compression.

## Examples

### Compress FASTA file
**Args:** `naf -c input.fasta -o output.naf`
**Explanation:** Standard compression. Creates compressed NAF file from FASTA input.

### Compress FASTQ file
**Args:** `naf -c reads.fastq.gz -o compressed.naf`
**Explanation:** Compresses gzipped FASTQ directly. NAF achieves better compression than gzip.

### Decompress NAF file
**Args:** `naf -d input.naf -o output.fasta`
**Explanation:** Standard decompression. Recovers original FASTA/FASTQ from NAF.

### Create with random access index
**Args:** `naf -c sequences.fasta -o indexed.naf -i`
**Explanation:** Creates NAF with embedded index for fast random access to individual sequences.

### Extract single sequence by name
**Args:** `naf -d indexed.naf -s "chr1" -o chr1.fasta`
**Explanation:** Random access extraction. Retrieves only the sequence named "chr1" without decompressing entire file.

### Display help
**Args:** `--help`
**Explanation:** Shows all compression options and usage information.
