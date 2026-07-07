---
name: stainwarpy
category: image-processing
description: Tools for image registration between multiplexed and H&E stained tissue images.
tags: [stainwarpy, image-registration, spatial-omics, pathology]
author: oxo-call-community
source_url: "https://github.com/tckumarasekara/stainwarpy"
---

## Concepts

- **Tool Overview**: stainwarpy (v0.2.4) is a Python library for registering multiplexed imaging data with H&E stained tissue sections.
- **Core Function**: Aligns spatial transcriptomics or imaging data to histopathology slides for spatial annotation.
- **Algorithm**: Uses feature-based registration with stain normalization for multi-modal image alignment.
- **Input/Output**: Input: Multiplexed images and H&E slides; Output: Registered images with spatial coordinates.
- **Stain Normalization**: Normalizes H&E staining variations across different slides.
- **Installation**: `conda install -c bioconda stainwarpy` or `pip install stainwarpy`.

## Pitfalls

- **Image Quality**: Low-quality or blurry images affect registration accuracy.
- **Stain Variation**: Significant staining differences between slides may require preprocessing.
- **Tissue Deformation**: Physical tissue distortion affects registration precision.
- **Memory Requirements**: Large high-resolution images require significant memory.
- **Computational Time**: Registration of large images can be time-consuming.
- **Feature Matching**: Sparse or ambiguous features may cause registration failures.

## Examples

### Display help
**Args:** `stainwarpy --help`
**Explanation:** Shows available options and usage information.

### Basic registration
**Args:** `stainwarpy register -m multiplex.tiff -h he_image.png -o registered.tiff`
**Explanation:** Register multiplexed image to H&E slide.

### Stain normalization
**Args:** `stainwarpy normalize -i he_image.png -o normalized.png`
**Explanation:** Apply stain normalization to H&E image.

### Batch processing
**Args:** `stainwarpy register -m batch/ -h he_images/ -o output/`
**Explanation:** Process multiple image pairs in batch mode.

### Advanced registration
**Args:** `stainwarpy register -m multi.tiff -h he.png -o reg.tiff --advanced`
**Explanation:** Use advanced registration algorithm for better accuracy.

### Downsample images
**Args:** `stainwarpy register -m multi.tiff -h he.png -o reg.tiff --downsample 2`
**Explanation:** Downsample images for faster processing.

### Verbose mode
**Args:** `stainwarpy register -m multi.tiff -h he.png -o reg.tiff -v`
**Explanation:** Run with detailed logging for debugging.

### Save transformation matrix
**Args:** `stainwarpy register -m multi.tiff -h he.png -o reg.tiff --save-transform transform.txt`
**Explanation:** Save transformation matrix for reproducibility.
