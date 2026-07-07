---
name: bioformats
category: formatting
description: Python wrapper for Bio-Formats library for reading and writing life sciences image file formats
tags: [image-processing, microscopy, ome-xml, file-formats]
author: oxo-call-community
source_url: "https://pypi.org/project/python-bioformats"
---

## Concepts

- **Tool Overview**: python-bioformats is a Python wrapper for the Bio-Formats Java library, enabling reading and writing of life sciences image file formats from Python.
- **Supported Formats**: Supports over 150 image formats including OME-TIFF, CZI, LIF, Flex, and many microscopy formats.
- **JVM Integration**: Uses python-javabridge to start and interact with a Java Virtual Machine.
- **Metadata Handling**: Full support for OME-XML metadata parsing and generation.
- **Image Reading**: Supports multi-dimensional images (z-stack, time-series, multi-channel).

## Pitfalls

- **JVM Requirements**: Requires Java Virtual Machine and python-javabridge installation.
- **Memory Management**: Need to explicitly start and kill the JVM to avoid memory leaks.
- **Format Specific**: Some formats may require additional native libraries.
- **Performance**: Java bridge overhead may affect performance for large datasets.

## Examples

### Load an image
**Args:** `from bioformats import load_image; img = load_image('image.tif')`
**Explanation:** Loads an image file using Bio-Formats.

### Load specific z-slice
**Args:** `img = load_image('image.tif', z=5, t=0, rescale=True)`
**Explanation:** Loads a specific z-stack slice from a multi-dimensional image.

### Get OME metadata
**Args:** `from bioformats import get_omexml_metadata; xml = get_omexml_metadata('image.tif')`
**Explanation:** Extracts OME-XML metadata from an image file.

### Initialize JVM
**Args:** `import javabridge; import bioformats; javabridge.start_vm(class_path=bioformats.JARS)`
**Explanation:** Starts the Java Virtual Machine with Bio-Formats JARs.