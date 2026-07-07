---
name: dextractor
category: utility
description: DEXTRACTOR - Bax File Decoder and Data Compressor for PacBio data.
tags: [dextractor, utility, pacbio, hdf5, compression]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/DEXTRACTOR"
---

## Concepts

- **Tool Overview**: dextractor (v1.0p2+) is a tool for decoding PacBio BAX/HDF5 files and compressing sequence data. It provides efficient extraction and compression of PacBio sequencing data.
- **Core Function**: Extracts reads from PacBio HDF5 (bax.h5) files, converts them to FASTQ format, and compresses sequence data for storage efficiency.
- **Input/Output**: Input: PacBio bax.h5 files, optional auxiliary files. Output: FASTQ files, compressed sequence data, quality scores.
- **Algorithm**: Parses HDF5 format to extract raw sequence data and quality values, with optional compression using specialized algorithms.
- **Key Features**: PacBio HDF5 decoding, FASTQ conversion, data compression, quality score extraction, batch processing.
- **Installation**: `conda install -c bioconda dextractor`

## Pitfalls

- **Input Requirements**: Requires PacBio HDF5 format files (bax.h5).
- **File Compatibility**: May not support all PacBio data formats.
- **Compression Artifacts**: Aggressive compression may affect downstream analysis.
- **Memory Usage**: May require significant memory for large datasets.
- **Quality Scores**: Some older PacBio formats may have limited quality information.

## Examples

### Extract reads from BAX file
**Args:** `dextractor --bax input.bax.h5 --output reads.fastq`
**Explanation:** Extracts reads from PacBio HDF5 file to FASTQ format.

### With compression
**Args:** `dextractor --bax input.bax.h5 --output reads.fastq --compress`
**Explanation:** Compress output FASTQ file to save space.

### Batch processing
**Args:** `dextractor --bax-dir bax_files/ --output-dir fastq_files/`
**Explanation:** Process multiple BAX files in batch.

### Extract quality scores only
**Args:** `dextractor --bax input.bax.h5 --output qualities.txt --quality-only`
**Explanation:** Extract only quality scores without sequence data.

### Generate summary statistics
**Args:** `dextractor --bax input.bax.h5 --output reads.fastq --stats stats.txt`
**Explanation:** Generate summary statistics during extraction.