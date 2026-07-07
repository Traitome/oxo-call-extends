---
name: cellprofiler-core
category: imaging
description: Core library dependency for CellProfiler cell image analysis software
tags: [cellprofiler-core, cellprofiler, imaging, cell-analysis, microscopy]
author: oxo-call-community
source_url: "https://github.com/CellProfiler/CellProfiler"
---

## Concepts

- **Tool Overview**: cellprofiler-core is the core library component of CellProfiler for image processing.
- **Core Function**: Provides image analysis algorithms and utilities for CellProfiler.
- **Features**: Image segmentation, object detection, measurement, and feature extraction.
- **Input**: Microscopy images in various formats (TIFF, PNG, JPEG).
- **Output**: Analyzed cell measurements and statistics.
- **Application**: High-throughput cell imaging analysis and screening.
- **Installation**: Install via bioconda: `conda install -c bioconda cellprofiler-core`

## Pitfalls

- **Version Compatibility**: Must match CellProfiler version requirements.
- **Image Format**: Supports specific image formats, may need conversion.
- **Memory Usage**: Large image datasets may require significant memory.
- **GPU Acceleration**: Some operations may benefit from GPU.

## Examples

### Import and use in Python
**Args:** `python -c "import cellprofiler_core; print(cellprofiler_core.__version__)"`
**Explanation:** Checks cellprofiler-core version.

### Run headless analysis
**Args:** `cellprofiler --headless --pipeline pipeline.cppipe --input images/ --output results/`
**Explanation:** Runs CellProfiler analysis without GUI.

### Display help
**Args:** `python -c "from cellprofiler_core import help"`
**Explanation:** Shows available modules and documentation.

### Install with CellProfiler
**Args:** `conda install -c bioconda cellprofiler`
**Explanation:** Installs CellProfiler with cellprofiler-core as dependency.