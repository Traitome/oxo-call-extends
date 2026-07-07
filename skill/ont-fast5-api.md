---
name: ont-fast5-api
category: programming
description: ONT fast5 API provides access to Oxford Nanopore Technologies raw sequencing data.
tags: [ont-fast5-api, programming, nanopore, sequencing]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/ont_fast5_api"
---

## Concepts

- **Tool Overview**: ONT fast5 API enables reading and writing fast5 files.
- **Core Function**: Provides Python interface for fast5 file manipulation.
- **Algorithm**: Uses HDF5 format for efficient data storage.
- **Input Format**: Accepts fast5 raw data files.
- **Output**: Produces modified fast5 files and extracted data.
- **Use Case**: Nanopore sequencing analysis, raw data processing, and basecalling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **File Format**: Requires proper fast5 format.
- **Memory Usage**: Large files require memory.
- **HDF5 Dependencies**: Requires HDF5 libraries.
- **Performance**: Reading large datasets can be slow.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "from ont_fast5_api import Fast5File; help(Fast5File)"`
**Explanation:** Shows available options and usage instructions.

### Read fast5
**Args:** `python -c "from ont_fast5_api import Fast5File; f5 = Fast5File('reads.fast5')"`
**Explanation:** Reads fast5 file.

### List reads
**Args:** `python -c "reads = list(f5.get_reads()); print(len(reads))"`
**Explanation:** Lists all reads in fast5 file.

### Extract raw data
**Args:** `python -c "raw_data = read.get_raw_data()"`
**Explanation:** Extracts raw signal data.

### Write fast5
**Args:** `python -c "f5.write('output.fast5')"`
**Explanation:** Writes modified fast5 file.

### Batch processing
**Args:** `python -c "for f in fast5_files: process_fast5(f)"`
**Explanation:** Processes multiple fast5 files.

### Close file
**Args:** `python -c "f5.close()"`
**Explanation:** Closes fast5 file.