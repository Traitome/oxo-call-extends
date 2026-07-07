---
name: centrosome
category: imaging
description: Open source image processing library and dependency for CellProfiler
tags: [centrosome, imaging, image-processing, cellprofiler, microscopy]
author: oxo-call-community
source_url: "https://github.com/CellProfiler/centrosome"
---

## Concepts

- **Tool Overview**: centrosome is an open-source image processing library used as a dependency for CellProfiler.
- **Core Function**: Provides image processing utilities for biological image analysis.
- **Features**: Image segmentation, object detection, feature extraction, and image transformation.
- **Input**: Microscopy images in various formats (TIFF, PNG, JPEG).
- **Output**: Processed images and measurement data.
- **Application**: Biological image analysis and cell imaging processing.
- **Installation**: Install via bioconda: `conda install -c bioconda centrosome`

## Pitfalls

- **Version Compatibility**: Must match CellProfiler version requirements.
- **Image Format**: Supports specific image formats, may need conversion.
- **Memory Usage**: Large image datasets may require significant memory.
- **GPU Acceleration**: Some operations may benefit from GPU.

## Examples

### Import and use in Python
**Args:** `python -c "import centrosome; print(centrosome.__version__)"`
**Explanation:** Checks centrosome version.

### Process image
**Args:** `python -c "from centrosome import detect; result = detect.cells(image_array)"`
**Explanation:** Detects cells in image using centrosome functions.

### Install with CellProfiler
**Args:** `conda install -c bioconda cellprofiler`
**Explanation:** Installs CellProfiler which includes centrosome as dependency.

### Display help
**Args:** `python -c "from centrosome import help"`
**Explanation:** Shows available modules and documentation.