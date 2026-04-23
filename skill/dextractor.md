---
name: dextractor
category: utility
description: Bax File Decoder and Data Compressor for PacBio data.
tags: [dextractor, utility, pacbio, hdf5, compression]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/DEXTRACTOR"
---

## Concepts

- **Tool Overview**: DEXTRACTOR v1.0p2 - Tool for decoding PacBio BAX/HDF5 files and compressing sequence data.
- **Core Function**: Extracts and converts PacBio HDF5 (bax.h5) files to FASTQ format and compresses sequence data.
- **Input/Output**: Expects PacBio bax.h5 files; outputs FASTQ files and compressed data.
- **Installation**: `conda install -c bioconda dextractor`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires PacBio HDF5 format files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dextractor --bax input.bax.h5 --output reads.fastq`
**Explanation:** Extracts reads from PacBio HDF5 file to FASTQ.
