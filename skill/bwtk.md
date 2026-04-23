---
name: bwtk
category: utility
description: BigWig toolkit for manipulating bigWig files
tags: [bwtk, bigwig, genomics, signal, coverage]
author: oxo-call-community
source_url: "https://github.com/bjmt/bwtk"
---

## Concepts

- **Tool Overview**: bwtk is a toolkit for manipulating BigWig files.
- **Core Function**: Extracts, merges, and transforms BigWig signal files.
- **Input**: BigWig files (.bw, .bigWig).
- **Output**: Modified BigWig files or extracted data.
- **Features**: Signal extraction, merging, normalization, and conversion.
- **Installation**: Install via bioconda: `conda install -c bioconda bwtk`

## Pitfalls

- **File Format**: Only supports BigWig format; convert Wig/bedGraph first.
- **Memory Usage**: Large BigWig files require significant memory.
- **Coordinate System**: Uses 0-based coordinates.

## Examples

### Extract signal for region
**Args:** `bwtk extract signal.bw chr1:1000000-2000000 -o region.tsv`
**Explanation:** Extracts signal values for specified genomic region.

### Merge BigWig files
**Args:** `bwtk merge file1.bw file2.bw -o merged.bw`
**Explanation:** Merges multiple BigWig files into one.

### Convert to bedGraph
**Args:** `bwtk tobedgraph signal.bw -o signal.bedgraph`
**Explanation:** Converts BigWig to bedGraph format.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
