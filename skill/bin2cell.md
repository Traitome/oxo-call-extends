---
name: bin2cell
category: expression
description: Join subcellular Visium HD bins into cells
tags: [spatial-transcriptomics, visium-hd, single-cell, binning]
author: oxo-call-community
source_url: "https://github.com/Teichlab/bin2cell"
---

## Concepts
- **Tool Overview**: bin2cell joins subcellular Visium HD bins into cells for spatial transcriptomics analysis. Visium HD produces data at subcellular resolution (2µm bins), which need to be aggregated into cell-level profiles.
- **Visium HD**: 10x Genomics Visium HD platform generates spatial transcriptomics data at subcellular bin resolution.
- **Binning**: Aggregates small bins (2µm) into cell-level units using cell segmentation boundaries.
- **Applications**: Single-cell resolution spatial transcriptomics, cell type identification in tissue context.

## Pitfalls
- **Segmentation Dependency**: Requires cell segmentation masks or boundaries for proper bin-to-cell assignment.
- **Resolution**: Choice of bin aggregation strategy affects downstream analysis quality.
- **Memory**: High-resolution Visium HD data can be memory-intensive.

## Examples
### Aggregate bins to cells
**Args:** `bin2cell --h5 filtered_feature_bc_matrix.h5 --segmentation segmentation.tif --output cell_matrix.h5`
**Explanation:** Aggregates subcellular bins into cell-level expression profiles using segmentation.

### Process with specific bin size
**Args:** `bin2cell --h5 data.h5 --binsize 8 --output cells.h5`
**Explanation:** Uses 8µm bins for aggregation instead of default 2µm.
