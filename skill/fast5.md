---
name: fast5
category: programming
description: "A C++ header-only library for reading Oxford Nanopore Fast5 files."
tags: [fast5, programming, Nanopore, sequencing-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/mateidavid/fast5"
---

## Concepts

- **Tool Overview**: fast5 is a C++ header-only library for reading Oxford Nanopore Fast5 files, which store raw sequencing data.
- **Core Function**: Provides efficient reading and parsing of Fast5 files containing nanopore sequencing data.
- **Input/Output**: Input: Fast5 file. Output: Raw signal data, sequence information, metadata.
- **Algorithm**: Parses HDF5-based Fast5 format to extract sequencing data.
- **Key Features**: Fast5 parsing, raw signal extraction, metadata access, header-only library, efficient memory usage.
- **Installation**: `conda install -c bioconda fast5`

## Pitfalls

- **File Format**: Requires Fast5 format version compatibility.
- **Memory Usage**: Large Fast5 files may require significant memory.
- **Dependency**: Requires HDF5 library.
- **File Corruption**: Corrupted Fast5 files may cause parsing errors.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Read Fast5 file
**Args:** `fast5 read -i data.fast5 -o raw_signal.txt`
**Explanation:** Extracts raw signal from Fast5 file.

### Get metadata
**Args:** `fast5 metadata -i data.fast5 -o metadata.json`
**Explanation:** Extracts metadata from Fast5 file.

### List reads
**Args:** `fast5 list -i data.fast5`
**Explanation:** Lists all reads in Fast5 file.

### Extract sequences
**Args:** `fast5 extract -i data.fast5 -o sequences.fasta`
**Explanation:** Extracts base-called sequences.

### Batch processing
**Args:** `fast5 batch -i fast5_files/ -o output/`
**Explanation:** Processes multiple Fast5 files in batch mode.