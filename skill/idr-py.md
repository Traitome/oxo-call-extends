---
name: idr-py
category: programming
description: Helper methods for accessing the Image Data Resource (IDR) - a public repository of image-based screening data from the Open Microscopy Environment.
tags: [idr-py, programming, imaging, microscopy, OME]
author: oxo-call-community
source_url: "https://idr.openmicroscopy.org/about/api.html"
---

## Concepts

- **Image Data Resource**: IDR is a public repository hosting high-content screening datasets from microscopy experiments.
- **OMERO Integration**: Built on OMERO (Open Microscopy Environment Remote Objects) for managing and accessing image data.
- **Metadata Querying**: Enables programmatic access to image metadata, annotations, and experimental data.
- **Dataset Exploration**: Facilitates searching and filtering of large-scale imaging datasets.
- **API Access**: Provides Python bindings for the IDR REST API for automated data retrieval and analysis.

## Pitfalls

- **Network Dependencies**: Requires network access to query the remote IDR server.
- **Data Volume**: Large imaging datasets may require significant storage and bandwidth.
- **Authentication**: Some restricted datasets may require authentication credentials.
- **API Rate Limits**: May encounter rate limits when making frequent API requests.
- **Data Format**: Understanding OMERO data structures is required for effective usage.

## Examples

### Connect to IDR
**Args:** `from idr import connection; conn = connection('idr.openmicroscopy.org')`
**Explanation:** Establishes a connection to the IDR server for data access.

### Search datasets by keyword
**Args:** `datasets = conn.getDatasets('siRNA')`
**Explanation:** Retrieves datasets related to siRNA screening from the IDR repository.

### Get image metadata
**Args:** `image = conn.getImage(image_id); metadata = image.getMetadata()`
**Explanation:** Fetches metadata for a specific image by its ID.

### Query annotations
**Args:** `annotations = conn.searchAnnotations('gene:BRCA1')`
**Explanation:** Searches for annotations related to the BRCA1 gene across datasets.

### Download image data
**Args:** `pixels = image.getPrimaryPixels(); data = pixels.getPlane(0, 0, 0)`
**Explanation:** Downloads pixel data for a specific plane from a multi-dimensional image.