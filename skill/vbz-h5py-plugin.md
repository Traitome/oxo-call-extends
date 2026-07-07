---
name: vbz-h5py-plugin
category: utility
description: VBZ HDF5 Plugin - Compression plugin for HDF5.
tags: [vbz-h5py-plugin, hdf5, compression, utility]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/vbz_compression"
---

## Concepts

- **Tool Overview**: VBZ HDF5 Plugin - A compression plugin for HDF5 files.
- **Core Function**: Provides compression for HDF5 files used in sequencing data.
- **Input**: HDF5 files.
- **Output**: Compressed HDF5 files.
- **Installation**: Install via conda or source
- **Use Case**: Data compression, bioinformatics.

## Pitfalls

- **Compatibility**: Requires compatible HDF5 version.
- **Performance**: Compression may slow down I/O.

## Examples

### Compress file
**Args:** `h5repack -f GZIP=9 input.h5 output.h5`
**Explanation:** Compress HDF5 file.

### With VBZ compression
**Args:** `h5repack -f VBZ=5 input.h5 output.h5`
**Explanation:** Use VBZ compression.
