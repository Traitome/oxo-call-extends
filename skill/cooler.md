---
name: cooler
category: epigenomics
description: Sparse binary format for Hi-C interaction matrices
tags: [cooler, hi-c, genomics, interaction, 3d, chromatin, hdf5]
author: oxo-call-community
source_url: "https://github.com/open2c/cooler"
---

## Concepts

- **Tool Overview**: Cooler is a support library for a sparse, compressed, and binary format for genomic interaction matrices, designed specifically for Hi-C contact data storage and analysis.
- **Core Function**: Creates, manipulates, and queries Hi-C contact matrices stored in the cool format (.cool/.mcool files).
- **Algorithm**: Uses HDF5-based sparse format for efficient storage and retrieval of Hi-C matrices at multiple resolutions.
- **Input**: Hi-C pairs, matrix data in various formats, or existing cool files.
- **Output**: .cool (single-resolution) or .mcool (multi-resolution) files; can export to text formats.
- **Application**: Hi-C data analysis, 3D genome research, chromatin interaction studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cooler`

## Pitfalls

- **File Format**: .cool is single-resolution, .mcool is multi-resolution; most downstream tools prefer .mcool.
- **Memory Usage**: Loading whole-genome matrices at fine resolution requires significant memory; use region-based queries.
- **Balancing Required**: Raw contact matrices must be balanced (normalized) before analysis using `cooler balance`.
- **Chromosome Naming**: Ensure consistent chromosome naming (chr1 vs 1) between cooler files and other inputs.
- **Compression Settings**: Different compression levels affect file size and access speed.

## Examples

### Create cool file from pairs
**Args:** `cooler cload pairix -p 4 reference.chromsizes:10000 pairs.pairs output.cool`
**Explanation:** Creates a cool file at 10kb resolution from a pairs file using 4 threads.

### Balance a cool file
**Args:** `cooler balance output.cool`
**Explanation:** Applies iterative correction (ICE/KR) balancing to normalize the contact matrix.

### Create multi-resolution file
**Args:** `cooler zoomify -r 1000,5000,10000,50000 output.cool -o output.mcool`
**Explanation:** Creates a multi-resolution cool file with multiple bin sizes.

### Dump matrix to text
**Args:** `cooler dump -r chr1:10000000-20000000 output.cool`
**Explanation:** Exports a specific genomic region from the cool file as text.

### Display file info
**Args:** `cooler info output.cool`
**Explanation:** Displays metadata including bin size, genome assembly, and statistics.

### Merge cool files
**Args:** `cooler merge sample1.cool sample2.cool -o merged.cool`
**Explanation:** Merges contact matrices from multiple samples into a single file.