---
name: rust-proseg
category: spatial_transcriptomics
description: A Rust crate for running Proseg, a cell segmentation method for in situ spatial transcriptomics.
tags: ["rust-proseg", "spatial transcriptomics", "cell segmentation", "Proseg"]
author: oxo-call-community
source_url: "https://github.com/dcjones/proseg/blob/v3.1.1/README.md"
---

## Concepts

- **Tool Overview**: rust-proseg (v3.1.1) is a Rust implementation of Proseg, a cell segmentation algorithm specifically designed for in situ spatial transcriptomics data. It identifies cell boundaries from transcript localization data.
- **Core Function**: Takes spatial transcriptomics data and performs cell segmentation by clustering RNA molecules into individual cells based on their spatial coordinates.
- **Algorithm**: Implements a seeded region growing algorithm with adaptive thresholding to identify cell boundaries from point clouds of RNA transcripts.
- **Input Format**: Spot-based spatial transcriptomics data in CSV/TSV format with x,y coordinates and gene expression.
- **Output Format**: Cell segmentation masks, cell assignments for each spot, visualization of segmentation results.
- **Use Case**: Spatial transcriptomics data analysis, cell type identification, tissue structure analysis.

## Pitfalls

- **Data quality**: Requires high-quality spatial transcriptomics data with accurate spot coordinates.
- **Parameter sensitivity**: Segmentation parameters need careful tuning for different datasets.
- **Cell density**: Works best with moderate cell densities; very sparse or dense data may require adjustment.
- **Tissue type**: Optimized for certain tissue types; may need customization for others.
- **Computational time**: Large datasets can be computationally intensive.
- **Boundary accuracy**: Cell boundaries may not always align with true biological boundaries.

## Examples

### Basic segmentation
**Args:** `proseg -i spots.csv -o segmentation.csv`
**Explanation:** `-i` input spot coordinates; `-o` output cell assignments.

### Specify cell diameter
**Args:** `proseg -i spots.csv -o segmentation.csv -d 50`
**Explanation:** `-d` expected cell diameter in microns.

### Adjust sensitivity
**Args:** `proseg -i spots.csv -o segmentation.csv -s 0.8`
**Explanation:** `-s` sensitivity parameter (0-1). Higher values detect more cells.

### Output visualization
**Args:** `proseg -i spots.csv -o segmentation.csv --plot segmentation.png`
**Explanation:** `--plot` generates visualization of cell segmentation.

### Batch processing
**Args:** `proseg -i spots.csv -o segmentation.csv -b`
**Explanation:** `-b` batch mode for large datasets.

### Custom parameters file
**Args:** `proseg -i spots.csv -o segmentation.csv --config params.toml`
**Explanation:** `--config` uses custom configuration file.

### Verbose mode
**Args:** `proseg -i spots.csv -o segmentation.csv -v`
**Explanation:** `-v` verbose output with segmentation statistics.
