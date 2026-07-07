---
name: matlock
category: utility
description: Simple tools for working with Hi-C data and matrix manipulation.
tags: [matlock, Hi-C, matrix-manipulation]
author: oxo-call-community
source_url: "https://github.com/phasegenomics/matlock"
---

## Concepts

- **Tool Overview**: matlock provides utilities for Hi-C data processing and matrix operations.
- **Core Function**: Manipulates and analyzes Hi-C contact matrices.
- **Matrix Operations**: Supports various matrix operations on Hi-C data.
- **Data Format Conversion**: Converts between different Hi-C data formats.
- **Visualization**: Generates visualizations of Hi-C contact maps.
- **Installation**: `conda install -c bioconda matlock`

## Pitfalls

- **Data Format**: Requires specific Hi-C data formats (e.g., .cool, .mcool).
- **Memory Requirements**: Large Hi-C matrices require significant memory.
- **Resolution**: Different resolutions affect matrix size and computation.
- **Normalization**: Matrix normalization affects downstream analysis.
- **Chromosome Handling**: Requires careful handling of chromosome coordinates.
- **Visualization Quality**: Output may require post-processing for publication.

## Examples

### Convert Hi-C format
**Args:** `matlock convert -i input.cool -o output.mcool`
**Explanation:** Converts .cool to .mcool format.

### Extract matrix
**Args:** `matlock extract -i contacts.cool -c chr1 -o chr1.cool`
**Explanation:** Extracts chromosome-specific matrix.

### Matrix balancing
**Args:** `matlock balance -i input.cool -o balanced.cool`
**Explanation:** Performs matrix balancing on Hi-C data.

### Generate heatmap
**Args:** `matlock plot -i input.cool -o heatmap.png`
**Explanation:** Generates Hi-C contact map visualization.

### Resolution change
**Args:** `matlock coarsen -i input.cool -r 100000 -o coarse.cool`
**Explanation:** Changes matrix resolution to 100kb.

### Help documentation
**Args:** `matlock --help`
**Explanation:** Displays available commands and options.
