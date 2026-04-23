---
name: bftools
category: utility
description: Bio-Formats Command line tools for microscopy image processing
tags: [microscopy, imaging, format-conversion, bio-formats]
author: oxo-call-community
source_url: "https://docs.openmicroscopy.org/bio-formats/"
---

## Concepts
- **Tool Overview**: bftools is a collection of command-line utilities for working with microscopy images using the Bio-Formats library. It provides tools for format conversion, metadata extraction, and image manipulation.
- **Bio-Formats**: Bio-Formats is a Java library for reading and writing microscopy file formats. It supports over 150 proprietary formats.
- **Common Tools**: `bfconvert` (format conversion), `showinf` (display image info), `tiffcomment` (extract TIFF metadata), `xmlvalid` (validate XML metadata).
- **Metadata Handling**: Extracts and preserves rich metadata from proprietary microscopy formats.

## Pitfalls
- **Java Dependency**: Requires Java Runtime Environment.
- **Memory Usage**: Large image files may require increased Java heap memory (`-Xmx` option).
- **Format Support**: Some proprietary formats may have incomplete support or require specific versions.

## Examples
### Convert microscopy image format
**Args:** `bfconvert input.lif output.ome.tiff`
**Explanation:** Converts Leica LIF format to OME-TIFF format.

### Display image information
**Args:** `showinf -omexml image.czi`
**Explanation:** Displays metadata and OME-XML from a Zeiss CZI file.

### Extract TIFF comment
**Args:** `tiffcomment image.tiff`
**Explanation:** Extracts embedded metadata comment from TIFF file.

### Convert with specific series
**Args:** `bfconvert -series 0 input.nd2 output.tiff`
**Explanation:** Converts the first series from a Nikon ND2 file.
