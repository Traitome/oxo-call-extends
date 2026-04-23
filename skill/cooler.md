---
name: cooler
category: epigenomics
description: Sparse binary format for genomic interaction matrices (Hi-C data)
tags: [cooler, hi-c, genomics, interaction, 3d, chromatin]
author: oxo-call-community
source_url: "https://github.com/open2c/cooler"
---

## Concepts

- **Tool Overview**: Cooler is a support library for a sparse, compressed, and binary format for genomic interaction matrices, also called "cool" format, designed for Hi-C contact matrices.
- **Core Function**: Creates, manipulates, and queries Hi-C contact matrices stored in the cool format (.cool/.mcool files).
- **Input/Output**: Input: Hi-C pairs or matrix data. Output: .cool or .mcool files (multi-resolution). Can also export to text formats.
- **Cool Format**: Uses HDF5-based sparse format for efficient storage of Hi-C matrices at multiple resolutions.
- **Multi-Resolution**: Supports multi-resolution cool files (.mcool) with matrices at different bin sizes (e.g., 1kb, 10kb, 100kb).
- **Integration**: Works with cooltools, HiGlass, and other Hi-C analysis tools. Part of the Open2C ecosystem.

## Pitfalls

- **File Format**: .cool is single-resolution, .mcool is multi-resolution. Most tools prefer .mcool.
- **Memory Usage**: Loading whole-genome matrices at fine resolution can consume significant memory. Use region-based queries.
- **Balancing Required**: Raw contact matrices must be balanced (normalized) before analysis. Use `cooler balance`.
- **Chromosome Naming**: Ensure consistent chromosome naming (chr1 vs 1) between cooler files and other inputs.

## Examples

### Create cool file from pairs
**Args:** `cload pairix -p 4 reference.chromsizes:10000 pairs.pairs output.cool`
**Explanation:** Creates a cool file at 10kb resolution from a pairs file using 4 threads.

### Create cool from matrix
**Args:** `load -i matrix.txt --format bg2 reference.chromsizes:5000 output.cool`
**Explanation:** Creates a cool file at 5kb resolution from a bedGraph2 format matrix.

### Balance (normalize) a cool file
**Args:** `balance output.cool`
**Explanation:** Applies iterative correction (ICE/KR) balancing to normalize the contact matrix for downstream analysis.

### Create multi-resolution file
**Args:** `zoomify -r 1000,5000,10000,50000 output.cool -o output.mcool`
**Explanation:** Creates a multi-resolution cool file with 1kb, 5kb, 10kb, and 50kb resolutions.

### Dump matrix to text
**Args:** `dump -r chr1:10000000-20000000 output.cool`
**Explanation:** Exports a specific genomic region from the cool file as text for inspection.

### List available resolutions
**Args:** `ls output.mcool`
**Explanation:** Lists all available resolutions in a multi-resolution cool file.

### Info about cool file
**Args:** `info output.cool`
**Explanation:** Displays metadata about the cool file including bin size, genome assembly, and statistics.

### Merge multiple cool files
**Args:** `merge sample1.cool sample2.cool -o merged.cool`
**Explanation:** Merges contact matrices from multiple samples into a single cool file.

### Extract specific chromosomes
**Args:** `dump -r chr1,chr2 --balanced output.cool`
**Explanation:** Exports balanced contact matrix for specific chromosomes only.
