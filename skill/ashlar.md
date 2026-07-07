---
name: ashlar
category: alignment
description: ASHLAR - Alignment by Simultaneous Harmonization of Layer/Adjacency Registration
tags: [ashlar, alignment, image-registration, microscopy, multi-layer]
author: oxo-call-community
source_url: "https://labsyspharm.github.io/ashlar/"
---

## Concepts

- **Tool Overview**: ASHLAR (Alignment by Simultaneous Harmonization of Layer/Adjacency Registration) aligns multi-layer microscopy images through simultaneous registration. Version 1.19.0.
- **Core Function**: Performs simultaneous alignment and registration of multiple image layers or tiles in microscopy datasets.
- **Multi-Layer Alignment**: Aligns multiple image layers or tiles simultaneously for consistent registration across entire dataset.
- **Adjacency Registration**: Uses adjacency information between neighboring tiles for improved alignment accuracy.
- **Microscopy Focus**: Designed for microscopy images including tiled and multi-layer datasets.
- **Transformation Models**: Supports various transformation models (affine, similarity, etc.) for different alignment requirements.
- **Input/Output**: Accepts microscopy image formats (TIFF, etc.) and outputs aligned images with transformation matrices.
- **Installation**: `conda install -c bioconda ashlar` or install from PyPI.

## Pitfalls

- **Image Quality**: Alignment accuracy depends on image quality. Poor quality or noisy images produce poor registration.
- **Overlap Requirements**: Requires sufficient overlap between adjacent tiles for registration. Minimal overlap causes alignment failures.
- **Memory Requirements**: Large multi-layer datasets require significant memory for simultaneous processing.
- **Transformation Model**: Choosing incorrect transformation model causes misalignment. Select model appropriate for your data.
- **Feature Detection**: Images with few distinctive features may fail registration. Ensure adequate features for alignment.
- **Computational Time**: Simultaneous multi-layer alignment can be slow for large datasets.

## Examples

### Display help
**Args:** `ashlar --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic multi-layer alignment
**Args:** `ashlar align --input layer1.tif layer2.tif layer3.tif --output aligned/`
**Explanation:** Aligns three image layers simultaneously. Outputs aligned images to specified directory.

### Specify transformation model
**Args:** `ashlar align --input layer1.tif layer2.tif --output aligned/ --model affine`
**Explanation:** Uses affine transformation model for alignment. Different models suit different deformation types.

### Set registration parameters
**Args:** `ashlar align --input layer1.tif layer2.tif --output aligned/ --max_iterations 100 --tolerance 0.1`
**Explanation:** Sets maximum 100 iterations and 0.1 tolerance for registration convergence.

### Process tiled images
**Args:** `ashlar align --tiles tile_*.tif --output aligned/ --tile_grid 3x3`
**Explanation:** Aligns tiled images in 3x3 grid layout. Uses adjacency information between tiles for improved alignment.

### Export transformation matrices
**Args:** `ashlar align --input layer1.tif layer2.tif --output aligned/ --export_matrices transforms.txt`
**Explanation:** Exports transformation matrices to text file. Useful for downstream analysis or reapplication.

### Multi-threaded processing
**Args:** `ashlar align --input layer1.tif layer2.tif --output aligned/ -t 8`
**Explanation:** Uses 8 threads for parallel processing. Speeds up alignment for large datasets.

### Visualize alignment
**Args:** `ashlar visualize --input layer1.tif layer2.tif --output overlay.png`
**Explanation:** Creates overlay visualization of aligned layers for quality assessment.