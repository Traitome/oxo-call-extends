---
name: ont_vbz_hdf_plugin
category: utility
description: VBZ compression plugin for Oxford Nanopore Technologies signal data.
tags: [ont_vbz_hdf_plugin, utility, compression, nanopore]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/vbz_compression"
---

## Concepts

- **Tool Overview**: VBZ compression plugin provides efficient compression for nanopore data.
- **Core Function**: Compresses raw nanopore signal data in HDF5 format.
- **Algorithm**: Uses VBZ compression algorithm optimized for nanopore signals.
- **Input Format**: Accepts HDF5/fast5 files with raw signal data.
- **Output**: Produces compressed HDF5/fast5 files.
- **Use Case**: Storage optimization, data transfer, and backup of nanopore data.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Dependency**: Requires HDF5 library support.
- **Compatibility**: May not work with all HDF5 versions.
- **Decompression**: Requires same plugin for decompression.
- **Performance**: Compression may affect read/write speed.
- **Validation**: Results should be validated for integrity.

## Examples

### Display help
**Args:** `h5ls -h`
**Explanation:** Shows HDF5 tools options.

### Compress file
**Args:** `h5repack -i raw.fast5 -o compressed.fast5`
**Explanation:** Compresses fast5 file using VBZ.

### Check compression
**Args:** `h5dump -H compressed.fast5 | grep compression`
**Explanation:** Verifies compression settings.

### Decompress file
**Args:** `h5repack -i compressed.fast5 -o decompressed.fast5`
**Explanation:** Decompresses fast5 file.

### Batch processing
**Args:** `parallel "h5repack -i {} -o compressed/{/.}.fast5" ::: *.fast5`
**Explanation:** Compresses multiple fast5 files.

### Verify integrity
**Args:** `h5check compressed.fast5`
**Explanation:** Checks file integrity.

### List compressed datasets
**Args:** `h5ls -v compressed.fast5`
**Explanation:** Lists compressed datasets.