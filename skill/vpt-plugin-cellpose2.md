---
name: vpt-plugin-cellpose2
category: bioinformatics
description: VPT-Plugin-Cellpose2 - Cellpose2 plugin for VPT.
tags: [vpt-plugin-cellpose2, cell-segmentation, bioinformatics, imaging]
author: oxo-call-community
source_url: "https://github.com/vpt-plugin-cellpose2/"
---

## Concepts

- **Tool Overview**: VPT-Plugin-Cellpose2 - Cell segmentation plugin.
- **Core Function**: Provides Cellpose2 segmentation for VPT.
- **Input**: Image data.
- **Output**: Segmentation masks.
- **Installation**: Install via pip
- **Use Case**: Cell segmentation, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large images.
- **Dependencies**: Requires VPT and Cellpose2.

## Examples

### Run segmentation
**Args:** `vpt segment -i image.tif -o mask.tif --method cellpose2`
**Explanation:** Run Cellpose2 segmentation.

### With options
**Args:** `vpt segment -i image.tif -o mask.tif --method cellpose2 -m cyto`
**Explanation:** Use cytoplasm model.
