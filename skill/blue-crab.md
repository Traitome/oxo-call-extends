---
name: blue-crab
category: formatting
description: Lossless nanopore pod5 to S/BLOW5 file conversion
tags: [blue-crab, nanopore, pod5, blow5, conversion]
author: oxo-call-community
source_url: "https://github.com/Psy-Fer/blue-crab"
---

## Concepts

- **Tool Overview**: Blue-crab converts Nanopore POD5 files to S/BLOW5 format and vice versa.
- **Core Function**: Lossless conversion between Nanopore signal file formats.
- **Formats**: POD5 (Nanopore native), BLOW5 (compressed), SLOW5 (human-readable).
- **Advantage**: BLOW5 format offers better compression and faster access than POD5.
- **Lossless**: No data loss during conversion; all signal data preserved.
- **Installation**: Install via bioconda: `conda install -c bioconda blue-crab`

## Pitfalls

- **File Size**: BLOW5 files may be larger or smaller depending on compression.
- **Index Files**: Conversion generates associated index files.
- **Batch Processing**: Large numbers of files may take significant time.
- **Version Compatibility**: Ensure format version compatibility with downstream tools.

## Examples

### Convert POD5 to BLOW5
**Args:** `blue-crab pod5_convert -i signal.pod5 -o signal.blow5`
**Explanation:** Converts POD5 signal file to compressed BLOW5 format.

### Convert POD5 to SLOW5
**Args:** `blue-crab pod5_convert -i signal.pod5 -o signal.slow5`
**Explanation:** Converts POD5 to human-readable SLOW5 format.

### Batch convert directory
**Args:** `blue-crab pod5_convert -i pod5_dir/ -o blow5_dir/`
**Explanation:** Converts all POD5 files in directory to BLOW5 format.

### Convert BLOW5 back to POD5
**Args:** `blue-crab blow5_convert -i signal.blow5 -o signal.pod5`
**Explanation:** Converts BLOW5 back to POD5 format for Nanopore tools.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
