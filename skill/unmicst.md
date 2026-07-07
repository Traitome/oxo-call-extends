---
name: unmicst
category: bioinformatics
description: UNMICST - Unsupervised Nucleus Classification Tool.
tags: [unmicst, nucleus-segmentation, bioinformatics, imaging]
author: oxo-call-community
source_url: "https://github.com/CellProfiling/HPA-Cell-Segmentation"
---

## Concepts

- **Tool Overview**: UNMICST - A tool for unsupervised nucleus classification in imaging data.
- **Core Function**: Segments and classifies nuclei in microscopy images.
- **Input**: Microscopy images.
- **Output**: Segmented and classified nuclei.
- **Installation**: Install via pip
- **Use Case**: Image analysis, cell biology, bioinformatics.

## Pitfalls

- **Image Quality**: Results depend on image quality.
- **Memory**: May require significant memory for large images.

## Examples

### Segment nuclei
**Args:** `unmicst -i image.tif -o segmentation/`
**Explanation:** Segment nuclei in image.

### With options
**Args:** `unmicst -i image.tif -o segmentation/ -t 8`
**Explanation:** Use 8 threads.
