---
name: superdsm
category: containerization
description: SuperDSM is a globally optimal segmentation method based on superadditivity and deformable shape models for cell nuclei in fluorescence microscopy images and beyond.
tags: [superdsm, containerization]
author: oxo-call-community
source_url: "https://superdsm.readthedocs.io"
---

## Concepts

- **Tool Overview**: superdsm (v0.4.0) - SuperDSM is a globally optimal segmentation method based on superadditivity and deformable shape models for cell nuclei in fluorescence microscopy images and beyond.
- **Core Function**: SuperDSM is a globally optimal segmentation method based on superadditivity and deformable shape models for cell nuclei in fluorescence microscopy images and beyond.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda superdsm`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `superdsm -i <input_file> -o <output_file>`
**Explanation:** Run superdsm with typical input and output options.
