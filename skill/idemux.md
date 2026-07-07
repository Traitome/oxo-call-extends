---
name: idemux
category: utility
description: A Lexogen tool for demultiplexing and index error correcting fastq files. Works with Lexogen i7, i5 and i1 barcodes with support for QuantSeq-Pool libraries.
tags: [idemux, utility, FASTQ, demultiplexing, barcode, QuantSeq]
author: oxo-call-community
source_url: "https://github.com/lexogen-tools/idemux"
---

## Concepts

- **Demultiplexing**: Separates pooled sequencing reads into individual samples based on index barcodes.
- **Index Error Correction**: Built-in error correction to maximize data output by rescuing reads with index errors.
- **Triple-index Support**: Designed for Lexogen's triple-indexed QuantSeq-Pool libraries with i7, i5, and i1 barcodes.
- **UMI Handling**: Supports Unique Molecular Identifiers for accurate read deduplication.
- **Base Quality Filtering**: Filters low-quality reads and indices to improve data quality.

## Pitfalls

- **Library Type Compatibility**: Optimized for Lexogen library prep kits; may not work optimally with other platforms.
- **Barcode Whitelist**: Requires proper barcode whitelist configuration; incorrect lists cause misassignment.
- **Index Orientation**: Must specify correct index orientation (forward/reverse complement) for accurate demultiplexing.
- **File Format**: Requires specific input file formats; conversion may be needed for non-standard formats.
- **Performance**: Large datasets may require significant processing time; parallelization recommended.

## Examples

### Basic demultiplexing
**Args:** `idemux --input input.fastq --output output_dir --barcodes barcodes.txt`
**Explanation:** Demultiplexes input FASTQ file using specified barcode file.

### Error correction enabled
**Args:** `idemux --input input.fastq --output output_dir --barcodes barcodes.txt --correct`
**Explanation:** Enables index error correction to rescue reads with sequencing errors in barcodes.

### Triple-index processing
**Args:** `idemux --input input.fastq --output output_dir --i7 i7.txt --i5 i5.txt --i1 i1.txt`
**Explanation:** Processes triple-indexed data with separate files for each index type.

### Quality filtering options
**Args:** `idemux --input input.fastq --output output_dir --barcodes barcodes.txt --min-quality 25 --max-mismatches 2`
**Explanation:** Filters reads with quality < 25 and allows up to 2 mismatches in index sequences.

### Paired-end mode
**Args:** `idemux --input read1.fastq --input2 read2.fastq --output output_dir --barcodes barcodes.txt`
**Explanation:** Processes paired-end sequencing data with two input FASTQ files.