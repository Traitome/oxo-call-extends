---
name: boms
category: expression
description: Cell Segmentation for Spatial Transcriptomics Data using BOMS
tags: [boms, spatial-transcriptomics, segmentation, cell]
author: oxo-call-community
source_url: "https://github.com/ocimakamboj/boms"
---

## Concepts

- **Tool Overview**: BOMS performs cell segmentation for spatial transcriptomics data.
- **Core Function**: Identifies cell boundaries from spatial transcriptomics images and expression data.
- **Input**: Spatial transcriptomics data with imaging and expression matrices.
- **Output**: Cell segmentation masks and assigned transcripts.
- **Application**: Spatial transcriptomics analysis for single-cell resolution.
- **Installation**: Install via bioconda: `conda install -c bioconda boms`

## Pitfalls

- **Image Quality**: Segmentation quality depends on staining image quality.
- **Tissue Type**: Different tissues may require parameter adjustment.
- **Memory Usage**: Large tissue sections require significant memory.
- **Resolution**: Results depend on spatial resolution of input data.

## Examples

### Run cell segmentation
**Args:** `boms -i tissue_image.tif -e expression.h5 -o segmentation_results/`
**Explanation:** Performs cell segmentation on spatial transcriptomics data.

### Adjust segmentation parameters
**Args:** `boms -i tissue.tif -e expr.h5 --threshold 0.5 -o results/`
**Explanation:** Uses custom threshold for cell boundary detection.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
